# JobSubmission

**Framework**: Account Data Transfer  
**Kind**: dictionary

An object that describes a submission that requests someone’s data.

**Availability**:
- Account Data Transfer 1.0+

## Declaration

```swift
object JobSubmission
```

## Properties

- `mode` (string): Whether you want a one-time download, a daily download for 30 days, or a weekly download for 180 days.

## See Also

- [Submit request](submit-request.md)
  Starts preparing someone’s data for download.
- [object CreatedJob](createdjob.md)
  An object that represents a newly created download request.
- [Resubmit request](resubmit-request.md)
  Enqueue the next instance of a recurring request.
- [object ResubmissionRequest](resubmissionrequest.md)
  An object that describes a request to resubmit a recurring download request.
- [object ResubmissionResponse](resubmissionresponse.md)
  An object that represents a resubmitted recurring download request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accountdatatransfer/jobsubmission)*