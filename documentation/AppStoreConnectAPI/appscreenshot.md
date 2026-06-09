# AppScreenshot

**Framework**: App Store Connect API  
**Kind**: dictionary

The data structure that represent an App Screenshots resource.

**Availability**:
- App Store Connect API 1.2+

## Declaration

```swift
object AppScreenshot
```

## Topics

### Objects
- [object AppScreenshot.Attributes](appscreenshot/attributes-data.dictionary.md)
  Attributes that describe an App Screenshots resource.
- [object AppScreenshot.Relationships](appscreenshot/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `attributes` (AppScreenshot.Attributes)
- `id` (string) *(required)*
- `links` (ResourceLinks)
- `relationships` (AppScreenshot.Relationships)
- `type` (string) *(required)*

## See Also

- [object AppScreenshotCreateRequest](appscreenshotcreaterequest.md)
  The request body you use to create an App Screenshot.
- [object AppScreenshotUpdateRequest](appscreenshotupdaterequest.md)
  The request body you use to update an App Screenshot.
- [object AppScreenshotResponse](appscreenshotresponse.md)
  The response body for endpoints that create, read, or modify an app screenshot.
- [object AppScreenshotsResponse](appscreenshotsresponse.md)
  The response body for endpoints that list screenshots in an app screenshot set.
- [object UploadOperation](uploadoperation.md)
  Upload instructions for assets such as app previews and app screenshots.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appscreenshot)*