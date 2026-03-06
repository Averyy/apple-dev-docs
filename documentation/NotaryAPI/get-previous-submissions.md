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

**Request**:

```https
https://appstoreconnect.apple.com/notary/v2/submissions
```

**Response**:

```json
{
  "data": [
    {
      "attributes": {
        "createdDate": "2021-04-29T01:38:09.498Z",
        "name": "OvernightTextEditor_11.6.8.zip",
        "status": "Accepted"
      },
      "id": "2efe2717-52ef-43a5-96dc-0797e4ca1041",
      "type": "submissions"
    },
    {
      "attributes": {
        "createdDate": "2021-04-23T17:44:54.761Z",
        "name": "OvernightTextEditor_11.6.7.zip",
        "status": "Accepted"
      },
      "id": "cf0c235a-dad2-4c24-96eb-c876d4cb3a2d",
      "type": "submissions"
    },
    {
      "attributes": {
        "createdDate": "2021-04-19T16:56:17.839Z",
        "name": "OvernightTextEditor_11.6.7.zip",
        "status": "Invalid"
      },
      "id": "38ce81cc-0bf7-454b-91ef-3f7395bf297b",
      "type": "submissions"
    }
  ],
  "meta": {
  }
} 
```

## Endpoint

`GET https://appstoreconnect.apple.com/notary/v2/submissions`

## See Also

- [object SubmissionListResponse](submissionlistresponse.md)
  The notary service’s response to a request for information about your team’s previous submissions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notaryapi/get-previous-submissions)*