# arrowDirection

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The direction the arrow of the editing menu is pointing.

**Availability**:
- iOS 3.2+ - Deprecated in 16.0
- iPadOS 3.2+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
var arrowDirection: UIMenuController.ArrowDirection { get set }
```

```objc
@property (nonatomic) UIMenuControllerArrowDirection arrowDirection;
```

## Discussion

You can set the direction editing-menu arrow points by assigning a [`UIMenuController.ArrowDirection`](./arrowdirection-swift.enum.md) enum constant to this property. The default behavior ([`UIMenuController.ArrowDirection.default`](./arrowdirection-swift.enum/default.md)) is to point up or down at the object of focus based on its location on the screen.

## See Also

### Positioning the menu
- [var menuFrame: CGRect](./menuframe.md)
  Returns the frame of the editing menu.
- [UIMenuController.ArrowDirection](./arrowdirection-swift.enum.md)
  The direction the arrow of the editing menu is pointing.
- [func setTargetRect(CGRect, in: UIView)](./settargetrect%28_,in%29.md)
  Sets the area in a view above or below which the editing menu is positioned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenucontroller/arrowdirection-swift.property)*