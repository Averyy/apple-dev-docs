# ReviewSubmission

**Framework**: App Store Connect API  
**Kind**: dictionary

A formal submission to App Store review grouping one or more items — app versions, in-app purchases, or events — for simultaneous review.

**Availability**:
- App Store Connect API 1.7+

## Declaration

```swift
object ReviewSubmission
```

## Topics

### Objects
- [object ReviewSubmission.Attributes](reviewsubmission/attributes-data.dictionary.md)
  Attributes that describe a review submission resource.
- [object ReviewSubmission.Relationships](reviewsubmission/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `attributes` (ReviewSubmission.Attributes)
- `id` (string) *(required)*
- `links` (ResourceLinks)
- `relationships` (ReviewSubmission.Relationships)
- `type` (string) *(required)*

## See Also

- [object ReviewSubmissionItem](reviewsubmissionitem.md)
  An individual reviewable item — such as an app version, in-app purchase, or App Clip — included in a review submission.
- [object ReviewSubmissionUpdateRequest](reviewsubmissionupdaterequest.md)
  The request body you use to update a review submission update request.
- [object ReviewSubmissionCreateRequest](reviewsubmissioncreaterequest.md)
  The request body for creating a review submission for an App Store version or associated items.
- [object ReviewSubmissionResponse](reviewsubmissionresponse.md)
  The response body for endpoints that create, read, or modify a single review submission.
- [object ReviewSubmissionsResponse](reviewsubmissionsresponse.md)
  The response body for endpoints that list review submissions for an app.
- [object AppReviewSubmissionsLinkagesResponse](appreviewsubmissionslinkagesresponse.md)
  A response containing the resource identifiers of review submissions associated with an app.
- [object ReviewSubmissionItemsLinkagesResponse](reviewsubmissionitemslinkagesresponse.md)
  A response containing the resource identifiers of items included in a review submission.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/reviewsubmission)*