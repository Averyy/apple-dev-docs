# SubmissionListResponse

**Framework**: Notary API  
**Kind**: dictionary

The notary service’s response to a request for information about your team’s previous submissions.

**Availability**:
- Notary API 2.0.0+

## Declaration

```swift
object SubmissionListResponse
```

#### Discussion

You receive a structure of this type in response to a call to the [`Get Previous Submissions`](get-previous-submissions.md) endpoint. The list includes only the 100 most recent submissions.

## Topics

### Objects
- [object SubmissionListResponse.Data](submissionlistresponse/data-data.dictionary.md)
  Data that describes one of your team’s previous submissions.
- [object SubmissionListResponse.Meta](submissionlistresponse/meta-data.dictionary.md)
  An empty object.

## See Also

- [Get Previous Submissions](get-previous-submissions.md)
  Fetch a list of your team’s previous notarization submissions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notaryapi/submissionlistresponse)*