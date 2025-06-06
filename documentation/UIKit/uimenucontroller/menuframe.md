# menuFrame

**Framework**: UIKit  
**Kind**: property

Returns the frame of the editing menu.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var menuFrame: CGRect { get }
```

#### Discussion

The property value is the bounding rectangle of the menu in screen coordinates. The property has a value of [`CGRectZero`](https://developer.apple.com/documentation/CoreGraphics/CGRectZero) if the menu is not visible. You can use this property to adjust any user-interface objects away from the menu after displaying the menu.

## See Also

- [var arrowDirection: UIMenuController.ArrowDirection](uimenucontroller/arrowdirection-swift.property.md)
  The direction the arrow of the editing menu is pointing.
- [UIMenuController.ArrowDirection](uimenucontroller/arrowdirection-swift.enum.md)
  The direction the arrow of the editing menu is pointing.
- [func setTargetRect(CGRect, in: UIView)](uimenucontroller/settargetrect(_:in:).md)
  Sets the area in a view above or below which the editing menu is positioned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenucontroller/menuframe)*