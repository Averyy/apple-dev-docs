# AppScreenshotCreateRequest.Data

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The data element of the request body.

**Availability**:
- App Store Connect API 1.2+ - Deprecated in 4.5

> **Deprecated**: This object is deprecated. Use [`AppAssetLibraryImageCreateRequest`](../appassetlibraryimagecreaterequest.md) instead.

## Declaration

```
object AppScreenshotCreateRequest.Data
```

## Topics

### Objects
- [object AppScreenshotCreateRequest.Data.Attributes](./data-data.dictionary/attributes-data.dictionary.md)
  Attributes that you set that describe the new resource.
- [object AppScreenshotCreateRequest.Data.Relationships](./data-data.dictionary/relationships-data.dictionary.md)
  The relationships to other resources that you can set with this request.

## Properties

- `attributes` (AppScreenshotCreateRequest.Data.Attributes) *(required)*
- `relationships` (AppScreenshotCreateRequest.Data.Relationships) *(required)*
- `type` (string) *(required)*: **Allowed Values**: `appScreenshots`


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appscreenshotcreaterequest/data-data.dictionary)*