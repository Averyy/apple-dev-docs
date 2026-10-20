# Get Matchmaking Rule Errors

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get errors that occur for a specific matchmaking rule.

**Availability**:
- App Store Connect API 3.1+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterMatchmakingRules/{id}/metrics/matchmakingRuleErrors`

## Parameters

### Path Parameters

- `id` (string) *(required)*: The unique identifier for the rule.

### Query Parameters

- `filter[gameCenterMatchmakingQueue]` (string): The fields of the queues to include in the response.
- `granularity` (string) *(required)*: The level of information you want in the response, specified as a time interval for the data collection, using the ISO 8601 format for durations.

  **Allowed Values**: `P1D`, `PT1H`, `PT15M`
- `groupBy` ([string]): Organizes the results by queue.

  **Allowed Values**: `gameCenterMatchmakingQueue`
- `limit` (integer): The maximum number of results to include.

  **Maximum**: `200`
- `sort` ([string]): Sort results by the decreasing or increasing number of players that Game Center finds.

  **Allowed Values**: `count`, `-count`

## Responses

- `200` OK (`GameCenterMatchmakingRuleErrorsV1MetricResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting rule results and errors
- [Get boolean rule results](./get-v1-gamecentermatchmakingrules-_id_-metrics-matchmakingbooleanruleresults.md)
  Get the results of a specific matchmaking rule that returns Boolean values.
- [Get Numeric Rule Results](./get-v1-gamecentermatchmakingrules-_id_-metrics-matchmakingnumberruleresults.md)
  Get the results of a specific matchmaking rule that returns numeric values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecentermatchmakingrules-_id_-metrics-matchmakingruleerrors)*