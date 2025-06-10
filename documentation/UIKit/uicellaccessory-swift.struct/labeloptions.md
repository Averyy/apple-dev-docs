# UICellAccessory.LabelOptions

**Framework**: UIKit  
**Kind**: struct

Configuration options for a label accessory.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
struct LabelOptions
```

## Topics

### Creating configuration options
- [init(isHidden: Bool?, reservedLayoutWidth: UICellAccessory.LayoutDimension?, tintColor: UIColor?, font: UIFont?, adjustsFontForContentSizeCategory: Bool?)](uicellaccessory-swift.struct/labeloptions/init(ishidden:reservedlayoutwidth:tintcolor:font:adjustsfontforcontentsizecategory:).md)
  Creates a label accessory options structure.
### Accessing configuration options
- [var isHidden: Bool](uicellaccessory-swift.struct/labeloptions/ishidden.md)
  A Boolean value that determines whether the cell hides the accessory.
- [var reservedLayoutWidth: UICellAccessory.LayoutDimension](uicellaccessory-swift.struct/labeloptions/reservedlayoutwidth.md)
  The layout width that the system reserves for the accessory, and then centers the accessory within.
- [var tintColor: UIColor?](uicellaccessory-swift.struct/labeloptions/tintcolor.md)
  The tint color to apply to the accessory.
- [var font: UIFont](uicellaccessory-swift.struct/labeloptions/font.md)
  The font for the label.
- [var adjustsFontForContentSizeCategory: Bool](uicellaccessory-swift.struct/labeloptions/adjustsfontforcontentsizecategory.md)
  A Boolean value that determines whether the label automatically adjusts its font according to the content size category.

## See Also

- [static func label(text: String, displayed: UICellAccessory.DisplayedState, options: UICellAccessory.LabelOptions) -> UICellAccessory](uicellaccessory-swift.struct/label(text:displayed:options:).md)
  Creates a label system accessory with the specified text, display state, and configuration options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicellaccessory-swift.struct/labeloptions)*