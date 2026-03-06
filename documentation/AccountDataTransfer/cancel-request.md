# Cancel request

**Framework**: Account Data Transfer  
**Kind**: httpRequest

Tells the server to stop processing an active request.

**Availability**:
- Account Data Transfer 1.0+

#### Overview

A cancellation request only succeeds if the request is currently in progress.

##### Cancel a One Time Download

**Request**:

```None
% curl -X POST \
  -H "Authorization: Bearer [ACCESS_TOKEN]" \
  -H "X-Apple-Transaction-Id: E3857B28-7FC4-41C8-AC54-08E121E26F59" \
  -H "Content-Type: application/json" \
  -d '{ "requestId": "11619695-72C0-4FFD-858A-1E152DCF0838" }' \
  https://accountdatatransfer.apple.com/api/transfer/accountdata/cancel
```

**Response**:

```None
{
  "jobStatus": "cancelled",
  "status": "success"
}
```

##### Cancel a Recurring Download

**Request**:

```None
% curl -X POST \
  -H "Authorization: Bearer [ACCESS_TOKEN]" \
  -H "X-Apple-Transaction-Id: E3857B28-7FC4-41C8-AC54-08E121E26F59" \
  -H "Content-Type: application/json" \
  -d '{ "requestId": "7BBBD45D-638B-4DB5-8B02-F23FDB15EDA7" }' \
  https://accountdatatransfer.apple.com/api/transfer/accountadata/cancel
```

**Response**:

```None
{
  "jobStatus": "cancelled",
  "status": "success"
}
```

## Endpoint

`POST https://accountdatatransfer.apple.com/api/transfer/accountdata/cancel`

## Request Body

An object that identifies the request to cancel.

## See Also

- [object CancellationRequest](cancellationrequest.md)
  An object that identifies a one-time request, or an individual instance of a recurring request, to cancel.
- [object CancellationResponse](cancellationresponse.md)
  An object that describes the outcome of canceling a download request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accountdatatransfer/cancel-request)*