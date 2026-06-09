# ReviewSubmissionsResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that list review submissions for an app.

**Availability**:
- App Store Connect API 1.7+

## Declaration

```swift
object ReviewSubmissionsResponse
```

## Properties

- `data` ([ReviewSubmission]) *(required)*
- `included` ([*])
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

- [object ReviewSubmission](reviewsubmission.md)
  A formal submission to App Store review grouping one or more items — app versions, in-app purchases, or events — for simultaneous review.
- [object ReviewSubmissionItem](reviewsubmissionitem.md)
  An individual reviewable item — such as an app version, in-app purchase, or App Clip — included in a review submission.
- [object ReviewSubmissionUpdateRequest](reviewsubmissionupdaterequest.md)
  The request body you use to update a review submission update request.
- [object ReviewSubmissionCreateRequest](reviewsubmissioncreaterequest.md)
  The request body for creating a review submission for an App Store version or associated items.
- [object ReviewSubmissionResponse](reviewsubmissionresponse.md)
  The response body for endpoints that create, read, or modify a single review submission.
- [object AppReviewSubmissionsLinkagesResponse](appreviewsubmissionslinkagesresponse.md)
  A response containing the resource identifiers of review submissions associated with an app.
- [object ReviewSubmissionItemsLinkagesResponse](reviewsubmissionitemslinkagesresponse.md)
  A response containing the resource identifiers of items included in a review submission.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/reviewsubmissionsresponse)*