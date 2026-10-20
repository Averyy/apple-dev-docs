# AppEventScreenshotCreateRequest.Data

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The request body you use to create an app event screenshot.

**Availability**:
- App Store Connect API 1.7+ - Deprecated in 4.5

> **Deprecated**: This object is deprecated. Use [`AppAssetLibraryImageCreateRequest`](../appassetlibraryimagecreaterequest.md) instead.

## Declaration

```
object AppEventScreenshotCreateRequest.Data
```

## Topics

### Objects
- [object AppEventScreenshotCreateRequest.Data.Attributes](./data-data.dictionary/attributes-data.dictionary.md)
  Attributes that describe an app event screenshot create request resource.
- [object AppEventScreenshotCreateRequest.Data.Relationships](./data-data.dictionary/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `attributes` (AppEventScreenshotCreateRequest.Data.Attributes) *(required)*
- `relationships` (AppEventScreenshotCreateRequest.Data.Relationships) *(required)*
- `type` (string) *(required)*: **Allowed Values**: `appEventScreenshots`


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appeventscreenshotcreaterequest/data-data.dictionary)*