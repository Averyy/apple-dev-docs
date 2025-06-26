# TCThrottleDescriptor

**Framework**: Touch Controller  
**Kind**: class

A descriptor for configuring a throttle.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
class TCThrottleDescriptor
```

## Topics

### Creating the descriptor
- [init()](tcthrottledescriptor/init.md)
  Creates a new throttle descriptor with default values.
### Inspecting the descriptor
- [var anchor: TCTransformAnchor](tcthrottledescriptor/anchor.md)
  The anchor point that the throttle’s offset is relative to.
- [var backgroundVisuals: TCControlVisuals?](tcthrottledescriptor/backgroundvisuals.md)
  The visuals for the background of the throttle.
- [var baseValue: CGFloat](tcthrottledescriptor/basevalue.md)
  The initial value of this control.
- [var colliderType: TCColliderType](tcthrottledescriptor/collidertype.md)
  The type of collider to use for the throttle.
- [var highlightTime: simd_float1](tcthrottledescriptor/highlighttime.md)
  The time it takes for a highlight to fade away, in seconds.
- [var indicatorSize: CGSize](tcthrottledescriptor/indicatorsize.md)
  The size (width, height) of the indicator itself in points.
- [var indicatorVisuals: TCControlVisuals?](tcthrottledescriptor/indicatorvisuals.md)
  The visuals for the indicator of the throttle.
- [var label: TCControlLabel](tcthrottledescriptor/label.md)
  The label associated with the throttle.
- [var layer: simd_int1](tcthrottledescriptor/layer.md)
  The layer of the throttle, used for z-sorting.
- [var offset: CGPoint](tcthrottledescriptor/offset.md)
  The control’s offset from the anchor, which determines its position.
- [var orientation: TCThrottleOrientation](tcthrottledescriptor/orientation.md)
  The orientation of the throttle.
- [var size: CGSize](tcthrottledescriptor/size.md)
  The size (width, height) of the throttle in points.
- [var snapToBaseValue: Bool](tcthrottledescriptor/snaptobasevalue.md)
  A Boolean value that indicates whether the control reverts to it’s base value.
- [var throttleSize: CGSize](tcthrottledescriptor/throttlesize.md)
  The size (width, height) of the throttle itself, providing boundaries for the indicator, in points.

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

- [class TCButtonDescriptor](tcbuttondescriptor.md)
  A descriptor for configuring a button.
- [class TCDirectionPadDescriptor](tcdirectionpaddescriptor.md)
  A descriptor for configuring a directional pad.
- [class TCThumbstickDescriptor](tcthumbstickdescriptor.md)
  A descriptor for configuring a thumbstick.
- [class TCTouchpadDescriptor](tctouchpaddescriptor.md)
  A descriptor for configuring a touchpad.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tcthrottledescriptor)*