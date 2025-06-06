# arrowDirection

**Framework**: UIKit  
**Kind**: property

The direction the arrow of the editing menu is pointing.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var arrowDirection: UIMenuController.ArrowDirection { get set }
```

#### Discussion

You can set the direction editing-menu arrow points by assigning a [`UIMenuController.ArrowDirection`](uimenucontroller/arrowdirection-swift.enum.md) enum constant to this property. The default behavior ([`UIMenuController.ArrowDirection.default`](uimenucontroller/arrowdirection-swift.enum/default.md)) is to point up or down at the object of focus based on its location on the screen.

## See Also

- [var menuFrame: CGRect](uimenucontroller/menuframe.md)
  Returns the frame of the editing menu.
- [UIMenuController.ArrowDirection](uimenucontroller/arrowdirection-swift.enum.md)
  The direction the arrow of the editing menu is pointing.
- [func setTargetRect(CGRect, in: UIView)](uimenucontroller/settargetrect(_:in:).md)
  Sets the area in a view above or below which the editing menu is positioned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenucontroller/arrowdirection-swift.property)*