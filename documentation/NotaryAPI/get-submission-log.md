# Get Submission Log

**Framework**: Notary API  
**Kind**: httpRequest

Fetch details about a single completed notarization.

**Availability**:
- Notary API 2.0.0+

## Mentions

- [Submitting software for notarization over the web](submitting-software-for-notarization-over-the-web.md)

#### Discussion

Use this endpoint to get a URL that you can download a log file from that enumerates any issues found by the notary service. The URL that you receive is temporary, so be sure to use it to immediately fetch the log. If you need the log again in the future, ask for the URL again.

The log file that you download contains JSON-formatted data, and might include both errors and warnings. For information about how to deal with common notarization problems, see [`Resolving common notarization issues`](https://developer.apple.com/documentation/Security/resolving-common-notarization-issues).

##### Example

## See Also

- [Get Submission Status](get-submission-status.md)
  Fetch the status of a software notarization submission.
- [object SubmissionResponse](submissionresponse.md)
  The notary service’s response to a request for the status of a submission.
- [object SubmissionLogURLResponse](submissionlogurlresponse.md)
  The notary service’s response to a request for the log information about a completed submission.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notaryapi/get-submission-log)*