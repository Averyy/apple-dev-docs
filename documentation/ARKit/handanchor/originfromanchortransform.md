# originFromAnchorTransform

**Framework**: ARKit  
**Kind**: property

The location and orientation of a hand in world space.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
var originFromAnchorTransform: simd_float4x4 { get }
```

#### Discussion

The transform of a hand anchor is positioned at the base of the wrist. ARKit provides transforms of other joints on the hand relative to this root transform.

## See Also

- [var handSkeleton: HandSkeleton?](handanchor/handskeleton.md)
  The current position and orientation of joints on a hand.
- [var chirality: HandAnchor.Chirality](handanchor/chirality-swift.property.md)
  The chirality of this hand.
- [HandAnchor.Chirality](handanchor/chirality-swift.enum.md)
  A value that indicates a left or right hand.
- [var isTracked: Bool](handanchor/istracked.md)
  A Boolean value that indicates whether ARKit is currently tracking this hand.
- [var description: String](handanchor/description.md)
  A textual representation of this anchor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/handanchor/originfromanchortransform)*