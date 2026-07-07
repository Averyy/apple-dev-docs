# TCButtonDescriptor

**Framework**: Touch Controller  
**Kind**: class

A descriptor for configuring a button.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
class TCButtonDescriptor
```

## Topics

### Creating the descriptor
- [init()](tcbuttondescriptor/init.md)
  Creates a new button descriptor with default values.
### Inspecting the descriptor
- [var contents: TCControlContents?](tcbuttondescriptor/contents.md)
  The contents for the button in its normal state.
- [var highlightDuration: TimeInterval](tcbuttondescriptor/highlightduration.md)
  The time it takes for a highlight to fade away, in seconds.
- [var zIndex: Int](tcbuttondescriptor/zindex.md)
  The z-index of the button. A lower z-index is drawn first.
- [var label: TCControlLabel](tcbuttondescriptor/label.md)
  The label you associate with the button.
- [var offset: CGPoint](tcbuttondescriptor/offset.md)
  The control’s offset from the anchor, which determines its position.
- [var size: CGSize](tcbuttondescriptor/size.md)
  The size (width, height) of the button in points.
### Accessing the anchor
- [var anchor: TCControlLayoutAnchor](tcbuttondescriptor/anchor.md)
  The anchor point that the button’s offset is relative to.
- [enum TCControlLayoutAnchor](tccontrollayoutanchor.md)
  Defines the anchor point for a control.
- [var anchorCoordinateSystem: TCControlLayoutAnchorCoordinateSystem](tcbuttondescriptor/anchorcoordinatesystem.md)
  The coordinate system for the control’s anchor point.
- [enum TCControlLayoutAnchorCoordinateSystem](tccontrollayoutanchorcoordinatesystem.md)
  Defines the coodinate system for an anchor point.
### Getting the collider shape
- [var colliderShape: TCColliderShape](tcbuttondescriptor/collidershape.md)
  The shape of collider to use for the button.
- [enum TCColliderShape](tccollidershape.md)
  Defines the shape of a control collider.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [func addButton(descriptor: TCButtonDescriptor) -> TCButton](tctouchcontroller/addbutton(descriptor:).md)
  Creates a new button control with the provided descriptor, and adds it to the touch controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tcbuttondescriptor)*