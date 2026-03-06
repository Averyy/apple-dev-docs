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

**Request**:

```https
https://appstoreconnect.apple.com/notary/v2/submissions/2EFE2717-52EF-43A5-96DC-0797E4CA1041/logs
```

**Response**:

```json
{
  "data": {
    "attributes": {
      "developerLogUrl": "https://..."
    },
    "id": "2efe2717-52ef-43a5-96dc-0797e4ca1041",
    "type": "submissionsLog"
  },
  "meta": {
  }
} 

```

## Endpoint

`GET https://appstoreconnect.apple.com/notary/v2/submissions/{submissionId}/logs`

## Parameters

- `submissionId` (string) *(required)*: The identifier that you receive from the notary service when you post to [`Submit Software`](submit-software.md) to start a new submission.

## See Also

- [Get Submission Status](get-submission-status.md)
  Fetch the status of a software notarization submission.
- [object SubmissionResponse](submissionresponse.md)
  The notary service’s response to a request for the status of a submission.
- [object SubmissionLogURLResponse](submissionlogurlresponse.md)
  The notary service’s response to a request for the log information about a completed submission.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notaryapi/get-submission-log)*