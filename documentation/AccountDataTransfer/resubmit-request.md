# Resubmit request

**Framework**: Account Data Transfer  
**Kind**: httpRequest

Enqueue the next instance of a recurring request.

**Availability**:
- Account Data Transfer 1.0+

#### Overview

The `requestId` you pass must be the most recent instance of the series identified by the `parentRequestId`.

**Request**:

```None
% curl -X POST \
  -H "Authorization: Bearer [ACCESS_TOKEN]" \
  -H "X-Apple-Transaction-Id: E3857B28-7FC4-41C8-AC54-08E121E26F59" \
  -H "Content-Type: application/json" \
  -d '{ "parentRequestId": "EABD06C0-9210-47FF-83C4-318CF8520644", "requestId": "7BBBD45D-638B-4DB5-8B02-F23FDB15EDA7" }' \
  https://accountdatatransfer.apple.com/api/transfer/accountdata/resubmit
```

**Response**:

```None
{
  "parentRequestId": "EABD06C0-9210-47FF-83C4-318CF8520644",
  "requestId": "A2DFE115-F039-4FC4-8286-7EAD51D91D8B",
  "status": "success",
  "statusCheckDelay": 86400
}
```

## Endpoint

`POST https://accountdatatransfer.apple.com/api/transfer/accountdata/resubmit`

## Request Body

The recurring request for which you submit a new instance.

## See Also

- [Submit request](submit-request.md)
  Starts preparing someone’s data for download.
- [object JobSubmission](jobsubmission.md)
  An object that describes a submission that requests someone’s data.
- [object CreatedJob](createdjob.md)
  An object that represents a newly created download request.
- [object ResubmissionRequest](resubmissionrequest.md)
  An object that describes a request to resubmit a recurring download request.
- [object ResubmissionResponse](resubmissionresponse.md)
  An object that represents a resubmitted recurring download request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accountdatatransfer/resubmit-request)*