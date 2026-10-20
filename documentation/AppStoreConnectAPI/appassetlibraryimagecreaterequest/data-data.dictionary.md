# AppAssetLibraryImageCreateRequest.Data

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The request body you use to create an app asset library image.

**Availability**:
- App Store Connect API 4.5+

## Declaration

```
object AppAssetLibraryImageCreateRequest.Data
```

## Topics

### Objects
- [object AppAssetLibraryImageCreateRequest.Data.Attributes](./data-data.dictionary/attributes-data.dictionary.md)
  The attributes you set that describe the new app asset library image resource.
- [object AppAssetLibraryImageCreateRequest.Data.Relationships](./data-data.dictionary/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `type` (string) *(required)*: **Allowed Values**: `appAssetLibraryImages`
- `attributes` (AppAssetLibraryImageCreateRequest.Data.Attributes) *(required)*
- `relationships` (AppAssetLibraryImageCreateRequest.Data.Relationships) *(required)*


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appassetlibraryimagecreaterequest/data-data.dictionary)*