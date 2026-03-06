# SubmissionLogURLResponse.Data.Attributes

**Framework**: Notary API  
**Kind**: dictionary

Information about the log associated with the submission.

**Availability**:
- Notary API 2.0.0+

## Declaration

```swift
object SubmissionLogURLResponse.Data.Attributes
```

## Properties

- `developerLogUrl` (string): The URL that you use to download the logs for a submission. The URL serves a JSON-encoded file that contains the log information. The URL is valid for only a few hours. If you need the log again later, ask for the URL again by making another call to the [`Get Submission Log`](get-submission-log.md) endpoint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notaryapi/submissionlogurlresponse/data-data.dictionary/attributes-data.dictionary)*