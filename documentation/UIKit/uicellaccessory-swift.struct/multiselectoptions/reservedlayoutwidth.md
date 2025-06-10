# reservedLayoutWidth

**Framework**: UIKit  
**Kind**: property

The layout width that the system reserves for the accessory, and then centers the accessory within.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
var reservedLayoutWidth: UICellAccessory.LayoutDimension
```

#### Discussion

Use this property to ensure consistent horizontal alignment from both system and custom accessories to your content, even when the accessories vary in size.

The reserved layout width only affects the amount of space for the accessory, and its positioning within that space. It doesn’t affect the size of the accessory.

![Diagram of three cells, each of which contains one accessory on the leading side. The accessories vary in width, but use the same reserved layout width to achieve consistent alignment. Annotations running the height of the diagram illustrate the static width.](https://docs-assets.developer.apple.com/published/e3246a54d7c4b18fe3b2101d0a737694/media-3681818%402x.png)

## See Also

- [var isHidden: Bool](uicellaccessory-swift.struct/multiselectoptions/ishidden.md)
  A Boolean value that determines whether the cell hides the accessory.
- [var tintColor: UIColor?](uicellaccessory-swift.struct/multiselectoptions/tintcolor.md)
  The tint color to apply to the accessory.
- [var backgroundColor: UIColor?](uicellaccessory-swift.struct/multiselectoptions/backgroundcolor.md)
  The background color to apply to the accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicellaccessory-swift.struct/multiselectoptions/reservedlayoutwidth)*