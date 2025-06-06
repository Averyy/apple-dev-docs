# titleEdgeInsets

**Framework**: UIKit  
**Kind**: property

The inset or outset margins for the rectangle around the button’s title text.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS 2.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var titleEdgeInsets: UIEdgeInsets { get set }
```

#### Discussion

Use this property to resize and reposition the effective drawing rectangle for the button title. You can specify a different value for each of the four insets (top, left, bottom, right). A positive value shrinks, or insets, that edge—moving it closer to the center of the button. A negative value expands, or outsets, that edge. Use the [`init(top:left:bottom:right:)`](uiedgeinsets/init(top:left:bottom:right:)-1s1t9.md) function to construct a value for this property. The default value is [`zero`](uiedgeinsets/zero.md).

The insets you specify are applied to the title rectangle after that rectangle has been sized to fit the button’s text. Thus, positive inset values may actually clip the title text.

This property is used only for positioning the title during layout. The button does not use this property to determine [`intrinsicContentSize`](uiview/intrinsiccontentsize.md) and [`sizeThatFits(_:)`](uiview/sizethatfits(_:).md).

## See Also

- [var contentEdgeInsets: UIEdgeInsets](uibutton/contentedgeinsets.md)
  The inset or outset margins for the rectangle surrounding all of the button’s content.
- [var imageEdgeInsets: UIEdgeInsets](uibutton/imageedgeinsets.md)
  The inset or outset margins for the rectangle around the button’s image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/titleedgeinsets)*