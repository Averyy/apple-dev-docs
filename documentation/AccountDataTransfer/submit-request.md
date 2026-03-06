# Submit request

**Framework**: Account Data Transfer  
**Kind**: httpRequest

Starts preparing someone’s data for download.

**Availability**:
- Account Data Transfer 1.0+

#### Overview

Request the `app-store` data type to get App Store information and app-install activity.

##### Request a One Time Download

**Request**:

```None
% curl -X POST \
  -H "Authorization: Bearer [ACCESS_TOKEN]" \
  -H "X-Apple-Transaction-Id: E3857B28-7FC4-41C8-AC54-08E121E26F59" \
  -H "Content-Type: application/json" \
  -d '{ "mode": "ONE_TIME" }' \
  https://accountdatatransfer.apple.com/api/transfer/accountdata/submit
```

**Response**:

```None
{
  "requestId": "11619695-72C0-4FFD-858A-1E152DCF0838",
  "status": "in_progress",
  "statusCheckDelay": 86400
}
```

##### Request a Recurring Download

**Request**:

```None
% curl -X POST \
  -H "Authorization: Bearer [ACCESS_TOKEN]" \
  -H "X-Apple-Transaction-Id: E3857B28-7FC4-41C8-AC54-08E121E26F59" \
  -H "Content-Type: application/json" \
  -d '{ "mode": "DAILY_30" }' \
  https://accountdatatransfer.apple.com/api/transfer/accountdata/submit
```

**Response**:

```None
{
  "parentRequestId": "EABD06C0-9210-47FF-83C4-318CF8520644",
  "requestId": "7BBBD45D-638B-4DB5-8B02-F23FDB15EDA7",
  "status": "in_progress",
  "statusCheckDelay": 86400
}
```

## Endpoint

`POST https://accountdatatransfer.apple.com/api/transfer/accountdata/submit`

## Request Body

The description of the new download request.

## See Also

- [object JobSubmission](jobsubmission.md)
  An object that describes a submission that requests someone’s data.
- [object CreatedJob](createdjob.md)
  An object that represents a newly created download request.
- [Resubmit request](resubmit-request.md)
  Enqueue the next instance of a recurring request.
- [object ResubmissionRequest](resubmissionrequest.md)
  An object that describes a request to resubmit a recurring download request.
- [object ResubmissionResponse](resubmissionresponse.md)
  An object that represents a resubmitted recurring download request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accountdatatransfer/submit-request)*