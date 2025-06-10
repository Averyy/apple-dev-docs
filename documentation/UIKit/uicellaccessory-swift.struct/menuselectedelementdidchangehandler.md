# UICellAccessory.MenuSelectedElementDidChangeHandler

**Framework**: UIKit  
**Kind**: typealias

A closure type that defines a handler to perform when a user selects an element in the menu.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
typealias MenuSelectedElementDidChangeHandler = (UIMenu) -> Void
```

## See Also

- [static func popUpMenu(UIMenu, displayed: UICellAccessory.DisplayedState, options: UICellAccessory.PopUpMenuOptions, selectedElementDidChangeHandler: UICellAccessory.MenuSelectedElementDidChangeHandler?) -> UICellAccessory](uicellaccessory-swift.struct/popupmenu(_:displayed:options:selectedelementdidchangehandler:).md)
  Creates a popup menu system accessory with the specified menu, display state, configuration options, and optional selection handler.
- [UICellAccessory.PopUpMenuOptions](uicellaccessory-swift.struct/popupmenuoptions.md)
  Configuration options for a popup menu accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicellaccessory-swift.struct/menuselectedelementdidchangehandler)*