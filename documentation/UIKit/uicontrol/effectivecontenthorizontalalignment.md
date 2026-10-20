# effectiveContentHorizontalAlignment

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The horizontal alignment currently in effect for the control.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var effectiveContentHorizontalAlignment: UIControl.ContentHorizontalAlignment { get }
```

```objc
@property (nonatomic, readonly) UIControlContentHorizontalAlignment effectiveContentHorizontalAlignment;
```

#### Discussion

This property always contains the value [`UIControl.ContentHorizontalAlignment.left`](./contenthorizontalalignment-swift.enum/left.md) or [`UIControl.ContentHorizontalAlignment.right`](./contenthorizontalalignment-swift.enum/right.md), even when the actual horizontal alignment is [`UIControl.ContentHorizontalAlignment.leading`](./contenthorizontalalignment-swift.enum/leading.md) or [`UIControl.ContentHorizontalAlignment.trailing`](./contenthorizontalalignment-swift.enum/trailing.md).

## See Also

### Specifying content alignment
- [var contentVerticalAlignment: UIControl.ContentVerticalAlignment](./contentverticalalignment-swift.property.md)
  The vertical alignment of content within the control’s bounds.
- [UIControl.ContentVerticalAlignment](./contentverticalalignment-swift.enum.md)
  Constants for specifying the vertical alignment of content (text and images) in a control.
- [var contentHorizontalAlignment: UIControl.ContentHorizontalAlignment](./contenthorizontalalignment-swift.property.md)
  The horizontal alignment of content within the control’s bounds.
- [UIControl.ContentHorizontalAlignment](./contenthorizontalalignment-swift.enum.md)
  The horizontal alignment of content (text and images) within a control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontrol/effectivecontenthorizontalalignment)*