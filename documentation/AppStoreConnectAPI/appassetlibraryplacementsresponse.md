# AppAssetLibraryPlacementsResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that list app asset library placements.

**Availability**:
- App Store Connect API 4.5+

## Declaration

```swift
object AppAssetLibraryPlacementsResponse
```

## Properties

- `data` ([AppAssetLibraryPlacement]) *(required)*
- `included` ([*])
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

- [object AppAssetLibraryPlacement](appassetlibraryplacement.md)
  A placement that positions a library asset on a specific App Store surface.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appassetlibraryplacementsresponse)*