# AppAssetLibraryPlacement

**Framework**: App Store Connect API  
**Kind**: dictionary

A placement that positions a library asset on a specific App Store surface.

**Availability**:
- App Store Connect API 4.5+

## Declaration

```swift
object AppAssetLibraryPlacement
```

## Topics

### Objects
- [object AppAssetLibraryPlacement.Attributes](appassetlibraryplacement/attributes-data.dictionary.md)
  Attributes that describe an app asset library placement resource.

## Properties

- `type` (string) *(required)*
- `id` (string) *(required)*
- `attributes` (AppAssetLibraryPlacement.Attributes)
- `relationships` (*)
- `links` (ResourceLinks)

## See Also

- [object AppAssetLibraryPlacementCommonAttributes](appassetlibraryplacementcommonattributes.md)
  The attributes common to an app asset library placement of any media type.
- [object AppAssetLibraryPlacementCommonRelationships](appassetlibraryplacementcommonrelationships.md)
  The relationships shared by every app asset library placement to its target localizations.
- [object AppAssetLibraryPlacementImageRelationships](appassetlibraryplacementimagerelationships.md)
  The relationships specific to an image placement, including its image asset.
- [object AppAssetLibraryPlacementVideoRelationships](appassetlibraryplacementvideorelationships.md)
  The relationships specific to a video placement, including its video asset.
- [object AppAssetLibraryPlacementVideoAttributes](appassetlibraryplacementvideoattributes.md)
  The attributes specific to a video placement, such as its preview-frame settings.
- [object AppAssetLibraryPlacementCreateRequest](appassetlibraryplacementcreaterequest.md)
  The request body you use to create an app asset library placement.
- [object AppAssetLibraryPlacementResponse](appassetlibraryplacementresponse.md)
  The response body for endpoints that create, read, or modify an app asset library placement.
- [object AppAssetLibraryPlacementsResponse](appassetlibraryplacementsresponse.md)
  The response body for endpoints that list app asset library placements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appassetlibraryplacement)*