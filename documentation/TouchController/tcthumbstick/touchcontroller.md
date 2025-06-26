# touchController

**Framework**: Touch Controller  
**Kind**: property

The touch controller that manages this thumbstick.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var touchController: TCTouchController { get }
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tcthumbstick/touchcontroller)*