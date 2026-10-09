# AppAssetLibraryPlacement.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary

Attributes that describe an app asset library placement resource.

**Availability**:
- App Store Connect API 4.5+

## Declaration

```swift
object AppAssetLibraryPlacement.Attributes
```

## Properties

- `mediaType` (AppAssetLibraryMediaType): The kind of asset the placement positions, either an image or a video.
- `placementType` (AppAssetLibraryPlacementType): The App Store location where the placement positions the asset.
- `placementGroup` (string): The identifier that groups related placements, such as the screenshots for a single device.
- `createdDate` (date-time): The date and time when App Store Connect created the resource.
- `lastModifiedDate` (date-time): The date and time when App Store Connect last modified the resource.
- `state` (AppAssetLibraryPlacementState): The current state of the resource in App Store Connect.
- `stateDetails` ([StateDetail]): Additional details about the current state, such as validation errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appassetlibraryplacement/attributes-data.dictionary)*