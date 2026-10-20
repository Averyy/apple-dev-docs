# Get recurring request status

**Framework**: Account Data Transfer  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get the status of an instance of a recurring download request.

**Availability**:
- Account Data Transfer 1.0+

#### Overview

**Request**:

```
% curl -X GET \
  -H "Authorization: Bearer [ACCESS_TOKEN]" \
  -H "X-Apple-Transaction-Id: E3857B28-7FC4-41C8-AC54-08E121E26F59" \
  -H "Accept: application/json" \
  https://accountdatatransfer.apple.com/api/transfer/accountdata/EABD06C0-9210-47FF-83C4-318CF8520644/7BBBD45D-638B-4DB5-8B02-F23FDB15EDA7
```

**Response**:

```
{
  "jobStatus": "in_progress",
  "status": "success",
  "statusCheckDelay": 86400
}
```

## Endpoint

`GET https://accountdatatransfer.apple.com/api/transfer/accountdata/{parentRequestId}/{requestId}`

## Parameters

### Path Parameters

- `parentRequestId` (string) *(required)*: A UUID that identifies the series of recurring download requests.
- `requestId` (string) *(required)*: A UUID that identifies the individual request.

## Responses

- `200` OK (`RequestStatus`, `application/json`)
- `400` Bad Request
- `401` Unauthorized
- `403` Forbidden
- `500` Internal Server Error

## See Also

### Status
- [Get one-time request status](./get-one-time-request-status.md)
  Find the status of a one-time download request.
- [object RequestStatus](./requeststatus.md)
  An object that represents the status of a download request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accountdatatransfer/get-recurring-request-status)*