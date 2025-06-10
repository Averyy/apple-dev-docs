# multiselect(displayed:options:)

**Framework**: UIKit  
**Kind**: method

Creates a multiselect system accessory with the specified display state and configuration options.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
static func multiselect(displayed: UICellAccessory.DisplayedState = .whenEditing, options: UICellAccessory.MultiselectOptions = MultiselectOptions()) -> UICellAccessory
```

#### Return Value

A configured multiselect cell accessory that changes apperance according to the cell’s selection state. The accessory displays as an empty circle for an unselected cell and as a filled circle with a checkmark for a selected cell. This accessory appears on the leading edge of the cell.

## Parameters

- `displayed`: The cell-editing states that the multiselect accessory appears in. This parameter has a default value of  .
- `options`: Configuration options for the multiselect accessory. See   for possible configuration options.

## See Also

- [UICellAccessory.MultiselectOptions](uicellaccessory-swift.struct/multiselectoptions.md)
  Configuration options for a multiselect accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicellaccessory-swift.struct/multiselect(displayed:options:))*