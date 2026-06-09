# Read Rule Set Information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about a specific rule set and its related objects.

**Availability**:
- App Store Connect API 3.1+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterMatchmakingRuleSets/{id}`

## Parameters

- `fields[gameCenterMatchmakingQueues]` ([string]): The fields of the queues to include in the response.
- `fields[gameCenterMatchmakingRuleSets]` ([string]): The fields of the rule set to include in the response.
- `fields[gameCenterMatchmakingRules]` ([string]): The fields of the rules to include in the response.
- `fields[gameCenterMatchmakingTeams]` ([string]): The fields of the teams to include in the response.
- `include` ([string]): The relationships to include in the response.
- `limit[matchmakingQueues]` (integer): The maximum number of queues to fetch.
- `limit[rules]` (integer): The maximum number of rules to fetch.
- `limit[teams]` (integer): The maximum number of teams to fetch.

## See Also

- [List All Rule Sets](get-v1-gamecentermatchmakingrulesets.md)
  Get information about all rule sets and their associated objects.
- [List Queues in a Rule Set](get-v1-gamecentermatchmakingrulesets-_id_-matchmakingqueues.md)
  Get information about queues that belong to a rule set.
- [List matchmaking queue IDs for a Game Center matchmaking rule set](get-v1-gamecentermatchmakingrulesets-_id_-relationships-matchmakingqueues.md)
- [List Rules in a Rule Set](get-v1-gamecentermatchmakingrulesets-_id_-rules.md)
  Get information about the rules in a rule set.
- [List rule IDs for a Game Center matchmaking rule set](get-v1-gamecentermatchmakingrulesets-_id_-relationships-rules.md)
- [List Teams in a Rule Set](get-v1-gamecentermatchmakingrulesets-_id_-teams.md)
  Get information about the teams in a rule set.
- [List team IDs for a Game Center matchmaking rule set](get-v1-gamecentermatchmakingrulesets-_id_-relationships-teams.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecentermatchmakingrulesets-_id_)*