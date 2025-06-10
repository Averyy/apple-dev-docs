# TCThrottle

**Framework**: Touch Controls  
**Kind**: class

Represents a single on-screen throttle - a one axis input.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
class TCThrottle
```

#### Overview

This is mirrored by a `GCControllerButtonInput` on the associated `GCController` instance.

## Topics

### Instance Properties
- [var anchor: TCTransformAnchor](tcthrottle/anchor.md)
  The anchor point that the throttle’s offset is relative to.
- [var backgroundVisuals: TCControlVisuals?](tcthrottle/backgroundvisuals.md)
  The visuals for the background of the throttle.
- [var baseValue: CGFloat](tcthrottle/basevalue.md)
  The initial value of this control.
- [var collider: any TCCollider](tcthrottle/collider.md)
  The collider for the throttle.
- [var highlightTime: simd_float1](tcthrottle/highlighttime.md)
  The time it takes for a highlight to fade away, in seconds.
- [var indicatorSize: CGSize](tcthrottle/indicatorsize.md)
  The size (width, height) of the indicator itself in points.
- [var indicatorVisuals: TCControlVisuals?](tcthrottle/indicatorvisuals.md)
  The visuals for the indicator of the throttle.
- [var layer: simd_int1](tcthrottle/layer.md)
  The layer of the throttle, used for z-sorting.
- [var offset: CGPoint](tcthrottle/offset.md)
  The control’s offset from the anchor, which determines its position.
- [var orientation: TCThrottleOrientation](tcthrottle/orientation.md)
  The orientation of the throttle.
- [var position: CGPoint](tcthrottle/position.md)
  The position of the throttle in points, with the origin at the top left corner of the screen.
- [var size: CGSize](tcthrottle/size.md)
  The size (width, height) of the throttle in points.
- [var snapToBaseValue: Bool](tcthrottle/snaptobasevalue.md)
  A Boolean value that indicates whether the control reverts to it’s base value.
- [var throttleSize: CGSize](tcthrottle/throttlesize.md)
  The size (width, height) of the throttle itself, providing boundaries for the indicator, in points.
- [var touchController: TCTouchController](tcthrottle/touchcontroller.md)
  The touch controller that manages this throttle.

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
- [TCControl](tccontrol.md)
- [TCTransform](tctransform.md)

## See Also

- [protocol TCControl](tccontrol.md)
  A protocol that defines the base properties and methods for all touch controls.
- [class TCButton](tcbutton.md)
  A control that represents a single on-screen button.
- [class TCDirectionPad](tcdirectionpad.md)
  An object that represents a direction pad.
- [class TCThumbstick](tcthumbstick.md)
  Represents a single on-screen thumbstick.
- [class TCTouchpad](tctouchpad.md)
  Represents a single on-screen touchpad that reports absolute coordinates or delta movements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontrols/tcthrottle)*