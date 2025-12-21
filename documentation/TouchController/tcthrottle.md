# TCThrottle

**Framework**: Touch Controller  
**Kind**: class

Represents a single on-screen throttle - a one axis input.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
class TCThrottle
```

#### Overview

This is mirrored by a `GCControllerButtonInput` on the associated `GCController` instance.

## Topics

### Inspecting the throttle
- [var backgroundContents: TCControlContents?](tcthrottle/backgroundcontents.md)
  The contents for the background of the throttle.
- [var baseValue: CGFloat](tcthrottle/basevalue.md)
  The initial value of this control.
- [var highlightDuration: TimeInterval](tcthrottle/highlightduration.md)
  The time it takes for a highlight to fade away, in seconds.
- [var indicatorContents: TCControlContents?](tcthrottle/indicatorcontents.md)
  The contents for the indicator of the throttle.
- [var indicatorSize: CGSize](tcthrottle/indicatorsize.md)
  The size (width, height) of the indicator itself in points.
- [var snapsToBaseValue: Bool](tcthrottle/snapstobasevalue.md)
  A Boolean value that indicates whether the control reverts to it’s base value.
- [var throttleSize: CGSize](tcthrottle/throttlesize.md)
  The size (width, height) of the throttle itself, providing boundaries for the indicator, in points.
### Getting the collider shape
- [var colliderShape: TCColliderShape](tcthrottle/collidershape.md)
  The collider shape for the throttle.
- [enum TCColliderShape](tccollidershape.md)
  Defines the shape of a control collider.
### Getting the orientation
- [var orientation: TCThrottle.Orientation](tcthrottle/orientation-swift.property.md)
  The orientation of the throttle.
- [TCThrottle.Orientation](tcthrottle/orientation-swift.enum.md)
  Defines the orientation of the throttle.

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
- [TCControlLayout](tccontrollayout.md)

## See Also

- [protocol TCControl](tccontrol.md)
  A protocol that defines the base properties and methods for all touch controls.
- [class TCButton](tcbutton.md)
  A control that represents a single on-screen button.
- [class TCDirectionPad](tcdirectionpad.md)
  An object that represents a direction pad.
- [class TCSwitch](tcswitch.md)
  A control that represents a single on-screen switch.
- [class TCThumbstick](tcthumbstick.md)
  Represents a single on-screen thumbstick.
- [class TCTouchpad](tctouchpad.md)
  Represents a single on-screen touchpad that reports absolute coordinates or delta movements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tcthrottle)*