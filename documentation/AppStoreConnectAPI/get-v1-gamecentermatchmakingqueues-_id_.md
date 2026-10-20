# Read Queue Information

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get information about a specific queue and its related objects.

**Availability**:
- App Store Connect API 3.1+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterMatchmakingQueues/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: The unique identifier for the queue.

### Query Parameters

- `fields[gameCenterMatchmakingQueues]` ([string]): The fields of the queue to include in the response.

  **Allowed Values**: `referenceName`, `classicMatchmakingBundleIds`, `ruleSet`, `experimentRuleSet`
- `include` ([string]): The type of rule set to include in the response.

  **Allowed Values**: `ruleSet`, `experimentRuleSet`
- `fields[gameCenterMatchmakingRuleSets]` ([string]): **Allowed Values**: `referenceName`, `ruleLanguageVersion`, `minPlayers`, `maxPlayers`, `teams`, `rules`, `matchmakingQueues`

## Responses

- `200` OK (`GameCenterMatchmakingQueueResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Reading queue information
- [List All Queues](./get-v1-gamecentermatchmakingqueues.md)
  Get information about all queues.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecentermatchmakingqueues-_id_)*