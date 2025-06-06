# Get Previous Submissions

**Framework**: Notary API  
**Kind**: httpRequest

Fetch a list of your team’s previous notarization submissions.

**Availability**:
- Notary API 2.0.0+

## Mentions

- [Submitting software for notarization over the web](submitting-software-for-notarization-over-the-web.md)

#### Discussion

Use this endpoint to get the list of submissions associated with your team. The response holds an array of values that include the unique identifier for the submission, the date you initiated the submission, the name of the associated software, and the status of the submission. The response returns information about only the 100 most recent submissions.

If you need information about just one submission, and you have the associated identifier, use [`Get Submission Status`](get-submission-status.md) instead.

##### Example

## See Also

- [object SubmissionListResponse](submissionlistresponse.md)
  The notary service’s response to a request for information about your team’s previous submissions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notaryapi/get-previous-submissions)*