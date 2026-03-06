# Get one-time request status

**Framework**: Account Data Transfer  
**Kind**: httpRequest

Find the status of a one-time download request.

**Availability**:
- Account Data Transfer 1.0+

#### Overview

**Request**:

```None
% curl -X GET \
  -H "Authorization: Bearer [ACCESS_TOKEN]" \
  -H "X-Apple-Transaction-Id: E3857B28-7FC4-41C8-AC54-08E121E26F59" \
  -H "Accept: application/json" \
  https://accountdatatransfer.apple.com/api/transfer/accountdata/11619695-72C0-4FFD-858A-1E152DCF0838
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

`GET https://accountdatatransfer.apple.com/api/transfer/accountdata/{requestId}`

## Parameters

- `requestId` (string) *(required)*: A UUID that identifies the download request.

## See Also

- [Get recurring request status](get-recurring-request-status.md)
  Get the status of an instance of a recurring download request.
- [object RequestStatus](requeststatus.md)
  An object that represents the status of a download request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accountdatatransfer/get-one-time-request-status)*