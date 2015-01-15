# Copyright 2014 NEC Corporation.  All rights reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import copy

from tempest.api_schema.response.compute import aggregates

delete_aggregate = {
    'status_code': [204]
}

create_aggregate = copy.deepcopy(aggregates.common_create_aggregate)
# V3 API's response status_code is 201
create_aggregate['status_code'] = [201]

aggregate_add_remove_host = copy.deepcopy(aggregates.aggregate_add_remove_host)
# V3 API's response status_code is 202
aggregate_add_remove_host['status_code'] = [202]