# UIControl.ContentVerticalAlignment

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants for specifying the vertical alignment of content (text and images) in a control.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
enum ContentVerticalAlignment
```

```c
enum UIControlContentVerticalAlignment : NSInteger;
```

#### Overview

You use these constants as the value of the [`contentVerticalAlignment`](./contentverticalalignment-swift.property.md) property.

## Topics

### Constants
- [UIControl.ContentVerticalAlignment.center](./contentverticalalignment-swift.enum/center.md)
  Aligns the content vertically in the center of the control.
- [UIControl.ContentVerticalAlignment.top](./contentverticalalignment-swift.enum/top.md)
  Aligns the content vertically at the top in the control (the default).
- [UIControl.ContentVerticalAlignment.bottom](./contentverticalalignment-swift.enum/bottom.md)
  Aligns the content vertically at the bottom in the control.
- [UIControl.ContentVerticalAlignment.fill](./contentverticalalignment-swift.enum/fill.md)
  Aligns the content vertically to fill the content rectangle; images may be stretched.
### Initializers
- [init?(rawValue: Int)](./contentverticalalignment-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Specifying content alignment
- [var contentVerticalAlignment: UIControl.ContentVerticalAlignment](./contentverticalalignment-swift.property.md)
  The vertical alignment of content within the control’s bounds.
- [var contentHorizontalAlignment: UIControl.ContentHorizontalAlignment](./contenthorizontalalignment-swift.property.md)
  The horizontal alignment of content within the control’s bounds.
- [var effectiveContentHorizontalAlignment: UIControl.ContentHorizontalAlignment](./effectivecontenthorizontalalignment.md)
  The horizontal alignment currently in effect for the control.
- [UIControl.ContentHorizontalAlignment](./contenthorizontalalignment-swift.enum.md)
  The horizontal alignment of content (text and images) within a control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontrol/contentverticalalignment-swift.enum)*