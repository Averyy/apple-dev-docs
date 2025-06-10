# UICellAccessory.OutlineDisclosureOptions

**Framework**: UIKit  
**Kind**: struct

Configuration options for an outline disclosure.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
struct OutlineDisclosureOptions
```

## Topics

### Creating configuration options
- [init(style: UICellAccessory.OutlineDisclosureOptions.Style?, isHidden: Bool?, reservedLayoutWidth: UICellAccessory.LayoutDimension?, tintColor: UIColor?)](uicellaccessory-swift.struct/outlinedisclosureoptions/init(style:ishidden:reservedlayoutwidth:tintcolor:).md)
  Creates an outline disclosure options structure.
### Accessing configuration options
- [var isHidden: Bool](uicellaccessory-swift.struct/outlinedisclosureoptions/ishidden.md)
  A Boolean value that determines whether the cell hides the accessory.
- [var reservedLayoutWidth: UICellAccessory.LayoutDimension](uicellaccessory-swift.struct/outlinedisclosureoptions/reservedlayoutwidth.md)
  The layout width that the system reserves for the accessory, and then centers the accessory within.
- [var tintColor: UIColor?](uicellaccessory-swift.struct/outlinedisclosureoptions/tintcolor.md)
  The tint color to apply to the accessory.
- [var style: UICellAccessory.OutlineDisclosureOptions.Style](uicellaccessory-swift.struct/outlinedisclosureoptions/style-swift.property.md)
  The style of the outline disclosure accessory.
- [UICellAccessory.OutlineDisclosureOptions.Style](uicellaccessory-swift.struct/outlinedisclosureoptions/style-swift.enum.md)
  Constants that describe the style of the outline disclosure accessory.

## See Also

- [static func outlineDisclosure(displayed: UICellAccessory.DisplayedState, options: UICellAccessory.OutlineDisclosureOptions, actionHandler: UICellAccessory.ActionHandler?) -> UICellAccessory](uicellaccessory-swift.struct/outlinedisclosure(displayed:options:actionhandler:).md)
  Creates an outline disclosure system accessory with the specified display state, configuration options, and optional action handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicellaccessory-swift.struct/outlinedisclosureoptions)*