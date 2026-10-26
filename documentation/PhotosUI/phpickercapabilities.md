# PHPickerCapabilities

**Framework**: PhotosUI  
**Kind**: struct  
**Role**: Structure

Options that customize the look and behavior of the photos picker.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
struct PHPickerCapabilities
```

```c
enum PHPickerCapabilities : NSUInteger;
```

#### Overview

This enumeration defines the possible values for the photo picker configuration ([`PHPickerConfiguration`](./phpickerconfiguration-swift.struct.md)) property [`disabledCapabilities`](./phpickerconfiguration-swift.struct/disabledcapabilities.md).

## Topics

### Specifying features
- [static var collectionNavigation: PHPickerCapabilities](./phpickercapabilities/collectionnavigation.md)
  A capability that corresponds to a sidebar or the Albums tab.
- [static var selectionActions: PHPickerCapabilities](./phpickercapabilities/selectionactions.md)
  A cabability that represents the Cancel and Add buttons.
- [static var search: PHPickerCapabilities](./phpickercapabilities/search.md)
  A capability that corresponds to the search bar.
- [static var sensitivityAnalysisIntervention: PHPickerCapabilities](./phpickercapabilities/sensitivityanalysisintervention.md)
  A capability that prompts for confirmation if a person selects a photo that contains nudity.
- [static var stagingArea: PHPickerCapabilities](./phpickercapabilities/stagingarea.md)
  A capability that corresponds to an area in which the selected photos display.
### Creating a capability
- [init(rawValue: UInt)](./phpickercapabilities/init%28rawvalue%29.md)
  Creates a photo picker capability.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phpickercapabilities)*