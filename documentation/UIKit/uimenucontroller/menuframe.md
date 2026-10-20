# menuFrame

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Returns the frame of the editing menu.

**Availability**:
- iOS 3.0+ - Deprecated in 16.0
- iPadOS 3.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: For more information, see [`UIMenuController`](../uimenucontroller.md).

## Declaration

```swift
var menuFrame: CGRect { get }
```

```objc
@property (nonatomic, readonly) CGRect menuFrame;
```

#### Discussion

The property value is the bounding rectangle of the menu in screen coordinates. The property has a value of [`CGRectZero`](../../CoreGraphics/cgrectzero.md) if the menu is not visible. You can use this property to adjust any user-interface objects away from the menu after displaying the menu.

## See Also

### Positioning the menu
- [var arrowDirection: UIMenuController.ArrowDirection](./arrowdirection-swift.property.md)
  The direction the arrow of the editing menu is pointing.
- [UIMenuController.ArrowDirection](./arrowdirection-swift.enum.md)
  The direction the arrow of the editing menu is pointing.
- [func setTargetRect(CGRect, in: UIView)](./settargetrect%28_,in%29.md)
  Sets the area in a view above or below which the editing menu is positioned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenucontroller/menuframe)*