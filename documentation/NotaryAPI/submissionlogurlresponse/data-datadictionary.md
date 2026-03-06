# SubmissionLogURLResponse.Data

**Framework**: Notary API  
**Kind**: dictionary

Data that indicates how to get the log information for a particular submission.

**Availability**:
- Notary API 2.0.0+

## Declaration

```swift
object SubmissionLogURLResponse.Data
```

## Topics

### Objects
- [object SubmissionLogURLResponse.Data.Attributes](submissionlogurlresponse/data-data.dictionary/attributes-data.dictionary.md)
  Information about the log associated with the submission.

## Properties

- `attributes` (SubmissionLogURLResponse.Data.Attributes): Information about the log associated with the submission.
- `id` (string): The unique identifier for this submission. This value matches the value that you provided as a path parameter to the [`Get Submission Log`](get-submission-log.md) call that elicited this response.
- `type` (string): The resource type.

## See Also

- [object SubmissionLogURLResponse.Meta](submissionlogurlresponse/meta-data.dictionary.md)
  An empty object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notaryapi/submissionlogurlresponse/data-data.dictionary)*