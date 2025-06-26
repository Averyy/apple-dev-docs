# visuals

**Framework**: Touch Controller  
**Kind**: property

The visuals for the touchpad.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var visuals: TCControlVisuals? { get set }
```

#### Discussion

May be `nil`.

## See Also

- [var anchor: TCTransformAnchor](tctouchpaddescriptor/anchor.md)
  The anchor point that the touchpad’s offset is relative to.
- [var colliderType: TCColliderType](tctouchpaddescriptor/collidertype.md)
  The type of collider to use for the touchpad.
- [var highlightTime: simd_float1](tctouchpaddescriptor/highlighttime.md)
  The time it takes for a highlight to fade away, in seconds.
- [var label: TCControlLabel](tctouchpaddescriptor/label.md)
  The label associated with the touchpad.
- [var layer: simd_int1](tctouchpaddescriptor/layer.md)
  The layer of the touchpad, used for z-sorting.
- [var offset: CGPoint](tctouchpaddescriptor/offset.md)
  The control’s offset from the anchor, which determines its position.
- [var reportsDeltas: Bool](tctouchpaddescriptor/reportsdeltas.md)
  A Boolean value that represents the touchpad reports deltas.
- [var size: CGSize](tctouchpaddescriptor/size.md)
  The size (width, height) of the touchpad in points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tctouchpaddescriptor/visuals)*