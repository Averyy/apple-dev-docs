# TCDirectionPad

**Framework**: Touch Controller  
**Kind**: class

An object that represents a direction pad.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
class TCDirectionPad
```

#### Overview

You can configure this object to behave as either a composite direction pad (mirrored by a `GCControllerDirectionPad` on the associated `GCController` instance) or as four separate buttons.

## Topics

### Inspecting the direction pad
- [var compositeLabel: TCControlLabel?](tcdirectionpad/compositelabel.md)
  A composite control label.
- [var downContents: TCControlContents?](tcdirectionpad/downcontents.md)
  The contents for the down button.
- [var downLabel: TCControlLabel?](tcdirectionpad/downlabel.md)
  The label for the down button, if the control isn’t a composite direction pad.
- [var highlightDuration: TimeInterval](tcdirectionpad/highlightduration.md)
  The time it takes for a highlight to fade away, in seconds.
- [var inputIsMutuallyExclusive: Bool](tcdirectionpad/inputismutuallyexclusive.md)
  A Boolean value that indicates whether the control has mutally exclusive input.
- [var isDigital: Bool](tcdirectionpad/isdigital.md)
  A Boolean value that indicates whether the control behaves as a digital button.
- [var isRadial: Bool](tcdirectionpad/isradial.md)
  A Boolean value that indicates whether the control behaves as a swipeable radial button.
- [var leftContents: TCControlContents?](tcdirectionpad/leftcontents.md)
  The contents for the left button.
- [var leftLabel: TCControlLabel?](tcdirectionpad/leftlabel.md)
  The label for the left button, if the control isn’t a composite direction pad.
- [var rightContents: TCControlContents?](tcdirectionpad/rightcontents.md)
  The contents for the right button.
- [var rightLabel: TCControlLabel?](tcdirectionpad/rightlabel.md)
  The label for the right button, if the control isn’t a composite direction pad.
- [var upContents: TCControlContents?](tcdirectionpad/upcontents.md)
  The contents for the up button.
- [var upLabel: TCControlLabel?](tcdirectionpad/uplabel.md)
  The label for the up button, if the control isn’t a composite direction pad.
### Getting the collider shape
- [var colliderShape: TCColliderShape](tcdirectionpad/collidershape.md)
  The collider shape for the direction pad.
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
- [class TCSwitch](tcswitch.md)
  A control that represents a single on-screen switch.
- [class TCThumbstick](tcthumbstick.md)
  Represents a single on-screen thumbstick.
- [class TCThrottle](tcthrottle.md)
  Represents a single on-screen throttle - a one axis input.
- [class TCTouchpad](tctouchpad.md)
  Represents a single on-screen touchpad that reports absolute coordinates or delta movements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tcdirectionpad)*