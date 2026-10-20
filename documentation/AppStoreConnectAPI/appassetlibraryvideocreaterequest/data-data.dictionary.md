# AppAssetLibraryVideoCreateRequest.Data

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The request body you use to create an app asset library video.

**Availability**:
- App Store Connect API 4.5+

## Declaration

```
object AppAssetLibraryVideoCreateRequest.Data
```

## Topics

### Objects
- [object AppAssetLibraryVideoCreateRequest.Data.Attributes](./data-data.dictionary/attributes-data.dictionary.md)
  The attributes you set that describe the new app asset library video resource.
- [object AppAssetLibraryVideoCreateRequest.Data.Relationships](./data-data.dictionary/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `type` (string) *(required)*: **Allowed Values**: `appAssetLibraryVideos`
- `attributes` (AppAssetLibraryVideoCreateRequest.Data.Attributes) *(required)*
- `relationships` (AppAssetLibraryVideoCreateRequest.Data.Relationships) *(required)*


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appassetlibraryvideocreaterequest/data-data.dictionary)*