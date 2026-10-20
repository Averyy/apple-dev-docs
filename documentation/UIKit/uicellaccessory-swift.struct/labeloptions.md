# UICellAccessory.LabelOptions

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

Configuration options for a label accessory.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS

## Declaration

```swift
struct LabelOptions
```

## Topics

### Creating configuration options
- [init(isHidden: Bool?, reservedLayoutWidth: UICellAccessory.LayoutDimension?, tintColor: UIColor?, font: UIFont?, adjustsFontForContentSizeCategory: Bool?)](./labeloptions/init%28ishidden,reservedlayoutwidth,tintcolor,font,adjustsfontforcontentsizecategory%29.md)
  Creates a label accessory options structure.
### Accessing configuration options
- [var isHidden: Bool](./labeloptions/ishidden.md)
  A Boolean value that determines whether the cell hides the accessory.
- [var reservedLayoutWidth: UICellAccessory.LayoutDimension](./labeloptions/reservedlayoutwidth.md)
  The layout width that the system reserves for the accessory, and then centers the accessory within.
- [var tintColor: UIColor?](./labeloptions/tintcolor.md)
  The tint color to apply to the accessory.
- [var font: UIFont](./labeloptions/font.md)
  The font for the label.
- [var adjustsFontForContentSizeCategory: Bool](./labeloptions/adjustsfontforcontentsizecategory.md)
  A Boolean value that determines whether the label automatically adjusts its font according to the content size category.

## See Also

### Creating a label accessory
- [static func label(text: String, displayed: UICellAccessory.DisplayedState, options: UICellAccessory.LabelOptions) -> UICellAccessory](./label%28text,displayed,options%29.md)
  Creates a label system accessory with the specified text, display state, and configuration options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicellaccessory-swift.struct/labeloptions)*