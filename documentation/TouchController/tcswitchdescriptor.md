# TCSwitchDescriptor

**Framework**: Touch Controller  
**Kind**: class

A descriptor for configuring a switch.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
class TCSwitchDescriptor
```

## Topics

### Creating the descriptor
- [init()](tcswitchdescriptor/init.md)
  Creates a new switch descriptor with default values.
### Inspecting the descriptor
- [var contents: TCControlContents?](tcswitchdescriptor/contents.md)
  The contents for the switch in its normal state.
- [var highlightDuration: TimeInterval](tcswitchdescriptor/highlightduration.md)
  The time it takes for a highlight to fade away, in seconds.
- [var label: TCControlLabel](tcswitchdescriptor/label.md)
  The label you associate with the switch.
- [var offset: CGPoint](tcswitchdescriptor/offset.md)
  The control’s offset from the anchor, which determines its position.
- [var size: CGSize](tcswitchdescriptor/size.md)
  The size (width, height) of the switch in points.
- [var switchedOnContents: TCControlContents?](tcswitchdescriptor/switchedoncontents.md)
  The contents for the switch when it is switched on.
- [var zIndex: Int](tcswitchdescriptor/zindex.md)
  The z-index of the switch. A lower z-index is drawn first.
### Accessing the anchor
- [var anchor: TCControlLayoutAnchor](tcswitchdescriptor/anchor.md)
  The anchor point that the switch’s offset is relative to.
- [enum TCControlLayoutAnchor](tccontrollayoutanchor.md)
  Defines the anchor point for a control.
- [var anchorCoordinateSystem: TCControlLayoutAnchorCoordinateSystem](tcswitchdescriptor/anchorcoordinatesystem.md)
  The coordinate system for the control’s anchor point.
- [enum TCControlLayoutAnchorCoordinateSystem](tccontrollayoutanchorcoordinatesystem.md)
  Defines the coodinate system for an anchor point.
### Getting the collider shape
- [var colliderShape: TCColliderShape](tcswitchdescriptor/collidershape.md)
  The shape of collider to use for the switch.
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

- [func addSwitch(descriptor: TCSwitchDescriptor) -> TCSwitch](tctouchcontroller/addswitch(descriptor:).md)
  Creates a new switch control with the provided descriptor, and adds it to the touch controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tcswitchdescriptor)*