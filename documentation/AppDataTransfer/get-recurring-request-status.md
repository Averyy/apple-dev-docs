# Get recurring request status

**Framework**: App Data Transfer  
**Kind**: httpRequest

Get the status of an instance of a recurring download request.

**Availability**:
- App Data Transfer 1.0+

#### Overview

**Request**:

```None
% curl -X GET \
  -H "Authorization: Bearer [ACCESS_TOKEN]" \
  -H "X-Apple-Transaction-Id: E3857B28-7FC4-41C8-AC54-08E121E26F59" \
  -H "Accept: application/json" \
  https://appdatatransfer.apple.com/api/transfer/appdata/EABD06C0-9210-47FF-83C4-318CF8520644/7BBBD45D-638B-4DB5-8B02-F23FDB15EDA7
```

**Response**:

```None
{
  "jobStatus": "in_progress",
  "status": "success",
  "statusCheckDelay": 86400
}
```

## Endpoint

`GET https://appdatatransfer.apple.com/api/transfer/appdata/{parentRequestId}/{requestId}`

## Parameters

- `parentRequestId` (string) *(required)*: A UUID that identifies the series of recurring download requests.
- `requestId` (string) *(required)*: A UUID that identifies the individual request.

## See Also

- [Get one-time request status](get-one-time-request-status.md)
  Find the status of a one-time download request.
- [object RequestStatus](requeststatus.md)
  An object that represents the status of a download request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appdatatransfer/get-recurring-request-status)*