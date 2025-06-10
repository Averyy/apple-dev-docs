# detail(displayed:options:actionHandler:)

**Framework**: UIKit  
**Kind**: method

Creates a detail system accessory with the specified display state, configuration options, and optional action handler.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst ?+
- tvOS 15.4+
- visionOS ?+

## Declaration

```swift
static func detail(displayed: UICellAccessory.DisplayedState = .always, options: UICellAccessory.DetailOptions = DetailOptions(), actionHandler: UICellAccessory.ActionHandler? = nil) -> UICellAccessory
```

#### Return Value

A configured detail cell accessory. The accessory displays as the system information button. This accessory appears on the trailing edge of the cell.

## Parameters

- `displayed`: The cell-editing states that the detail accessory appears in. This parameter has a default value of  .
- `options`: Configuration options for the detail accessory. See   for possible configuration options.
- `actionHandler`: An optional closure that the system calls when a user interacts with the detail accessory.

## See Also

- [UICellAccessory.DetailOptions](uicellaccessory-swift.struct/detailoptions.md)
  Configuration options for a detail accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicellaccessory-swift.struct/detail(displayed:options:actionhandler:))*