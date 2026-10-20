# TCSwitch

**Framework**: Touch Controller  
**Kind**: class  
**Role**: Class

A control that represents a single on-screen switch.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
class TCSwitch
```

```objc
@interface TCSwitch : NSObject
```

#### Overview

This is mirrored by a [`GCControllerButtonInput`](../GameController/gccontrollerbuttoninput.md) on the associated [`GCController`](../GameController/gccontroller.md).

## Topics

### Inspecting the switch
- [var contents: TCControlContents?](./tcswitch/contents.md)
  The contents for the switch in its normal state.
- [var highlightDuration: TimeInterval](./tcswitch/highlightduration.md)
  The time it takes for a highlight to fade away, in seconds.
- [var isSwitchedOn: Bool](./tcswitch/isswitchedon.md)
  A Boolean value that indicates whether the switch is currently switched on.
- [var switchedOnContents: TCControlContents?](./tcswitch/switchedoncontents.md)
  The contents for the switch when it is switched on.
### Getting the collider shape
- [var colliderShape: TCColliderShape](./tcswitch/collidershape.md)
  The collider shape for the switch.
- [enum TCColliderShape](./tccollidershape.md)
  Defines the shape of a control collider.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [TCControl](./tccontrol.md)
- [TCControlLayout](./tccontrollayout.md)

## See Also

### Controls
- [protocol TCControl](./tccontrol.md)
  A protocol that defines the base properties and methods for all touch controls.
- [class TCButton](./tcbutton.md)
  A control that represents a single on-screen button.
- [class TCDirectionPad](./tcdirectionpad.md)
  An object that represents a direction pad.
- [class TCThumbstick](./tcthumbstick.md)
  Represents a single on-screen thumbstick.
- [class TCThrottle](./tcthrottle.md)
  Represents a single on-screen throttle - a one axis input.
- [class TCTouchpad](./tctouchpad.md)
  Represents a single on-screen touchpad that reports absolute coordinates or delta movements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tcswitch)*