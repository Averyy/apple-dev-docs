# checkmark(displayed:options:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates a checkmark system accessory with the specified display state and configuration options.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS

## Declaration

```swift
static func checkmark(displayed: UICellAccessory.DisplayedState = .always, options: UICellAccessory.CheckmarkOptions = CheckmarkOptions()) -> UICellAccessory
```

## Return Value

A configured checkmark cell accessory. This accessory is a checkmark with the default system green color. This accessory appears on the trailing edge of the cell.

## Parameters

- `displayed`: The cell-editing states that the checkmark appears in. This parameter has a default value of [`UICellAccessory.DisplayedState.always`](./displayedstate/always.md).
- `options`: Configuration options for the checkmark. See [`UICellAccessory.CheckmarkOptions`](./checkmarkoptions.md) for possible configuration options.

## See Also

### Creating a checkmark accessory
- [UICellAccessory.CheckmarkOptions](./checkmarkoptions.md)
  Configuration options for a checkmark accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicellaccessory-swift.struct/checkmark(displayed:options:))*