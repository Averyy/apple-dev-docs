# contentHorizontalAlignment

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The horizontal alignment of content within the control’s bounds.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var contentHorizontalAlignment: UIControl.ContentHorizontalAlignment { get set }
```

```objc
@property (nonatomic) UIControlContentHorizontalAlignment contentHorizontalAlignment;
```

## Discussion

For controls that contain configurable text or image content, use this property to align that content appropriately inside the control’s bounds. Not all control subclasses have content that can be aligned, and it’s the responsibility of the subclass to determine how to apply this value. The default value of this property is [`UIControl.ContentHorizontalAlignment.center`](./contenthorizontalalignment-swift.enum/center.md).

## Parameters

- `contentAlignment`: A constant that specifies the horizontal alignment of text or images within the control. For a list of possible values, see [`UIControl.ContentHorizontalAlignment`](./contenthorizontalalignment-swift.enum.md).

## See Also

### Specifying content alignment
- [var contentVerticalAlignment: UIControl.ContentVerticalAlignment](./contentverticalalignment-swift.property.md)
  The vertical alignment of content within the control’s bounds.
- [UIControl.ContentVerticalAlignment](./contentverticalalignment-swift.enum.md)
  Constants for specifying the vertical alignment of content (text and images) in a control.
- [var effectiveContentHorizontalAlignment: UIControl.ContentHorizontalAlignment](./effectivecontenthorizontalalignment.md)
  The horizontal alignment currently in effect for the control.
- [UIControl.ContentHorizontalAlignment](./contenthorizontalalignment-swift.enum.md)
  The horizontal alignment of content (text and images) within a control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontrol/contenthorizontalalignment-swift.property)*