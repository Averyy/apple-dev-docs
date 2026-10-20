# AppStoreReviewDetailResponse

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The response body for endpoints that read or modify App Store review details for a version.

**Availability**:
- App Store Connect API 1.2+

## Declaration

```
object AppStoreReviewDetailResponse
```

## Properties

- `data` (AppStoreReviewDetail) *(required)*
- `included` ([*]): **Allowed Types**: `AppStoreReviewAttachment`, `AppStoreVersion`
- `links` (DocumentLinks) *(required)*

## See Also

### Objects
- [object AppStoreReviewDetail](./appstorereviewdetail.md)
  The data structure that represent an App Store Review Details  resource.
- [object AppStoreReviewDetailCreateRequest](./appstorereviewdetailcreaterequest.md)
  The request body you use to create an App Store Review Detail.
- [object AppStoreReviewDetailUpdateRequest](./appstorereviewdetailupdaterequest.md)
  The request body you use to update an App Store Review Detail.
- [object AppStoreReviewDetailAppStoreReviewAttachmentsLinkagesResponse](./appstorereviewdetailappstorereviewattachmentslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appstorereviewdetailresponse)*