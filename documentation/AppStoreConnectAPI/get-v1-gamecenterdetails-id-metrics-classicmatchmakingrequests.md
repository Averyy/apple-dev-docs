# Get classic match requests

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get match requests that don’t use matchmaking rules.

**Availability**:
- App Store Connect API 3.1+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterDetails/{id}/metrics/classicMatchmakingRequests`

## Parameters

- `filter[result]` (string): The types of the match requests to include in the response.
- `granularity` (string) *(required)*: The level of information you want in the response, specified as a time interval for the data collection, using the ISO 8601 format for durations.
- `groupBy` ([string]): If `result`, organizes the match requests by outcome (matched, canceled, and expired).
- `limit` (integer): The maximum number of match requests to fetch.
- `sort` ([string]): Sort results by the specified order. For example, `count` sorts the results by decreasing number of players that Game Center finds.

## See Also

- [Get rule-based match requests](get-v1-gamecenterdetails-_id_-metrics-rulebasedmatchmakingrequests.md)
  Get match requests that use matchmaking rules.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenterdetails-_id_-metrics-classicmatchmakingrequests)*