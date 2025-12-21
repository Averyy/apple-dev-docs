# TCButton

**Framework**: Touch Controller  
**Kind**: class

A control that represents a single on-screen button.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
class TCButton
```

#### Overview

This is mirrored by a [`GCControllerButtonInput`](https://developer.apple.com/documentation/GameController/GCControllerButtonInput) on the associated [`GCController`](https://developer.apple.com/documentation/GameController/GCController).

## Topics

### Inspecting a button
- [var contents: TCControlContents?](tcbutton/contents.md)
  The contents for the button in its normal state.
- [var highlightDuration: TimeInterval](tcbutton/highlightduration.md)
  The time it takes for a highlight to fade away, in seconds.
### Getting the collider shape
- [var colliderShape: TCColliderShape](tcbutton/collidershape.md)
  The collider shape for the button.
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
- [class TCDirectionPad](tcdirectionpad.md)
  An object that represents a direction pad.
- [class TCSwitch](tcswitch.md)
  A control that represents a single on-screen switch.
- [class TCThumbstick](tcthumbstick.md)
  Represents a single on-screen thumbstick.
- [class TCThrottle](tcthrottle.md)
  Represents a single on-screen throttle - a one axis input.
- [class TCTouchpad](tctouchpad.md)
  Represents a single on-screen touchpad that reports absolute coordinates or delta movements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tcbutton)*