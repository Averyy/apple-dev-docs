# insert(displayed:options:actionHandler:)

**Framework**: UIKit  
**Kind**: method

Creates an insert system accessory with the specified display state, configuration options, and optional action handler.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
static func insert(displayed: UICellAccessory.DisplayedState = .whenEditing, options: UICellAccessory.InsertOptions = InsertOptions(), actionHandler: UICellAccessory.ActionHandler? = nil) -> UICellAccessory
```

#### Return Value

A configured insert cell accessory. This accessory is a plus sign inside of a circle with the default system green color. This accessory appears on the leading edge of the cell.

## Parameters

- `displayed`: The cell-editing states that the insert accessory appears in. This parameter has a default value of  .
- `options`: Configuration options for the insert accessory. See   for possible configuration options.
- `actionHandler`: An optional closure that the system calls when a user interacts with the insert accessory.

## See Also

- [UICellAccessory.InsertOptions](uicellaccessory-swift.struct/insertoptions.md)
  Configuration options for an insert accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicellaccessory-swift.struct/insert(displayed:options:actionhandler:))*