# touchController

**Framework**: Touch Controller  
**Kind**: property

The touch controller that manages this touchpad.

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
- [var visuals: TCControlVisuals?](tctouchpad/visuals.md)
  The visuals for the touchpad. May be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tctouchpad/touchcontroller)*