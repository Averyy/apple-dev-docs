# reportsDeltas

**Framework**: Touch Controller  
**Kind**: property

A Boolean value that represents the touchpad reports deltas.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var reportsDeltas: Bool { get set }
```

#### Discussion

If `YES`, the touchpad will report delta values as touch moves instead of absolute positions.

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
- [var size: CGSize](tctouchpaddescriptor/size.md)
  The size (width, height) of the touchpad in points.
- [var visuals: TCControlVisuals?](tctouchpaddescriptor/visuals.md)
  The visuals for the touchpad.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tctouchpaddescriptor/reportsdeltas)*