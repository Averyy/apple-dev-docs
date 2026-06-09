# AppScreenshotsResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that list screenshots in an app screenshot set.

**Availability**:
- App Store Connect API 1.2+

## Declaration

```swift
object AppScreenshotsResponse
```

## Properties

- `data` ([AppScreenshot]) *(required)*
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)
- `included` ([AppScreenshotSet])

## See Also

- [object AppScreenshot](appscreenshot.md)
  The data structure that represent an App Screenshots resource.
- [object AppScreenshotCreateRequest](appscreenshotcreaterequest.md)
  The request body you use to create an App Screenshot.
- [object AppScreenshotUpdateRequest](appscreenshotupdaterequest.md)
  The request body you use to update an App Screenshot.
- [object AppScreenshotResponse](appscreenshotresponse.md)
  The response body for endpoints that create, read, or modify an app screenshot.
- [object UploadOperation](uploadoperation.md)
  Upload instructions for assets such as app previews and app screenshots.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appscreenshotsresponse)*