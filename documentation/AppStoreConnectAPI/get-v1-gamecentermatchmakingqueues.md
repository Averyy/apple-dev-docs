# List All Queues

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get information about all queues.

**Availability**:
- App Store Connect API 3.1+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterMatchmakingQueues`

## Parameters

### Query Parameters

- `fields[gameCenterMatchmakingQueues]` ([string]): The fields of the queues to include in the response.

  **Allowed Values**: `referenceName`, `classicMatchmakingBundleIds`, `ruleSet`, `experimentRuleSet`
- `fields[gameCenterMatchmakingRuleSets]` ([string]): **Allowed Values**: `referenceName`, `ruleLanguageVersion`, `minPlayers`, `maxPlayers`, `teams`, `rules`, `matchmakingQueues`
- `include` ([string]): The type of rule set to include in the response.

  **Allowed Values**: `ruleSet`, `experimentRuleSet`
- `limit` (integer): The maximum number of queues to fetch.

  **Maximum**: `200`

## Responses

- `200` OK (`GameCenterMatchmakingQueuesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Reading queue information
- [Read Queue Information](./get-v1-gamecentermatchmakingqueues-_id_.md)
  Get information about a specific queue and its related objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecentermatchmakingqueues)*