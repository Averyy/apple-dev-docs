# TCButton

**Framework**: Touch Controls  
**Kind**: class

A control that represents a single on-screen button.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
class TCButton
```

#### Overview

This is mirrored by a [`GCControllerButtonInput`](https://developer.apple.com/documentation/GameController/GCControllerButtonInput) on the associated [`GCController`](https://developer.apple.com/documentation/GameController/GCController).

## Topics

### Instance Properties
- [var anchor: TCTransformAnchor](tcbutton/anchor.md)
  The anchor point that the control’s offset is relative to.
- [var collider: any TCCollider](tcbutton/collider.md)
  The collider for the button.
- [var highlightTime: simd_float1](tcbutton/highlighttime.md)
  The time it takes for a highlight to fade away, in seconds.
- [var isToggle: Bool](tcbutton/istoggle.md)
  A Boolean value that indicates whether the button is a toggle button.
- [var layer: simd_int1](tcbutton/layer.md)
  The layer of the button, used for z-sorting.
- [var offset: CGPoint](tcbutton/offset.md)
  The control’s offset from the anchor, which determines its position.
- [var position: CGPoint](tcbutton/position.md)
  The position of the button in points, with the origin at the top left corner of the screen.
- [var size: CGSize](tcbutton/size.md)
  The size (width, height) of the button in points.
- [var toggleVisuals: TCControlVisuals?](tcbutton/togglevisuals.md)
  The visuals for the button when it is toggled on.
- [var touchController: TCTouchController](tcbutton/touchcontroller.md)
  The touch controller that manages this button.
- [var visuals: TCControlVisuals?](tcbutton/visuals.md)
  The visuals for the button in its normal state.

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
- [class TCDirectionPad](tcdirectionpad.md)
  An object that represents a direction pad.
- [class TCThumbstick](tcthumbstick.md)
  Represents a single on-screen thumbstick.
- [class TCThrottle](tcthrottle.md)
  Represents a single on-screen throttle - a one axis input.
- [class TCTouchpad](tctouchpad.md)
  Represents a single on-screen touchpad that reports absolute coordinates or delta movements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontrols/tcbutton)*