# TCThumbstick

**Framework**: Touch Controller  
**Kind**: class

Represents a single on-screen thumbstick.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
class TCThumbstick
```

#### Overview

This is mirrored by a `GCControllerDirectionPad` on the associated `GCController` instance.

## Topics

### Inspecting a thumbstick
- [var backgroundContents: TCControlContents?](tcthumbstick/backgroundcontents.md)
  The contents for the background of the thumbstick.
- [var hidesWhenNotPressed: Bool](tcthumbstick/hideswhennotpressed.md)
  A Boolean value that indicates whether to hide the thumbstick when it is not being pressed.
- [var highlightDuration: TimeInterval](tcthumbstick/highlightduration.md)
  The time it takes for a highlight to fade away, in seconds.
- [var stickContents: TCControlContents?](tcthumbstick/stickcontents.md)
  The contents for the thumbstick itself.
- [var stickSize: CGSize](tcthumbstick/sticksize.md)
  The size (width, height) of the thumbstick stick itself in points.
### Getting the collider shape
- [var colliderShape: TCColliderShape](tcthumbstick/collidershape.md)
  The collider shape for the thumbstick.
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
- [class TCThrottle](tcthrottle.md)
  Represents a single on-screen throttle - a one axis input.
- [class TCTouchpad](tctouchpad.md)
  Represents a single on-screen touchpad that reports absolute coordinates or delta movements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tcthumbstick)*