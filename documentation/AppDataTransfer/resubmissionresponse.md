# ResubmissionResponse

**Framework**: App Data Transfer  
**Kind**: dictionary

An object that represents a resubmitted recurring download request.

**Availability**:
- App Data Transfer 1.0+

## Declaration

```swift
object ResubmissionResponse
```

## Properties

- `parentRequestId` (string): A UUID that identifies the recurring request series.
- `requestId` (string): A UUID that identifies the new request.
- `status` (string): `success` if the server resubmitted the request; `error` otherwise.
- `statusCheckDelay` (integer): The number of seconds to wait before you call [`Get recurring request status`](get-recurring-request-status.md).

## See Also

- [Submit request](submit-request.md)
  Starts preparing someone’s data for download.
- [object JobSubmission](jobsubmission.md)
  An object that describes a submission that requests someone’s data.
- [object CreatedJob](createdjob.md)
  An object that represents a newly created download request.
- [Resubmit request](resubmit-request.md)
  Enqueue the next instance of a recurring request.
- [object ResubmissionRequest](resubmissionrequest.md)
  An object that describes a request to resubmit a recurring download request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appdatatransfer/resubmissionresponse)*