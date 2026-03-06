# NewSubmissionResponse.Data

**Framework**: Notary API  
**Kind**: dictionary

Information that the notary service provides for uploading your software for notarization and tracking the submission.

**Availability**:
- Notary API 2.0.0+

## Declaration

```swift
object NewSubmissionResponse.Data
```

## Topics

### Objects
- [object NewSubmissionResponse.Data.Attributes](newsubmissionresponse/data-data.dictionary/attributes-data.dictionary.md)
  Information that you use to upload your software for notarization.

## Properties

- `attributes` (NewSubmissionResponse.Data.Attributes): Information that you use to upload your software to Amazon S3.
- `id` (string): A unique identifier for this submission. Use this value to track the status of your submission. For example, you use it as the `submissionID` parameter in the [`Get Submission Status`](get-submission-status.md) call, or to match against the `id` field in the response from the [`Get Previous Submissions`](get-previous-submissions.md) call.
- `type` (string): The resource type.

## See Also

- [object NewSubmissionResponse.Meta](newsubmissionresponse/meta-data.dictionary.md)
  An empty object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notaryapi/newsubmissionresponse/data-data.dictionary)*