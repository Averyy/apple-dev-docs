# List Teams in a Rule Set

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about the teams in a rule set.

**Availability**:
- App Store Connect API 3.1+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterMatchmakingRuleSets/{id}/teams`

## Parameters

- `fields[gameCenterMatchmakingTeams]` ([string]): The fields of the teams to include in the response.
- `limit` (integer): The maximum number of teams to fetch.

## See Also

- [List All Rule Sets](get-v1-gamecentermatchmakingrulesets.md)
  Get information about all rule sets and their associated objects.
- [Read Rule Set Information](get-v1-gamecentermatchmakingrulesets-_id_.md)
  Get information about a specific rule set and its related objects.
- [List Queues in a Rule Set](get-v1-gamecentermatchmakingrulesets-_id_-matchmakingqueues.md)
  Get information about queues that belong to a rule set.
- [GET /v1/gameCenterMatchmakingRuleSets/{id}/relationships/matchmakingQueues](get-v1-gamecentermatchmakingrulesets-_id_-relationships-matchmakingqueues.md)
- [List Rules in a Rule Set](get-v1-gamecentermatchmakingrulesets-_id_-rules.md)
  Get information about the rules in a rule set.
- [GET /v1/gameCenterMatchmakingRuleSets/{id}/relationships/rules](get-v1-gamecentermatchmakingrulesets-_id_-relationships-rules.md)
- [GET /v1/gameCenterMatchmakingRuleSets/{id}/relationships/teams](get-v1-gamecentermatchmakingrulesets-_id_-relationships-teams.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecentermatchmakingrulesets-_id_-teams)*