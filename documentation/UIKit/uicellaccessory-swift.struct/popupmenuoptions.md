# UICellAccessory.PopUpMenuOptions

**Framework**: UIKit  
**Kind**: struct

Configuration options for a popup menu accessory.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
struct PopUpMenuOptions
```

## Topics

### Creating configuration options
- [init(isHidden: Bool?, reservedLayoutWidth: UICellAccessory.LayoutDimension?, tintColor: UIColor?)](uicellaccessory-swift.struct/popupmenuoptions/init(ishidden:reservedlayoutwidth:tintcolor:).md)
  Creates a popup menu accessory options structure.
### Accessing configuration options
- [var isHidden: Bool](uicellaccessory-swift.struct/popupmenuoptions/ishidden.md)
  A Boolean value that determines whether the cell hides the accessory.
- [var reservedLayoutWidth: UICellAccessory.LayoutDimension](uicellaccessory-swift.struct/popupmenuoptions/reservedlayoutwidth.md)
  The layout width that the system reserves for the accessory, and then centers the accessory within.
- [var tintColor: UIColor?](uicellaccessory-swift.struct/popupmenuoptions/tintcolor.md)
  The tint color to apply to the accessory.

## See Also

- [static func popUpMenu(UIMenu, displayed: UICellAccessory.DisplayedState, options: UICellAccessory.PopUpMenuOptions, selectedElementDidChangeHandler: UICellAccessory.MenuSelectedElementDidChangeHandler?) -> UICellAccessory](uicellaccessory-swift.struct/popupmenu(_:displayed:options:selectedelementdidchangehandler:).md)
  Creates a popup menu system accessory with the specified menu, display state, configuration options, and optional selection handler.
- [UICellAccessory.MenuSelectedElementDidChangeHandler](uicellaccessory-swift.struct/menuselectedelementdidchangehandler.md)
  A closure type that defines a handler to perform when a user selects an element in the menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicellaccessory-swift.struct/popupmenuoptions)*