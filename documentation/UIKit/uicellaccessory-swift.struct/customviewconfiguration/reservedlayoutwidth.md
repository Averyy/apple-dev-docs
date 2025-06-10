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

![Diagram of three cells, each of which contains one accessory on the leading side. The accessories vary in width, but use the same reserved layout width to achieve consistent alignment. Annotations running the height of the diagram illustrate the static width.](https://docs-assets.developer.apple.com/published/e3246a54d7c4b18fe3b2101d0a737694/media-3681825%402x.png)

## See Also

- [var isHidden: Bool](uicellaccessory-swift.struct/customviewconfiguration/ishidden.md)
  A Boolean value that determines whether the cell hides the accessory.
- [let customView: UIView](uicellaccessory-swift.struct/customviewconfiguration/customview.md)
  The custom view to display for the accessory.
- [let placement: UICellAccessory.Placement](uicellaccessory-swift.struct/customviewconfiguration/placement.md)
  The placement for the accessory.
- [var tintColor: UIColor?](uicellaccessory-swift.struct/customviewconfiguration/tintcolor.md)
  The tint color to apply to the accessory.
- [var maintainsFixedSize: Bool](uicellaccessory-swift.struct/customviewconfiguration/maintainsfixedsize.md)
  A Boolean value that determines whether to preserve the frame size of the custom view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicellaccessory-swift.struct/customviewconfiguration/reservedlayoutwidth)*