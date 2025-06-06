# Resubmit request

**Framework**: Account Data Transfer  
**Kind**: httpRequest

Enqueue the next instance of a recurring request.

**Availability**:
- Account Data Transfer 1.0+

#### Overview

The `requestId` you pass must be the most recent instance of the series identified by the `parentRequestId`.

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