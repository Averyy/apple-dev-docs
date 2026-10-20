# Submit request

**Framework**: App Data Transfer  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Starts preparing someone’s data for download.

**Availability**:
- App Data Transfer 1.0+

#### Overview

Request the `app-store` data type to get App Store information and app-install activity.

##### Request a one-time download

**Request**:

```
% curl -X POST \
  -H "Authorization: Bearer [ACCESS_TOKEN]" \
  -H "X-Apple-Transaction-Id: E3857B28-7FC4-41C8-AC54-08E121E26F59" \
  -H "Content-Type: application/json" \
  -d '{ "mode": "ONE_TIME" }' \
  https://appdatatransfer.apple.com/api/transfer/appdata/submit
```

**Response**:

```
{
  "requestId": "11619695-72C0-4FFD-858A-1E152DCF0838",
  "status": "in_progress",
  "statusCheckDelay": 86400
}
```

##### Request a recurring download

**Request**:

```
% curl -X POST \
  -H "Authorization: Bearer [ACCESS_TOKEN]" \
  -H "X-Apple-Transaction-Id: E3857B28-7FC4-41C8-AC54-08E121E26F59" \
  -H "Content-Type: application/json" \
  -d '{ "mode": "DAILY_30" }' \
  https://appdatatransfer.apple.com/api/transfer/appdata/submit
```

**Response**:

```
{
  "parentRequestId": "EABD06C0-9210-47FF-83C4-318CF8520644",
  "requestId": "7BBBD45D-638B-4DB5-8B02-F23FDB15EDA7",
  "status": "in_progress",
  "statusCheckDelay": 86400
}
```

## Endpoint

`POST https://appdatatransfer.apple.com/api/transfer/appdata/submit`

## Request Body

**Content-Type**: `application/json`  
**Type**: `JobSubmission`

The description of the new download request.

## Responses

- `200` OK (`CreatedJob`, `application/json`)
- `400` Bad Request
- `401` Unauthorized
- `403` Forbidden
- `500` Internal Server Error

## See Also

### Request creation
- [object JobSubmission](./jobsubmission.md)
  An object that describes a submission that requests someone’s data.
- [object CreatedJob](./createdjob.md)
  An object that represents a newly created download request.
- [Resubmit request](./resubmit-request.md)
  Enqueue the next instance of a recurring request.
- [object ResubmissionRequest](./resubmissionrequest.md)
  An object that describes a request to resubmit a recurring download request.
- [object ResubmissionResponse](./resubmissionresponse.md)
  An object that represents a resubmitted recurring download request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appdatatransfer/submit-request)*