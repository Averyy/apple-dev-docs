# HandAnchor.Chirality

**Framework**: ARKit  
**Kind**: enum

A value that indicates a left or right hand.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
@frozen
enum Chirality
```

## Topics

### Getting hand chirality
- [HandAnchor.Chirality.left](handanchor/chirality-swift.enum/left.md)
  A left hand.
- [HandAnchor.Chirality.right](handanchor/chirality-swift.enum/right.md)
  A right hand.
### Instance Properties
- [var description: String](handanchor/chirality-swift.enum/description.md)
  A textual representation of HandAnchor.Chirality

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var originFromAnchorTransform: simd_float4x4](handanchor/originfromanchortransform.md)
  The location and orientation of a hand in world space.
- [var handSkeleton: HandSkeleton?](handanchor/handskeleton.md)
  The current position and orientation of joints on a hand.
- [var chirality: HandAnchor.Chirality](handanchor/chirality-swift.property.md)
  The chirality of this hand.
- [var isTracked: Bool](handanchor/istracked.md)
  A Boolean value that indicates whether ARKit is currently tracking this hand.
- [var description: String](handanchor/description.md)
  A textual representation of this anchor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/handanchor/chirality-swift.enum)*