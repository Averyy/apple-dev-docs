# sensitivityAnalysisIntervention

**Framework**: PhotosUI  
**Kind**: property  
**Role**: Type Property

A capability that prompts for confirmation if a person selects a photo that contains nudity.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
static var sensitivityAnalysisIntervention: PHPickerCapabilities { get }
```

```c
PHPickerCapabilitiesSensitivityAnalysisIntervention
```

## Discussion

When either the Sensitive Content Warning setting or Communication Safety parental control in Screen Time are active in iOS 17 or later, the photos picker checks whether a selected asset contains nudity. If so, the photo picker presents a model view that warns the person before giving the app access to the photo. The intervention UI requires a person to confirm that they really intend to interact with the sensitive asset in the photo library before proceeding. For more information on nudity detection in iOS 17 and later, see [Sensitive Content Analysis](../../SensitiveContentAnalysis/SensitiveContentAnalysis.md).

## See Also

### Specifying features
- [static var collectionNavigation: PHPickerCapabilities](./collectionnavigation.md)
  A capability that corresponds to a sidebar or the Albums tab.
- [static var selectionActions: PHPickerCapabilities](./selectionactions.md)
  A cabability that represents the Cancel and Add buttons.
- [static var search: PHPickerCapabilities](./search.md)
  A capability that corresponds to the search bar.
- [static var stagingArea: PHPickerCapabilities](./stagingarea.md)
  A capability that corresponds to an area in which the selected photos display.
- [PHPickerCapabilitiesNone](./phpickercapabilitiesnone.md)
  An option that represents no capabilities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phpickercapabilities/sensitivityanalysisintervention)*