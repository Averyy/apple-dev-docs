# ResubmissionRequest

**Framework**: App Data Transfer  
**Kind**: dictionary

An object that describes a request to resubmit a recurring download request.

**Availability**:
- App Data Transfer 1.0+

## Declaration

```swift
object ResubmissionRequest
```

#### Overview

Use the `parentRequestId` and `requestId` returned by [`Submit request`](submit-request.md), or your most recent call to [`Resubmit request`](resubmit-request.md).

## See Also

- [Submit request](submit-request.md)
  Starts preparing someone’s data for download.
- [object JobSubmission](jobsubmission.md)
  An object that describes a submission that requests someone’s data.
- [object CreatedJob](createdjob.md)
  An object that represents a newly created download request.
- [Resubmit request](resubmit-request.md)
  Enqueue the next instance of a recurring request.
- [object ResubmissionResponse](resubmissionresponse.md)
  An object that represents a resubmitted recurring download request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appdatatransfer/resubmissionrequest)*