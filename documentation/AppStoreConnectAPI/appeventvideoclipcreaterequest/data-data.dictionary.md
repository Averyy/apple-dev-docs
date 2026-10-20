# AppEventVideoClipCreateRequest.Data

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The request body you use to create an app event video clip.

**Availability**:
- App Store Connect API 1.7+ - Deprecated in 4.5

> **Deprecated**: This object is deprecated. Use [`AppAssetLibraryVideoCreateRequest`](../appassetlibraryvideocreaterequest.md) instead.

## Declaration

```
object AppEventVideoClipCreateRequest.Data
```

## Topics

### Objects
- [object AppEventVideoClipCreateRequest.Data.Attributes](./data-data.dictionary/attributes-data.dictionary.md)
  Attributes that describe an app event video clip create request resource.
- [object AppEventVideoClipCreateRequest.Data.Relationships](./data-data.dictionary/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `attributes` (AppEventVideoClipCreateRequest.Data.Attributes) *(required)*
- `relationships` (AppEventVideoClipCreateRequest.Data.Relationships) *(required)*
- `type` (string) *(required)*: **Allowed Values**: `appEventVideoClips`


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appeventvideoclipcreaterequest/data-data.dictionary)*