# SubmissionListResponse.Data

**Framework**: Notary API  
**Kind**: dictionary

Data that describes one of your team’s previous submissions.

**Availability**:
- Notary API 2.0.0+

## Declaration

```swift
object SubmissionListResponse.Data
```

## Topics

### Objects
- [object SubmissionListResponse.Data.Attributes](submissionlistresponse/data-data.dictionary/attributes-data.dictionary.md)
  Information about the status of a submission.

## Properties

- `attributes` (SubmissionListResponse.Data.Attributes): Information about a particular submission.
- `id` (string): The unique identifier for a submission. This value matches the value that you received in the `id` field that appeared in the response to the [`Submit Software`](submit-software.md) call that you used to start the submission.
- `type` (string): The resource type.

## See Also

- [object SubmissionListResponse.Meta](submissionlistresponse/meta-data.dictionary.md)
  An empty object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notaryapi/submissionlistresponse/data-data.dictionary)*