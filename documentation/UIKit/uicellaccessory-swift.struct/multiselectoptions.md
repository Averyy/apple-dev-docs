# UICellAccessory.MultiselectOptions

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

Configuration options for a multiselect accessory.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS

## Declaration

```swift
struct MultiselectOptions
```

## Topics

### Creating configuration options
- [init(isHidden: Bool?, reservedLayoutWidth: UICellAccessory.LayoutDimension?, tintColor: UIColor?, backgroundColor: UIColor?)](./multiselectoptions/init%28ishidden,reservedlayoutwidth,tintcolor,backgroundcolor%29.md)
  Creates a multiselect accessory options structure.
### Accessing configuration options
- [var isHidden: Bool](./multiselectoptions/ishidden.md)
  A Boolean value that determines whether the cell hides the accessory.
- [var reservedLayoutWidth: UICellAccessory.LayoutDimension](./multiselectoptions/reservedlayoutwidth.md)
  The layout width that the system reserves for the accessory, and then centers the accessory within.
- [var tintColor: UIColor?](./multiselectoptions/tintcolor.md)
  The tint color to apply to the accessory.
- [var backgroundColor: UIColor?](./multiselectoptions/backgroundcolor.md)
  The background color to apply to the accessory.

## See Also

### Creating a multiselect accessory
- [static func multiselect(displayed: UICellAccessory.DisplayedState, options: UICellAccessory.MultiselectOptions) -> UICellAccessory](./multiselect%28displayed,options%29.md)
  Creates a multiselect system accessory with the specified display state and configuration options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicellaccessory-swift.struct/multiselectoptions)*