# UIControl.ContentHorizontalAlignment

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

The horizontal alignment of content (text and images) within a control.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
enum ContentHorizontalAlignment
```

```c
enum UIControlContentHorizontalAlignment : NSInteger;
```

## Overview

You use these constants as the value of the [`contentHorizontalAlignment`](./contenthorizontalalignment-swift.property.md) property.

## Topics

### Constants
- [UIControl.ContentHorizontalAlignment.center](./contenthorizontalalignment-swift.enum/center.md)
  Aligns the content horizontally in the center of the control.
- [UIControl.ContentHorizontalAlignment.left](./contenthorizontalalignment-swift.enum/left.md)
  Aligns the content horizontally from the left of the control (the default).
- [UIControl.ContentHorizontalAlignment.right](./contenthorizontalalignment-swift.enum/right.md)
  Aligns the content horizontally from the right of the control.
- [UIControl.ContentHorizontalAlignment.fill](./contenthorizontalalignment-swift.enum/fill.md)
  Aligns the content horizontally to fill the content rectangles; text may wrap and images may be stretched.
- [UIControl.ContentHorizontalAlignment.leading](./contenthorizontalalignment-swift.enum/leading.md)
  Aligns the content horizontally from the leading edge of the control.
- [UIControl.ContentHorizontalAlignment.trailing](./contenthorizontalalignment-swift.enum/trailing.md)
  Aligns the content horizontally from the trailing edge of the control.
### Initializers
- [init?(rawValue: Int)](./contenthorizontalalignment-swift.enum/init%28rawvalue%29.md)

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
- [UIControl.ContentVerticalAlignment](./contentverticalalignment-swift.enum.md)
  Constants for specifying the vertical alignment of content (text and images) in a control.
- [var contentHorizontalAlignment: UIControl.ContentHorizontalAlignment](./contenthorizontalalignment-swift.property.md)
  The horizontal alignment of content within the control’s bounds.
- [var effectiveContentHorizontalAlignment: UIControl.ContentHorizontalAlignment](./effectivecontenthorizontalalignment.md)
  The horizontal alignment currently in effect for the control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontrol/contenthorizontalalignment-swift.enum)*