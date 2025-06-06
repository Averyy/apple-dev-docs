# effectiveContentHorizontalAlignment

**Framework**: UIKit  
**Kind**: property

The horizontal alignment currently in effect for the control.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var effectiveContentHorizontalAlignment: UIControl.ContentHorizontalAlignment { get }
```

#### Discussion

This property always contains the value [`UIControl.ContentHorizontalAlignment.left`](uicontrol/contenthorizontalalignment-swift.enum/left.md) or [`UIControl.ContentHorizontalAlignment.right`](uicontrol/contenthorizontalalignment-swift.enum/right.md), even when the actual horizontal alignment is [`UIControl.ContentHorizontalAlignment.leading`](uicontrol/contenthorizontalalignment-swift.enum/leading.md) or [`UIControl.ContentHorizontalAlignment.trailing`](uicontrol/contenthorizontalalignment-swift.enum/trailing.md).

## See Also

- [var contentVerticalAlignment: UIControl.ContentVerticalAlignment](uicontrol/contentverticalalignment-swift.property.md)
  The vertical alignment of content within the control’s bounds.
- [UIControl.ContentVerticalAlignment](uicontrol/contentverticalalignment-swift.enum.md)
  Constants for specifying the vertical alignment of content (text and images) in a control.
- [var contentHorizontalAlignment: UIControl.ContentHorizontalAlignment](uicontrol/contenthorizontalalignment-swift.property.md)
  The horizontal alignment of content within the control’s bounds.
- [UIControl.ContentHorizontalAlignment](uicontrol/contenthorizontalalignment-swift.enum.md)
  The horizontal alignment of content (text and images) within a control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontrol/effectivecontenthorizontalalignment)*