# TCTouchpad

**Framework**: Touch Controller  
**Kind**: class

Represents a single on-screen touchpad that reports absolute coordinates or delta movements.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
class TCTouchpad
```

#### Overview

This is mirrored by a `GCControllerDirectionPad` on the associated `GCController` instance.

## Topics

### Inspecting at touchpad
- [var collider: any TCCollider](tctouchpad/collider.md)
  The collider for the touchpad.
- [var highlightTime: simd_float1](tctouchpad/highlighttime.md)
  The time it takes for a highlight to fade away, in seconds.
- [var layer: simd_int1](tctouchpad/layer.md)
  The layer of the touchpad, used for z-sorting.
- [var offset: CGPoint](tctouchpad/offset.md)
  The control’s offset from the anchor, which determines its position.
- [var position: CGPoint](tctouchpad/position.md)
  The position of the touchpad in points, with the origin at the top left corner of the screen.
- [var reportsDeltas: Bool](tctouchpad/reportsdeltas.md)
  A Boolean value that represents the touchpad reports deltas.
- [var size: CGSize](tctouchpad/size.md)
  The width and height of the touchpad. in points.
- [var touchController: TCTouchController](tctouchpad/touchcontroller.md)
  The touch controller that manages this touchpad.
- [var visuals: TCControlVisuals?](tctouchpad/visuals.md)
  The visuals for the touchpad. May be `nil`.
### Getting the anchor
- [var anchor: TCTransformAnchor](tctouchpad/anchor.md)
  The anchor point that the touchpad’s offset is relative to.
- [enum TCTransformAnchor](tctransformanchor.md)
  Defines the anchor point for a transform.

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
- [class TCThumbstick](tcthumbstick.md)
  Represents a single on-screen thumbstick.
- [class TCThrottle](tcthrottle.md)
  Represents a single on-screen throttle - a one axis input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tctouchpad)*