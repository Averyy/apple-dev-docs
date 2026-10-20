# AppScreenshotUpdateRequest.Data

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The data element of the request body.

**Availability**:
- App Store Connect API 1.2+ - Deprecated in 4.5

> **Deprecated**: This object is deprecated. Use [`AppAssetLibraryImageUpdateRequest`](../appassetlibraryimageupdaterequest.md) instead.

## Declaration

```
object AppScreenshotUpdateRequest.Data
```

## Topics

### Objects
- [object AppScreenshotUpdateRequest.Data.Attributes](./data-data.dictionary/attributes-data.dictionary.md)
  Attributes whose values you’re changing as part of the update request.

## Properties

- `attributes` (AppScreenshotUpdateRequest.Data.Attributes)
- `id` (string) *(required)*
- `type` (string) *(required)*: **Allowed Values**: `appScreenshots`


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appscreenshotupdaterequest/data-data.dictionary)*