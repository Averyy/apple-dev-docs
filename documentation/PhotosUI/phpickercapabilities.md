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
- [PHPickerCapabilitiesNone](./phpickercapabilities/phpickercapabilitiesnone.md)
  An option that represents no capabilities.
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

## See Also

### Customizing picker appearance and behavior
- [mode](./phpickerconfiguration-c.class/mode.md)
  A layout type for the photos in the picker’s view.
- [PHPickerMode](./phpickermode-c.enum.md)
  Layout options that determine how the picker orders photos visually.
- [disabledCapabilities](./phpickerconfiguration-c.class/disabledcapabilities.md)
  The aspects of a photo picker’s default appearance that your app can disable.
- [edgesWithoutContentMargins](./phpickerconfiguration-c.class/edgeswithoutcontentmargins.md)
  The portions of a photo picker’s perimeter that are borderless.
- [PHPickerUpdateConfiguration](./phpickerupdateconfiguration.md)
  An object that defines the aspects of a photo picker’s appearance that can change while it’s presented.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phpickercapabilities)*