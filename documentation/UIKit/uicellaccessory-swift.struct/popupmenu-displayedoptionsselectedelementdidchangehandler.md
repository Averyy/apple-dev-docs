# popUpMenu(_:displayed:options:selectedElementDidChangeHandler:)

**Framework**: UIKit  
**Kind**: method

Creates a popup menu system accessory with the specified menu, display state, configuration options, and optional selection handler.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
static func popUpMenu(_ menu: UIMenu, displayed: UICellAccessory.DisplayedState = .always, options: UICellAccessory.PopUpMenuOptions = PopUpMenuOptions(), selectedElementDidChangeHandler: UICellAccessory.MenuSelectedElementDidChangeHandler? = nil) -> UICellAccessory
```

#### Return Value

A configured popup menu cell accessory that appears as a pair of chevrons that point upward and downward. This accessory indicates that tapping anywhere in the cell presents a popup menu. This accessory appears on the trailing edge of the cell.

## Parameters

- `menu`: The menu to display when a user taps the popup menu accessory.
- `displayed`: The cell-editing states that the popup menu accessory appears in. This parameter has a default value of  .
- `options`: Configuration options for the popup menu accessory. See   for possible configuration options.
- `selectedElementDidChangeHandler`: An optional closure that the system calls when a user selects an element in the menu.

## See Also

- [UICellAccessory.MenuSelectedElementDidChangeHandler](uicellaccessory-swift.struct/menuselectedelementdidchangehandler.md)
  A closure type that defines a handler to perform when a user selects an element in the menu.
- [UICellAccessory.PopUpMenuOptions](uicellaccessory-swift.struct/popupmenuoptions.md)
  Configuration options for a popup menu accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicellaccessory-swift.struct/popupmenu(_:displayed:options:selectedelementdidchangehandler:))*