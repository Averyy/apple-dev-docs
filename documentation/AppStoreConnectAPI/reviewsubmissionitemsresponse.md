# ReviewSubmissionItemsResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that list items in a review submission.

**Availability**:
- App Store Connect API 1.7+

## Declaration

```swift
object ReviewSubmissionItemsResponse
```

## Properties

- `data` ([ReviewSubmissionItem]) *(required)*
- `included` ([*])
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

- [object ReviewSubmissionItemCreateRequest](reviewsubmissionitemcreaterequest.md)
  The request body you use to create a review submission item.
- [object ReviewSubmissionItemUpdateRequest](reviewsubmissionitemupdaterequest.md)
  The request body you use to update a review submission item update request.
- [object ReviewSubmissionItemResponse](reviewsubmissionitemresponse.md)
  The response body for endpoints that create, read, or modify a single review submission item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/reviewsubmissionitemsresponse)*