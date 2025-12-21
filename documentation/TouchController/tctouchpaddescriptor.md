# TCTouchpadDescriptor

**Framework**: Touch Controller  
**Kind**: class

A descriptor for configuring a touchpad.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
class TCTouchpadDescriptor
```

## Topics

### Creating the descriptor
- [init()](tctouchpaddescriptor/init.md)
  Creates a new touchpad descriptor with default values.
### Inspecting the descriptor
- [var contents: TCControlContents?](tctouchpaddescriptor/contents.md)
  The contents for the touchpad.
- [var highlightDuration: TimeInterval](tctouchpaddescriptor/highlightduration.md)
  The time it takes for a highlight to fade away, in seconds.
- [var label: TCControlLabel](tctouchpaddescriptor/label.md)
  The label associated with the touchpad.
- [var offset: CGPoint](tctouchpaddescriptor/offset.md)
  The control’s offset from the anchor, which determines its position.
- [var reportsRelativeValues: Bool](tctouchpaddescriptor/reportsrelativevalues.md)
  A Boolean value that represents the touchpad reports deltas.
- [var size: CGSize](tctouchpaddescriptor/size.md)
  The size (width, height) of the touchpad in points.
- [var zIndex: Int](tctouchpaddescriptor/zindex.md)
  The z-index of the touchpad. A lower z-index is drawn first.
### Accessing the anchor
- [var anchor: TCControlLayoutAnchor](tctouchpaddescriptor/anchor.md)
  The anchor point that the touchpad’s offset is relative to.
- [enum TCControlLayoutAnchor](tccontrollayoutanchor.md)
  Defines the anchor point for a control.
- [var anchorCoordinateSystem: TCControlLayoutAnchorCoordinateSystem](tctouchpaddescriptor/anchorcoordinatesystem.md)
  The coordinate system for the control’s anchor point.
- [enum TCControlLayoutAnchorCoordinateSystem](tccontrollayoutanchorcoordinatesystem.md)
  Defines the coodinate system for an anchor point.
### Getting the collider shape
- [var colliderShape: TCColliderShape](tctouchpaddescriptor/collidershape.md)
  The shape of collider to use for the touchpad.
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

- [func addTouchpad(descriptor: TCTouchpadDescriptor) -> TCTouchpad](tctouchcontroller/addtouchpad(descriptor:).md)
  Creates a new touchpad control with the provided descriptor, and adds it to the touch controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tctouchpaddescriptor)*