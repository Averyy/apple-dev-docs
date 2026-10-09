# AppAssetLibraryPlacementCommonRelationships

**Framework**: App Store Connect API  
**Kind**: dictionary

The relationships shared by every app asset library placement to its target localizations.

**Availability**:
- App Store Connect API 4.5+

## Declaration

```swift
object AppAssetLibraryPlacementCommonRelationships
```

## Topics

### Objects
- [object AppAssetLibraryPlacementCommonRelationships.AppEventLocalization](appassetlibraryplacementcommonrelationships/appeventlocalization-data.dictionary.md)
  The in-app event localization on which the app asset library placement appears.
- [object AppAssetLibraryPlacementCommonRelationships.AppStoreVersionLocalization](appassetlibraryplacementcommonrelationships/appstoreversionlocalization-data.dictionary.md)
  The App Store version localization on which the app asset library placement appears.
- [object AppAssetLibraryPlacementCommonRelationships.AppCustomProductPageLocalization](appassetlibraryplacementcommonrelationships/appcustomproductpagelocalization-data.dictionary.md)
  The custom product page localization on which the app asset library placement appears.
- [object AppAssetLibraryPlacementCommonRelationships.AppStoreVersionExperimentTreatmentLocalization](appassetlibraryplacementcommonrelationships/appstoreversionexperimenttreatmentlocalization-data.dictionary.md)
  The App Store version experiment treatment localization on which the app asset library placement appears.

## Properties

- `appEventLocalization` (AppAssetLibraryPlacementCommonRelationships.AppEventLocalization): The in-app event localization where the placement positions the asset.
- `appStoreVersionLocalization` (AppAssetLibraryPlacementCommonRelationships.AppStoreVersionLocalization): The App Store version localization where the placement positions the asset.
- `appCustomProductPageLocalization` (AppAssetLibraryPlacementCommonRelationships.AppCustomProductPageLocalization): The custom product page localization where the placement positions the asset.
- `appStoreVersionExperimentTreatmentLocalization` (AppAssetLibraryPlacementCommonRelationships.AppStoreVersionExperimentTreatmentLocalization): The product page optimization treatment localization where the placement positions the asset.

## Relationships

### Inherited By
- [AppAssetLibraryPlacementImageRelationships](appassetlibraryplacementimagerelationships.md)
- [AppAssetLibraryPlacementVideoRelationships](appassetlibraryplacementvideorelationships.md)

## See Also

- [object AppAssetLibraryPlacement](appassetlibraryplacement.md)
  A placement that positions a library asset on a specific App Store surface.
- [object AppAssetLibraryPlacementCommonAttributes](appassetlibraryplacementcommonattributes.md)
  The attributes common to an app asset library placement of any media type.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appassetlibraryplacementcommonrelationships)*