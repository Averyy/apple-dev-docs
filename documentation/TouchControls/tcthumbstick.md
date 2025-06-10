# TCThumbstick

**Framework**: Touch Controls  
**Kind**: class

Represents a single on-screen thumbstick.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
class TCThumbstick
```

#### Overview

This is mirrored by a `GCControllerDirectionPad` on the associated `GCController` instance.

## Topics

### Instance Properties
- [var anchor: TCTransformAnchor](tcthumbstick/anchor.md)
  The anchor point that the thumbstick’s offset is relative to.
- [var backgroundVisuals: TCControlVisuals?](tcthumbstick/backgroundvisuals.md)
  The visuals for the background of the thumbstick.
- [var collider: any TCCollider](tcthumbstick/collider.md)
  The collider for the thumbstick.
- [var hideWhenNotPressed: Bool](tcthumbstick/hidewhennotpressed.md)
  A Boolean value that indicates whether to hide the thumbstick when it is not being pressed.
- [var highlightTime: simd_float1](tcthumbstick/highlighttime.md)
  The time it takes for a highlight to fade away, in seconds.
- [var layer: simd_int1](tcthumbstick/layer.md)
  The layer of the thumbstick, used for z-sorting.
- [var offset: CGPoint](tcthumbstick/offset.md)
  The control’s offset from the anchor, which determines its position.
- [var position: CGPoint](tcthumbstick/position.md)
  The position of the thumbstick in points, with the origin at the top left corner of the screen.
- [var size: CGSize](tcthumbstick/size.md)
  The size (width, height) of the thumbstick in points.
- [var stickSize: CGSize](tcthumbstick/sticksize.md)
  The size (width, height) of the thumbstick stick itself in points.
- [var stickVisuals: TCControlVisuals?](tcthumbstick/stickvisuals.md)
  The visuals for the thumbstick itself.
- [var touchController: TCTouchController](tcthumbstick/touchcontroller.md)
  The touch controller that manages this thumbstick.

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
- [class TCThrottle](tcthrottle.md)
  Represents a single on-screen throttle - a one axis input.
- [class TCTouchpad](tctouchpad.md)
  Represents a single on-screen touchpad that reports absolute coordinates or delta movements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontrols/tcthumbstick)*