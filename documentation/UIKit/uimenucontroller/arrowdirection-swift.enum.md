# UIMenuController.ArrowDirection

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

The direction the arrow of the editing menu is pointing.

**Availability**:
- iOS 3.2+ - Deprecated in 16.0
- iPadOS 3.2+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: For more information, see [`UIMenuController`](../uimenucontroller.md).

## Declaration

```swift
enum ArrowDirection
```

```c
enum UIMenuControllerArrowDirection : NSInteger;
```

## Topics

### Constants
- [UIMenuController.ArrowDirection.default](./arrowdirection-swift.enum/default.md)
  The arrow is pointing up or down at the object of focus based on its location in the screen.
- [UIMenuController.ArrowDirection.up](./arrowdirection-swift.enum/up.md)
  The arrow is pointing up at the object of focus.
- [UIMenuController.ArrowDirection.down](./arrowdirection-swift.enum/down.md)
  The arrow is pointing down at the object of focus.
- [UIMenuController.ArrowDirection.left](./arrowdirection-swift.enum/left.md)
  The arrow is pointing left at the object of focus.
- [UIMenuController.ArrowDirection.right](./arrowdirection-swift.enum/right.md)
  The arrow is pointing right at the object of focus.
### Initializers
- [init?(rawValue: Int)](./arrowdirection-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Positioning the menu
- [var menuFrame: CGRect](./menuframe.md)
  Returns the frame of the editing menu.
- [var arrowDirection: UIMenuController.ArrowDirection](./arrowdirection-swift.property.md)
  The direction the arrow of the editing menu is pointing.
- [func setTargetRect(CGRect, in: UIView)](./settargetrect%28_,in%29.md)
  Sets the area in a view above or below which the editing menu is positioned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenucontroller/arrowdirection-swift.enum)*