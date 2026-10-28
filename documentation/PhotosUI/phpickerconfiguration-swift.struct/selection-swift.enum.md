# PHPickerConfiguration.Selection

**Framework**: PhotosUI  
**Kind**: enum  
**Role**: Enumeration

Options that represent differing selection behavior.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 13.0+
- visionOS

## Declaration

```swift
enum Selection
```

## Overview

This enumeration defines the possible values of the photo picker configuration ([`PHPickerConfiguration`](../phpickerconfiguration-swift.struct.md)) property [`selection`](./selection-swift.property.md).

## Topics

### Selection methods
- [PHPickerConfiguration.Selection.default](./selection-swift.enum/default.md)
  An option that provides selected photos to the app in the default order after the user confirms the selection.
- [PHPickerConfiguration.Selection.ordered](./selection-swift.enum/ordered.md)
  An option that provides selected photos to the app in the chosen order after the user confirms the selection.
- [PHPickerConfiguration.Selection.continuous](./selection-swift.enum/continuous.md)
  An option that provides the app a person’s selection immediately.
- [PHPickerConfiguration.Selection.continuousAndOrdered](./selection-swift.enum/continuousandordered.md)
  An option that provides the app a person’s selection immediately and displays selected photos with a numbered badge.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Setting the selection limit
- [var selectionLimit: Int](./selectionlimit.md)
  The maximum number of selections the user can make.
- [var selection: PHPickerConfiguration.Selection](./selection-swift.property.md)
  The selection behavior for the picker.
- [enum PHPickerConfigurationSelection](../phpickerconfigurationselection.md)
  Options that represent differing selection behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phpickerconfiguration-swift.struct/selection-swift.enum)*