# imageEdgeInsets

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The inset or outset margins for the rectangle around the button’s image.

**Availability**:
- iOS 2.0+ - Deprecated in 15.0
- iPadOS 2.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- tvOS 2.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`layoutSubviews()`](../uiview/layoutsubviews%28%29.md) instead.

## Declaration

```swift
var imageEdgeInsets: UIEdgeInsets { get set }
```

```objc
@property (nonatomic) UIEdgeInsets imageEdgeInsets;
```

#### Discussion

Use this property to resize and reposition the effective drawing rectangle for the button image. You can specify a different value for each of the four insets (top, left, bottom, right). A positive value shrinks, or insets, that edge—moving it closer to the center of the button. A negative value expands, or outsets, that edge. Use the [`init(top:left:bottom:right:)`](../uiedgeinsets/init%28top,left,bottom,right%29-1s1t9.md) function to construct a value for this property. The default value is [`zero`](../uiedgeinsets/zero.md).

This property is used only for positioning the image during layout. The button does not use this property to determine [`intrinsicContentSize`](../uiview/intrinsiccontentsize.md) and [`sizeThatFits(_:)`](../uiview/sizethatfits%28_%29.md).

## See Also

### Deprecated edge insets
- [var contentEdgeInsets: UIEdgeInsets](./contentedgeinsets.md)
  The inset or outset margins for the rectangle surrounding all of the button’s content.
- [var titleEdgeInsets: UIEdgeInsets](./titleedgeinsets.md)
  The inset or outset margins for the rectangle around the button’s title text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/imageedgeinsets)*