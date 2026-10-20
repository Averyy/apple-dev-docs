# AppPreviewCreateRequest.Data

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The data element of the request body.

**Availability**:
- App Store Connect API 1.2+ - Deprecated in 4.5

> **Deprecated**: This object is deprecated. Use [`AppAssetLibraryVideoCreateRequest`](../appassetlibraryvideocreaterequest.md) instead.

## Declaration

```
object AppPreviewCreateRequest.Data
```

## Topics

### Objects
- [object AppPreviewCreateRequest.Data.Attributes](./data-data.dictionary/attributes-data.dictionary.md)
  Attributes that you set that describe the new resource.
- [object AppPreviewCreateRequest.Data.Relationships](./data-data.dictionary/relationships-data.dictionary.md)
  The relationships to other resources that you can set with this request.

## Properties

- `attributes` (AppPreviewCreateRequest.Data.Attributes) *(required)*
- `relationships` (AppPreviewCreateRequest.Data.Relationships) *(required)*
- `type` (string) *(required)*: **Allowed Values**: `appPreviews`


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/apppreviewcreaterequest/data-data.dictionary)*