# PHPickerConfigurationSelection

**Framework**: PhotosUI  
**Kind**: enum  
**Role**: Enumeration

Options that represent differing selection behavior.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
enum PHPickerConfigurationSelection
```

```c
enum PHPickerConfigurationSelection : NSInteger;
```

#### Overview

This enumeration defines the possible values of the photo picker configuration ([`PHPickerConfiguration`](./phpickerconfiguration-swift.struct.md)) property [`selection`](./phpickerconfiguration-swift.struct/selection-swift.property.md).

## Topics

### Selection methods
- [PHPickerConfigurationSelection.default](./phpickerconfigurationselection/default.md)
  An option that provides selected photos to the app in the default order after the user confirms the selection.
- [PHPickerConfigurationSelection.ordered](./phpickerconfigurationselection/ordered.md)
  An option that provides selected photos to the app in the chosen order after the user confirms the selection.
- [PHPickerConfigurationSelection.continuous](./phpickerconfigurationselection/continuous.md)
  An option that provides the app a person’s selection immediately.
- [PHPickerConfigurationSelection.continuousAndOrdered](./phpickerconfigurationselection/continuousandordered.md)
  An option that provides the app a person’s selection immediately and displays selected photos with a numbered badge.
### Initializers
- [init?(rawValue: Int)](./phpickerconfigurationselection/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Setting the selection limit
- [selectionLimit](./phpickerconfiguration-c.class/selectionlimit.md)
  The maximum number of selections the user can make.
- [selection](./phpickerconfiguration-c.class/selection.md)
  The selection behavior for the picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phpickerconfigurationselection)*