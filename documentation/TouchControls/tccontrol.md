# TCControl

**Framework**: Touch Controls  
**Kind**: protocol

A protocol that defines the base properties and methods for all touch controls.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
protocol TCControl : TCTransform
```

## Topics

### Instance Properties
- [var collider: any TCCollider](tccontrol/collider.md)
  The collider for the control.
- [var enabled: Bool](tccontrol/enabled.md)
  A Boolean value that indicates whether the control is enabled.
- [var highlightFactor: Float](tccontrol/highlightfactor.md)
  The factor by which to highlight the control when pressed.
- [var highlightTime: simd_float1](tccontrol/highlighttime.md)
  The duration of the highlight animation.
- [var label: TCControlLabel](tccontrol/label.md)
  The label associated with the control.
- [var pressed: Bool](tccontrol/pressed.md)
  Indicates whether the control is currently pressed.
### Instance Methods
- [func handleTouchBegan(at: CGPoint)](tccontrol/handletouchbegan(at:).md)
  Handles a touch began event at the specified point.
- [func handleTouchEnded(at: CGPoint)](tccontrol/handletouchended(at:).md)
  Handles a touch ended event at the specified point.
- [func handleTouchMoved(at: CGPoint)](tccontrol/handletouchmoved(at:).md)
  Handles a touch moved event at the specified point.
- [func layoutIfNeeded()](tccontrol/layoutifneeded.md)
  Updates the layout of the control.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [TCTransform](tctransform.md)
### Conforming Types
- [TCButton](tcbutton.md)
- [TCDirectionPad](tcdirectionpad.md)
- [TCThrottle](tcthrottle.md)
- [TCThumbstick](tcthumbstick.md)
- [TCTouchpad](tctouchpad.md)

## See Also

- [class TCButton](tcbutton.md)
  A control that represents a single on-screen button.
- [class TCDirectionPad](tcdirectionpad.md)
  An object that represents a direction pad.
- [class TCThumbstick](tcthumbstick.md)
  Represents a single on-screen thumbstick.
- [class TCThrottle](tcthrottle.md)
  Represents a single on-screen throttle - a one axis input.
- [class TCTouchpad](tctouchpad.md)
  Represents a single on-screen touchpad that reports absolute coordinates or delta movements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontrols/tccontrol)*