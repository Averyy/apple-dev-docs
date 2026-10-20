# Get Classic Match Requests

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get match requests that don’t use matchmaking rules.

**Availability**:
- App Store Connect API 3.1+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterDetails/{id}/metrics/classicMatchmakingRequests`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the [`GameCenterDetail`](./gamecenterdetail.md) resource object. You can obtain this resource ID from the [`List apps`](./get-v1-apps.md) response.

### Query Parameters

- `filter[result]` (string): The types of the match requests to include in the response.

  **Allowed Values**: `MATCHED`, `CANCELED`, `EXPIRED`
- `granularity` (string) *(required)*: The level of information you want in the response, specified as a time interval for the data collection, using the ISO 8601 format for durations.

  **Allowed Values**: `P1D`, `PT1H`, `PT15M`
- `groupBy` ([string]): If `result`, organizes the match requests by outcome (matched, canceled, and expired).

  **Allowed Values**: `result`
- `limit` (integer): The maximum number of match requests to fetch.

  **Maximum**: `200`
- `sort` ([string]): Sort results by the specified order. For example, `count` sorts the results by decreasing number of players that Game Center finds.

  **Allowed Values**: `count`, `-count`, `averageSecondsInQueue`, `-averageSecondsInQueue`, `p50SecondsInQueue`, `-p50SecondsInQueue`, `p95SecondsInQueue`, `-p95SecondsInQueue`

## Responses

- `200` OK (`GameCenterMatchmakingAppRequestsV1MetricResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting match request metrics
- [Get Rule-Based Match Requests](./get-v1-gamecenterdetails-_id_-metrics-rulebasedmatchmakingrequests.md)
  Get match requests that use matchmaking rules.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenterdetails-_id_-metrics-classicmatchmakingrequests)*