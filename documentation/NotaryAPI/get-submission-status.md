# Get Submission Status

**Framework**: Notary API  
**Kind**: httpRequest

Fetch the status of a software notarization submission.

**Availability**:
- Notary API 2.0.0+

## Mentions

- [Submitting software for notarization over the web](submitting-software-for-notarization-over-the-web.md)

#### Discussion

Use this endpoint to fetch the status of a submission request. Form the URL for the call using the identifier that you receive in the `id` field of the response to the [`Submit Software`](submit-software.md) endpoint. If you lose the identifier, you can get a list of the most recent 100 submissions by calling the [`Get Previous Submissions`](get-previous-submissions.md) endpoint.

Along with the status of the request, the response indicates the date that you initiated the request and the software name that you provided at that time.

##### Example

## See Also

- [object SubmissionResponse](submissionresponse.md)
  The notary service’s response to a request for the status of a submission.
- [Get Submission Log](get-submission-log.md)
  Fetch details about a single completed notarization.
- [object SubmissionLogURLResponse](submissionlogurlresponse.md)
  The notary service’s response to a request for the log information about a completed submission.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notaryapi/get-submission-status)*