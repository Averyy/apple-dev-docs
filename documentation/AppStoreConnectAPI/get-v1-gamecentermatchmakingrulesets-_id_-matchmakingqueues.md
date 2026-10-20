# List Queues in a Rule Set

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get information about queues that belong to a rule set.

**Availability**:
- App Store Connect API 3.1+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterMatchmakingRuleSets/{id}/matchmakingQueues`

## Parameters

### Path Parameters

- `id` (string) *(required)*: The unique identifier for the rule set.

### Query Parameters

- `fields[gameCenterMatchmakingQueues]` ([string]): The fields of queues to include in the response.

  **Allowed Values**: `referenceName`, `classicMatchmakingBundleIds`, `ruleSet`, `experimentRuleSet`
- `fields[gameCenterMatchmakingRuleSets]` ([string]): The fields of the rule set to include.

  **Allowed Values**: `referenceName`, `ruleLanguageVersion`, `minPlayers`, `maxPlayers`, `teams`, `rules`, `matchmakingQueues`
- `include` ([string]): The relationships to include in the response.

  **Allowed Values**: `ruleSet`, `experimentRuleSet`
- `limit` (integer): The maximum number of queues to fetch.

  **Maximum**: `200`

## Responses

- `200` OK (`GameCenterMatchmakingQueuesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Reading rule set information
- [List All Rule Sets](./get-v1-gamecentermatchmakingrulesets.md)
  Get information about all rule sets and their associated objects.
- [Read Rule Set Information](./get-v1-gamecentermatchmakingrulesets-_id_.md)
  Get information about a specific rule set and its related objects.
- [List matchmaking queue IDs for a Game Center matchmaking rule set](./get-v1-gamecentermatchmakingrulesets-_id_-relationships-matchmakingqueues.md)
- [List Rules in a Rule Set](./get-v1-gamecentermatchmakingrulesets-_id_-rules.md)
  Get information about the rules in a rule set.
- [List rule IDs for a Game Center matchmaking rule set](./get-v1-gamecentermatchmakingrulesets-_id_-relationships-rules.md)
- [List Teams in a Rule Set](./get-v1-gamecentermatchmakingrulesets-_id_-teams.md)
  Get information about the teams in a rule set.
- [List team IDs for a Game Center matchmaking rule set](./get-v1-gamecentermatchmakingrulesets-_id_-relationships-teams.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecentermatchmakingrulesets-_id_-matchmakingqueues)*