# TCTouchpad

**Framework**: Touch Controller  
**Kind**: class

Represents a single on-screen touchpad that reports absolute coordinates or delta movements.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
class TCTouchpad
```

#### Overview

This is mirrored by a `GCControllerDirectionPad` on the associated `GCController` instance.

## Topics

### Inspecting at touchpad
- [var contents: TCControlContents?](tctouchpad/contents.md)
  The contents for the touchpad. May be `nil`.
- [var highlightDuration: TimeInterval](tctouchpad/highlightduration.md)
  The time it takes for a highlight to fade away, in seconds.
- [var reportsRelativeValues: Bool](tctouchpad/reportsrelativevalues.md)
  A Boolean value that represents the touchpad reports deltas.
### Getting the collider shape
- [var colliderShape: TCColliderShape](tctouchpad/collidershape.md)
  The collider shape for the touchpad.
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
- [class TCThrottle](tcthrottle.md)
  Represents a single on-screen throttle - a one axis input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tctouchpad)*