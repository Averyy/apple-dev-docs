# TCThumbstickDescriptor

**Framework**: Touch Controller  
**Kind**: class

A descriptor for configuring a thumbstick.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
class TCThumbstickDescriptor
```

## Topics

### Creating the descriptor
- [init()](tcthumbstickdescriptor/init.md)
  Creates a new thumbstick descriptor with default values.
### Inspecting the descriptor
- [var backgroundContents: TCControlContents?](tcthumbstickdescriptor/backgroundcontents.md)
  The contents for the background of the thumbstick.
- [var hidesWhenNotPressed: Bool](tcthumbstickdescriptor/hideswhennotpressed.md)
  Whether to hide the thumbstick when it is not being pressed.
- [var highlightDuration: TimeInterval](tcthumbstickdescriptor/highlightduration.md)
  The time it takes for a highlight to fade away, in seconds.
- [var label: TCControlLabel](tcthumbstickdescriptor/label.md)
  The label associated with the thumbstick.
- [var offset: CGPoint](tcthumbstickdescriptor/offset.md)
  The control’s offset from the anchor, which determines its position.
- [var size: CGSize](tcthumbstickdescriptor/size.md)
  The size (width, height) of the thumbstick in points.
- [var stickContents: TCControlContents?](tcthumbstickdescriptor/stickcontents.md)
  The contents for the thumbstick itself.
- [var stickSize: CGSize](tcthumbstickdescriptor/sticksize.md)
  The size (width, height) of the thumbstick stick itself in points.
- [var zIndex: Int](tcthumbstickdescriptor/zindex.md)
  The z-index of the thumbstick. A lower z-index is drawn first.
### Accessing the anchor
- [var anchor: TCControlLayoutAnchor](tcthumbstickdescriptor/anchor.md)
  The anchor point that the thumbstick’s offset is relative to.
- [enum TCControlLayoutAnchor](tccontrollayoutanchor.md)
  Defines the anchor point for a control.
- [var anchorCoordinateSystem: TCControlLayoutAnchorCoordinateSystem](tcthumbstickdescriptor/anchorcoordinatesystem.md)
  The coordinate system for the control’s anchor point.
- [enum TCControlLayoutAnchorCoordinateSystem](tccontrollayoutanchorcoordinatesystem.md)
  Defines the coodinate system for an anchor point.
### Getting the collider shape
- [var colliderShape: TCColliderShape](tcthumbstickdescriptor/collidershape.md)
  The shape of collider to use for the thumbstick.
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

- [func addThumbstick(descriptor: TCThumbstickDescriptor) -> TCThumbstick](tctouchcontroller/addthumbstick(descriptor:).md)
  Creates a new thumbstick control with the provided descriptor, and adds it to the touch controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tcthumbstickdescriptor)*