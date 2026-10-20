# AppAssetLibraryImageCreateRequest.Data.Relationships

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The relationships you include in the request and those on which you can operate.

**Availability**:
- App Store Connect API 4.5+

## Declaration

```
object AppAssetLibraryImageCreateRequest.Data.Relationships
```

## Topics

### Objects
- [object AppAssetLibraryImageCreateRequest.Data.Relationships.AssetLibrary](./relationships-data.dictionary/assetlibrary-data.dictionary.md)
  The asset library to associate with the new app asset library image.
- [object AppAssetLibraryImageCreateRequest.Data.Relationships.Placements](./relationships-data.dictionary/placements-data.dictionary.md)
  The placements to associate with the new app asset library image.

## Properties

- `assetLibrary` (AppAssetLibraryImageCreateRequest.Data.Relationships.AssetLibrary) *(required)*: The asset library that contains the asset.
- `placements` (AppAssetLibraryImageCreateRequest.Data.Relationships.Placements): The placements that position this asset across your App Store content.

## See Also

### Objects
- [object AppAssetLibraryImageCreateRequest.Data.Attributes](./attributes-data.dictionary.md)
  The attributes you set that describe the new app asset library image resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appassetlibraryimagecreaterequest/data-data.dictionary/relationships-data.dictionary)*