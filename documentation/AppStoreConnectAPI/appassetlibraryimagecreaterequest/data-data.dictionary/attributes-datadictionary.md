# AppAssetLibraryImageCreateRequest.Data.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary

The attributes you set that describe the new app asset library image resource.

**Availability**:
- App Store Connect API 4.5+

## Declaration

```swift
object AppAssetLibraryImageCreateRequest.Data.Attributes
```

## Properties

- `category` (AppAssetLibraryAssetCategory) *(required)*: The category that determines how you can use the asset across your App Store content.
- `fileName` (string) *(required)*: The name of the asset file you upload.
- `fileSize` (int64) *(required)*: The size, in bytes, of the asset file.
- `referenceName` (string): A name that identifies the asset within its asset library.

## See Also

- [object AppAssetLibraryImageCreateRequest.Data.Relationships](appassetlibraryimagecreaterequest/data-data.dictionary/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appassetlibraryimagecreaterequest/data-data.dictionary/attributes-data.dictionary)*