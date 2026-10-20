# HandAnchor.Chirality

**Framework**: ARKit  
**Kind**: enum  
**Role**: Enumeration

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
- [HandAnchor.Chirality.left](./chirality-swift.enum/left.md)
  A left hand.
- [HandAnchor.Chirality.right](./chirality-swift.enum/right.md)
  A right hand.
### Instance Properties
- [var description: String](./chirality-swift.enum/description.md)
  A textual representation of HandAnchor.Chirality.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Copyable](../../Swift/copyable.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting hand information
- [var originFromAnchorTransform: simd_float4x4](./originfromanchortransform.md)
  The location and orientation of a hand in world space.
- [var handSkeleton: HandSkeleton?](./handskeleton.md)
  The current position and orientation of joints on a hand.
- [var chirality: HandAnchor.Chirality](./chirality-swift.property.md)
  The chirality of this hand.
- [var isTracked: Bool](./istracked.md)
  A Boolean value that indicates whether ARKit is currently tracking this hand.
- [var description: String](./description.md)
  A textual representation of this anchor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/handanchor/chirality-swift.enum)*