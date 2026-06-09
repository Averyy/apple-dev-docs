# AppEventScreenshotsResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that list screenshots for an in-app event localization.

**Availability**:
- App Store Connect API 1.7+

## Declaration

```swift
object AppEventScreenshotsResponse
```

## Properties

- `data` ([AppEventScreenshot]) *(required)*
- `included` ([AppEventLocalization])
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

- [object AppEventScreenshot](appeventscreenshot.md)
  A screenshot image used to promote an app event on the App Store product page.
- [object AppEventScreenshotCreateRequest](appeventscreenshotcreaterequest.md)
  The request body you use to create an app event screenshot.
- [object AppEventScreenshotResponse](appeventscreenshotresponse.md)
  The response body for endpoints that create, read, or modify an in-app event screenshot.
- [object AppEventScreenshotUpdateRequest](appeventscreenshotupdaterequest.md)
  The request body you use to update an app event screenshot update request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appeventscreenshotsresponse)*