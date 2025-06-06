# SubmissionLogURLResponse

**Framework**: Notary API  
**Kind**: dictionary

The notary service’s response to a request for the log information about a completed submission.

**Availability**:
- Notary API 2.0.0+

## Declaration

```swift
object SubmissionLogURLResponse
```

#### Discussion

You receive a structure of this type in response to a call to the [`Get Submission Log`](get-submission-log.md) endpoint.

## Topics

### Objects
- [object SubmissionLogURLResponse.Data](submissionlogurlresponse/data-data.dictionary.md)
  Data that indicates how to get the log information for a particular submission.
- [object SubmissionLogURLResponse.Meta](submissionlogurlresponse/meta-data.dictionary.md)
  An empty object.

## See Also

- [Get Submission Status](get-submission-status.md)
  Fetch the status of a software notarization submission.
- [object SubmissionResponse](submissionresponse.md)
  The notary service’s response to a request for the status of a submission.
- [Get Submission Log](get-submission-log.md)
  Fetch details about a single completed notarization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notaryapi/submissionlogurlresponse)*