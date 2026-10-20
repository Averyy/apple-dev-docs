# UICellAccessory.MenuSelectedElementDidChangeHandler

**Framework**: UIKit  
**Kind**: typealias  
**Role**: Type Alias

A closure type that defines a handler to perform when a user selects an element in the menu.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS

## Declaration

```swift
typealias MenuSelectedElementDidChangeHandler = (UIMenu) -> Void
```

## See Also

### Creating a popup menu accessory
- [static func popUpMenu(UIMenu, displayed: UICellAccessory.DisplayedState, options: UICellAccessory.PopUpMenuOptions, selectedElementDidChangeHandler: UICellAccessory.MenuSelectedElementDidChangeHandler?) -> UICellAccessory](./popupmenu%28_,displayed,options,selectedelementdidchangehandler%29.md)
  Creates a popup menu system accessory with the specified menu, display state, configuration options, and optional selection handler.
- [UICellAccessory.PopUpMenuOptions](./popupmenuoptions.md)
  Configuration options for a popup menu accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicellaccessory-swift.struct/menuselectedelementdidchangehandler)*