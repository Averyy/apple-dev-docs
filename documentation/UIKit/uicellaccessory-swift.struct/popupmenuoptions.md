# UICellAccessory.PopUpMenuOptions

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

Configuration options for a popup menu accessory.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS

## Declaration

```swift
struct PopUpMenuOptions
```

## Topics

### Creating configuration options
- [init(isHidden: Bool?, reservedLayoutWidth: UICellAccessory.LayoutDimension?, tintColor: UIColor?)](./popupmenuoptions/init%28ishidden,reservedlayoutwidth,tintcolor%29.md)
  Creates a popup menu accessory options structure.
### Accessing configuration options
- [var isHidden: Bool](./popupmenuoptions/ishidden.md)
  A Boolean value that determines whether the cell hides the accessory.
- [var reservedLayoutWidth: UICellAccessory.LayoutDimension](./popupmenuoptions/reservedlayoutwidth.md)
  The layout width that the system reserves for the accessory, and then centers the accessory within.
- [var tintColor: UIColor?](./popupmenuoptions/tintcolor.md)
  The tint color to apply to the accessory.

## See Also

### Creating a popup menu accessory
- [static func popUpMenu(UIMenu, displayed: UICellAccessory.DisplayedState, options: UICellAccessory.PopUpMenuOptions, selectedElementDidChangeHandler: UICellAccessory.MenuSelectedElementDidChangeHandler?) -> UICellAccessory](./popupmenu%28_,displayed,options,selectedelementdidchangehandler%29.md)
  Creates a popup menu system accessory with the specified menu, display state, configuration options, and optional selection handler.
- [UICellAccessory.MenuSelectedElementDidChangeHandler](./menuselectedelementdidchangehandler.md)
  A closure type that defines a handler to perform when a user selects an element in the menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicellaccessory-swift.struct/popupmenuoptions)*