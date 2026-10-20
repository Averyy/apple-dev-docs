# AppAssetLibraryPlacementOrderingRequestCreateRequest.Data.Relationships

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The relationships you include in the request and those on which you can operate.

**Availability**:
- App Store Connect API 4.5+

## Declaration

```
object AppAssetLibraryPlacementOrderingRequestCreateRequest.Data.Relationships
```

## Topics

### Objects
- [object AppAssetLibraryPlacementOrderingRequestCreateRequest.Data.Relationships.OrderedPlacements](./relationships-data.dictionary/orderedplacements-data.dictionary.md)
  The placements to order, listed in the sequence you want them to display.
- [object AppAssetLibraryPlacementOrderingRequestCreateRequest.Data.Relationships.AppStoreVersionLocalization](./relationships-data.dictionary/appstoreversionlocalization-data.dictionary.md)
  The App Store version localization to associate with the new app asset library placement ordering request.
- [object AppAssetLibraryPlacementOrderingRequestCreateRequest.Data.Relationships.AppCustomProductPageLocalization](./relationships-data.dictionary/appcustomproductpagelocalization-data.dictionary.md)
  The custom product page localization to associate with the new app asset library placement ordering request.
- [object AppAssetLibraryPlacementOrderingRequestCreateRequest.Data.Relationships.AppStoreVersionExperimentTreatmentLocalization](./relationships-data.dictionary/appstoreversionexperimenttreatmentlocalization-data.dictionary.md)
  The App Store version experiment treatment localization to associate with the new app asset library placement ordering request.

## Properties

- `orderedPlacements` (AppAssetLibraryPlacementOrderingRequestCreateRequest.Data.Relationships.OrderedPlacements): The placements to reorder, listed in their new sequence.
- `appStoreVersionLocalization` (AppAssetLibraryPlacementOrderingRequestCreateRequest.Data.Relationships.AppStoreVersionLocalization): The App Store version localization where the placement positions the asset.
- `appCustomProductPageLocalization` (AppAssetLibraryPlacementOrderingRequestCreateRequest.Data.Relationships.AppCustomProductPageLocalization): The custom product page localization where the placement positions the asset.
- `appStoreVersionExperimentTreatmentLocalization` (AppAssetLibraryPlacementOrderingRequestCreateRequest.Data.Relationships.AppStoreVersionExperimentTreatmentLocalization): The product page optimization treatment localization where the placement positions the asset.

## See Also

### Objects
- [object AppAssetLibraryPlacementOrderingRequestCreateRequest.Data.Attributes](./attributes-data.dictionary.md)
  The attributes you set that describe the new app asset library placement ordering request resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appassetlibraryplacementorderingrequestcreaterequest/data-data.dictionary/relationships-data.dictionary)*