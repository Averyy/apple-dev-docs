# NewSubmissionRequest

**Framework**: Notary API  
**Kind**: dictionary

Data that you provide when starting a submission to the notary service.

**Availability**:
- Notary API 2.0.0+

## Declaration

```swift
object NewSubmissionRequest
```

#### Discussion

Use a structure of this type as the HTTP body when you post to the [`Submit Software`](submit-software.md) endpoint.

## Topics

### Objects
- [object NewSubmissionRequest.Notifications](newsubmissionrequest/notifications-data.dictionary.md)
  A notification that the notary service sends you when notarization finishes.

## See Also

- [Submit Software](submit-software.md)
  Start the process of uploading a new version of your software to the notary service.
- [object NewSubmissionResponse](newsubmissionresponse.md)
  The notary service’s response to a software submission.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notaryapi/newsubmissionrequest)*