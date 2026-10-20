# SubmissionResponse.Data

**Framework**: Notary API  
**Kind**: dictionary  
**Role**: Object

Information that the service provides about the status of a notarization submission.

**Availability**:
- Notary API 2.0.0+

## Declaration

```
object SubmissionResponse.Data
```

## Topics

### Objects
- [object SubmissionResponse.Data.Attributes](./data-data.dictionary/attributes-data.dictionary.md)
  Information about the status of a submission.

## Properties

- `attributes` (SubmissionResponse.Data.Attributes): Information about the status of a submission.
- `id` (string): The unique identifier for this submission. This value matches the value that you provided as a path parameter to the [`Get Submission Status`](../get-submission-status.md) call that elicited this response.
- `type` (string): The resource type.

## See Also

### Objects
- [object SubmissionResponse.Meta](./meta-data.dictionary.md)
  An empty object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notaryapi/submissionresponse/data-data.dictionary)*