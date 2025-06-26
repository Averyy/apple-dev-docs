# TCDirectionPad

**Framework**: Touch Controller  
**Kind**: class

An object that represents a direction pad.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
class TCDirectionPad
```

#### Overview

You can configure this object to behave as either a composite direction pad (mirrored by a `GCControllerDirectionPad` on the associated `GCController` instance) or as four separate buttons.

## Topics

### Inspecting the direction pad
- [var collider: any TCCollider](tcdirectionpad/collider.md)
  The collider for the direction pad.
- [var compositeLabel: TCControlLabel?](tcdirectionpad/compositelabel.md)
  A composite control label.
- [var downLabel: TCControlLabel?](tcdirectionpad/downlabel.md)
  The label for the down button, if the control isn’t a composite direction pad.
- [var downVisuals: TCControlVisuals?](tcdirectionpad/downvisuals.md)
  The visuals for the down button.
- [var hasMutuallyExclusiveInput: Bool](tcdirectionpad/hasmutuallyexclusiveinput.md)
  A Boolean value that indicates whether the control has mutally exclusive input.
- [var highlightTime: simd_float1](tcdirectionpad/highlighttime.md)
  The time it takes for a highlight to fade away, in seconds.
- [var isDigital: Bool](tcdirectionpad/isdigital.md)
  A Boolean value that indicates whether the control behaves as a digital button.
- [var isRadial: Bool](tcdirectionpad/isradial.md)
  A Boolean value that indicates whether the control behaves as a swipeable radial button.
- [var layer: simd_int1](tcdirectionpad/layer.md)
  The layer of the direction pad, used for z-sorting.
- [var leftLabel: TCControlLabel?](tcdirectionpad/leftlabel.md)
  The label for the left button, if the control isn’t a composite direction pad.
- [var leftVisuals: TCControlVisuals?](tcdirectionpad/leftvisuals.md)
  The visuals for the left button.
- [var offset: CGPoint](tcdirectionpad/offset.md)
  The control’s offset from the anchor, which determines its position.
- [var position: CGPoint](tcdirectionpad/position.md)
  The position of the direction pad in points, with the origin at the top left corner of the screen.
- [var rightLabel: TCControlLabel?](tcdirectionpad/rightlabel.md)
  The label for the right button, if the control isn’t a composite direction pad.
- [var rightVisuals: TCControlVisuals?](tcdirectionpad/rightvisuals.md)
  The visuals for the right button.
- [var size: CGSize](tcdirectionpad/size.md)
  The size (width, height) of the direction pad in points.
- [var touchController: TCTouchController](tcdirectionpad/touchcontroller.md)
  The touch controller that manages this direction pad.
- [var upLabel: TCControlLabel?](tcdirectionpad/uplabel.md)
  The label for the up button, if the control isn’t a composite direction pad.
- [var upVisuals: TCControlVisuals?](tcdirectionpad/upvisuals.md)
  The visuals for the up button.
### Getting the anchor
- [var anchor: TCTransformAnchor](tcdirectionpad/anchor.md)
  The anchor point that the direction pad’s offset is relative to.
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
- [class TCThumbstick](tcthumbstick.md)
  Represents a single on-screen thumbstick.
- [class TCThrottle](tcthrottle.md)
  Represents a single on-screen throttle - a one axis input.
- [class TCTouchpad](tctouchpad.md)
  Represents a single on-screen touchpad that reports absolute coordinates or delta movements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tcdirectionpad)*