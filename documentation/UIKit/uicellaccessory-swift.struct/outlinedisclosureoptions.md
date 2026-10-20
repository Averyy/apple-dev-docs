# UICellAccessory.OutlineDisclosureOptions

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

Configuration options for an outline disclosure.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS

## Declaration

```swift
struct OutlineDisclosureOptions
```

## Topics

### Creating configuration options
- [init(style: UICellAccessory.OutlineDisclosureOptions.Style?, isHidden: Bool?, reservedLayoutWidth: UICellAccessory.LayoutDimension?, tintColor: UIColor?)](./outlinedisclosureoptions/init%28style,ishidden,reservedlayoutwidth,tintcolor%29.md)
  Creates an outline disclosure options structure.
### Accessing configuration options
- [var isHidden: Bool](./outlinedisclosureoptions/ishidden.md)
  A Boolean value that determines whether the cell hides the accessory.
- [var reservedLayoutWidth: UICellAccessory.LayoutDimension](./outlinedisclosureoptions/reservedlayoutwidth.md)
  The layout width that the system reserves for the accessory, and then centers the accessory within.
- [var tintColor: UIColor?](./outlinedisclosureoptions/tintcolor.md)
  The tint color to apply to the accessory.
- [var style: UICellAccessory.OutlineDisclosureOptions.Style](./outlinedisclosureoptions/style-swift.property.md)
  The style of the outline disclosure accessory.
- [UICellAccessory.OutlineDisclosureOptions.Style](./outlinedisclosureoptions/style-swift.enum.md)
  Constants that describe the style of the outline disclosure accessory.

## See Also

### Creating an outline disclosure
- [static func outlineDisclosure(displayed: UICellAccessory.DisplayedState, options: UICellAccessory.OutlineDisclosureOptions, actionHandler: UICellAccessory.ActionHandler?) -> UICellAccessory](./outlinedisclosure%28displayed,options,actionhandler%29.md)
  Creates an outline disclosure system accessory with the specified display state, configuration options, and optional action handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicellaccessory-swift.struct/outlinedisclosureoptions)*