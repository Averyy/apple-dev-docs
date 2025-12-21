# TCThrottleDescriptor

**Framework**: Touch Controller  
**Kind**: class

A descriptor for configuring a throttle.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
class TCThrottleDescriptor
```

## Topics

### Creating the descriptor
- [init()](tcthrottledescriptor/init.md)
  Creates a new throttle descriptor with default values.
### Inspecting the descriptor
- [var backgroundContents: TCControlContents?](tcthrottledescriptor/backgroundcontents.md)
  The contents for the background of the throttle.
- [var baseValue: CGFloat](tcthrottledescriptor/basevalue.md)
  The initial value of this control.
- [var highlightDuration: TimeInterval](tcthrottledescriptor/highlightduration.md)
  The time it takes for a highlight to fade away, in seconds.
- [var indicatorContents: TCControlContents?](tcthrottledescriptor/indicatorcontents.md)
  The contents for the indicator of the throttle.
- [var indicatorSize: CGSize](tcthrottledescriptor/indicatorsize.md)
  The size (width, height) of the indicator itself in points.
- [var label: TCControlLabel](tcthrottledescriptor/label.md)
  The label associated with the throttle.
- [var offset: CGPoint](tcthrottledescriptor/offset.md)
  The control’s offset from the anchor, which determines its position.
- [var orientation: TCThrottle.Orientation](tcthrottledescriptor/orientation.md)
  The orientation of the throttle.
- [var size: CGSize](tcthrottledescriptor/size.md)
  The size (width, height) of the throttle in points.
- [var snapsToBaseValue: Bool](tcthrottledescriptor/snapstobasevalue.md)
  A Boolean value that indicates whether the control reverts to it’s base value.
- [var throttleSize: CGSize](tcthrottledescriptor/throttlesize.md)
  The size (width, height) of the throttle itself, providing boundaries for the indicator, in points.
- [var zIndex: Int](tcthrottledescriptor/zindex.md)
  The z-index of the throttle. A lower z-index is drawn first.
### Accessing the anchor
- [var anchor: TCControlLayoutAnchor](tcthrottledescriptor/anchor.md)
  The anchor point that the throttle’s offset is relative to.
- [enum TCControlLayoutAnchor](tccontrollayoutanchor.md)
  Defines the anchor point for a control.
- [var anchorCoordinateSystem: TCControlLayoutAnchorCoordinateSystem](tcthrottledescriptor/anchorcoordinatesystem.md)
  The coordinate system for the control’s anchor point.
- [enum TCControlLayoutAnchorCoordinateSystem](tccontrollayoutanchorcoordinatesystem.md)
  Defines the coodinate system for an anchor point.
### Getting the collider shape
- [var colliderShape: TCColliderShape](tcthrottledescriptor/collidershape.md)
  The shape of collider to use for the throttle.
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

- [func addThrottle(descriptor: TCThrottleDescriptor) -> TCThrottle](tctouchcontroller/addthrottle(descriptor:).md)
  Creates a new throttle control with the provided descriptor, and adds it to the touch controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tcthrottledescriptor)*