# delete(displayed:options:actionHandler:)

**Framework**: UIKit  
**Kind**: method

Creates a delete system accessory with the specified display state, configuration options, and optional action handler.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
static func delete(displayed: UICellAccessory.DisplayedState = .whenEditing, options: UICellAccessory.DeleteOptions = DeleteOptions(), actionHandler: UICellAccessory.ActionHandler? = nil) -> UICellAccessory
```

#### Return Value

A configured delete cell accessory. This accessory is a minus sign inside of a circle with the default system red color. This accessory appears on the leading edge of the cell.

## Parameters

- `displayed`: The cell-editing states that the delete accessory appears in. This parameter has a default value of  .
- `options`: Configuration options for the delete accessory. See   for possible configuration options.
- `actionHandler`: An optional closure that the system calls when a user interacts with the delete accessory.

## See Also

- [UICellAccessory.DeleteOptions](uicellaccessory-swift.struct/deleteoptions.md)
  Configuration options for a delete accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicellaccessory-swift.struct/delete(displayed:options:actionhandler:))*