# AppClipAppStoreReviewDetailResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response containing the App Store review details for a single App Clip.

**Availability**:
- App Store Connect API 1.6+

## Declaration

```swift
object AppClipAppStoreReviewDetailResponse
```

## Properties

- `data` (AppClipAppStoreReviewDetail) *(required)*: The resource data.
- `included` ([AppClipDefaultExperience]): The requested relationship data.
- `links` (DocumentLinks) *(required)*: Navigational links that include the self-link.

## See Also

- [object AppClipAppStoreReviewDetail](appclipappstorereviewdetail.md)
  The review submission details for an App Clip, including the invocation URLs required for App Store review.
- [object AppClipAppStoreReviewDetailCreateRequest](appclipappstorereviewdetailcreaterequest.md)
  The request body you use to create an App Clip App Store Review Detail.
- [object AppClipAppStoreReviewDetailUpdateRequest](appclipappstorereviewdetailupdaterequest.md)
  The request body you use to update App Clip information that you provide to App Store Review.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appclipappstorereviewdetailresponse)*