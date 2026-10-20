# Read Beta Crash Log Information

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get crash log details for a specific beta feedback crash submission.

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/betaCrashLogs/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the `betaCrashLogs` resource ID from the [`Read the Crash Log for a Beta Feedback Crash Submission`](./get-v1-betafeedbackcrashsubmissions-_id_-crashlog.md) response.

### Query Parameters

- `fields[betaCrashLogs]` ([string]): **Allowed Values**: `logText`

## Responses

- `200` OK (`BetaCrashLogResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-betacrashlogs-_id_)*