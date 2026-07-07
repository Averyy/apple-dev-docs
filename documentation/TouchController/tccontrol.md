# TCControl

**Framework**: Touch Controller  
**Kind**: protocol

A protocol that defines the base properties and methods for all touch controls.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
protocol TCControl : TCControlLayout
```

## Topics

### Inspecting a control
- [var isEnabled: Bool](tccontrol/isenabled.md)
  A Boolean value that indicates whether the control is enabled.
- [var highlightDuration: TimeInterval](tccontrol/highlightduration.md)
  The duration of the highlight animation.
- [var label: TCControlLabel](tccontrol/label.md)
  The label associated with the control.
- [class TCControlLabel](tccontrollabel.md)
  A label you associate with a touch control and provides a semantic description.
- [var isPressed: Bool](tccontrol/ispressed.md)
  Indicates whether the control is currently pressed.
### Handling touches
- [func handleTouchBegan(at: CGPoint)](tccontrol/handletouchbegan(at:).md)
  Handles a touch began event at the specified point.
- [func handleTouchMoved(at: CGPoint)](tccontrol/handletouchmoved(at:).md)
  Handles a touch moved event at the specified point.
- [func handleTouchEnded(at: CGPoint)](tccontrol/handletouchended(at:).md)
  Handles a touch ended event at the specified point.
### Getting the collider shape
- [var colliderShape: TCColliderShape](tccontrol/collidershape.md)
  The collider shape for the control.
- [enum TCColliderShape](tccollidershape.md)
  Defines the shape of a control collider.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [TCControlLayout](tccontrollayout.md)
### Conforming Types
- [TCButton](tcbutton.md)
- [TCDirectionPad](tcdirectionpad.md)
- [TCSwitch](tcswitch.md)
- [TCThrottle](tcthrottle.md)
- [TCThumbstick](tcthumbstick.md)
- [TCTouchpad](tctouchpad.md)

## See Also

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
- [class TCTouchpad](tctouchpad.md)
  Represents a single on-screen touchpad that reports absolute coordinates or delta movements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tccontrol)*