# Get Numeric Rule Results

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get the results of a specific matchmaking rule that returns numeric values.

**Availability**:
- App Store Connect API 3.1+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterMatchmakingRules/{id}/metrics/matchmakingNumberRuleResults`

## Parameters

- `filter[gameCenterMatchmakingQueue]` (string): The fields of the queues to include in the response.
- `granularity` (string) *(required)*: The level of information you want in the response, specified as a time interval for the data collection, using the ISO 8601 format for durations.
- `groupBy` ([string]): Organizes the results by queue.
- `limit` (integer): The maximum number of results to include.
- `sort` ([string]): Sort results by the specified order. For example, `count` sorts the results by decreasing number of players that Game Center finds.

## See Also

- [Get boolean rule results](get-v1-gamecentermatchmakingrules-_id_-metrics-matchmakingbooleanruleresults.md)
  Get the results of a specific matchmaking rule that returns Boolean values.
- [Get Matchmaking Rule Errors](get-v1-gamecentermatchmakingrules-_id_-metrics-matchmakingruleerrors.md)
  Get errors that occur for a specific matchmaking rule.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecentermatchmakingrules-_id_-metrics-matchmakingnumberruleresults)*