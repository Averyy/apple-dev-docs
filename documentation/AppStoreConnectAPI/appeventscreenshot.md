# AppEventScreenshot

**Framework**: App Store Connect API  
**Kind**: dictionary

A screenshot image used to promote an app event on the App Store product page.

**Availability**:
- App Store Connect API 1.7+

## Declaration

```swift
object AppEventScreenshot
```

## Topics

### Objects
- [object AppEventScreenshot.Attributes](appeventscreenshot/attributes-data.dictionary.md)
  Attributes that describe an app event screenshot resource.
- [object AppEventScreenshot.Relationships](appeventscreenshot/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `attributes` (AppEventScreenshot.Attributes)
- `id` (string) *(required)*
- `links` (ResourceLinks)
- `relationships` (AppEventScreenshot.Relationships)
- `type` (string) *(required)*

## See Also

- [object AppEventScreenshotCreateRequest](appeventscreenshotcreaterequest.md)
  The request body you use to create an app event screenshot.
- [object AppEventScreenshotResponse](appeventscreenshotresponse.md)
  The response body for endpoints that create, read, or modify an in-app event screenshot.
- [object AppEventScreenshotUpdateRequest](appeventscreenshotupdaterequest.md)
  The request body you use to update an app event screenshot update request.
- [object AppEventScreenshotsResponse](appeventscreenshotsresponse.md)
  The response body for endpoints that list screenshots for an in-app event localization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appeventscreenshot)*