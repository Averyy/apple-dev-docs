# SubmissionResponse

**Framework**: Notary API  
**Kind**: dictionary

The notary service’s response to a request for the status of a submission.

**Availability**:
- Notary API 2.0.0+

## Declaration

```swift
object SubmissionResponse
```

#### Discussion

You receive a structure of this type in response to a call to the [`Get Submission Status`](get-submission-status.md) endpoint.

## Topics

### Objects
- [object SubmissionResponse.Data](submissionresponse/data-data.dictionary.md)
  Information that the service provides about the status of a notarization submission.
- [object SubmissionResponse.Meta](submissionresponse/meta-data.dictionary.md)
  An empty object.

## See Also

- [Get Submission Status](get-submission-status.md)
  Fetch the status of a software notarization submission.
- [Get Submission Log](get-submission-log.md)
  Fetch details about a single completed notarization.
- [object SubmissionLogURLResponse](submissionlogurlresponse.md)
  The notary service’s response to a request for the log information about a completed submission.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notaryapi/submissionresponse)*