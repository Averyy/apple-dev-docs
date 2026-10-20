# isTracked

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether ARKit is currently tracking this hand.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
var isTracked: Bool { get }
```

## See Also

### Getting hand information
- [var originFromAnchorTransform: simd_float4x4](./originfromanchortransform.md)
  The location and orientation of a hand in world space.
- [var handSkeleton: HandSkeleton?](./handskeleton.md)
  The current position and orientation of joints on a hand.
- [var chirality: HandAnchor.Chirality](./chirality-swift.property.md)
  The chirality of this hand.
- [HandAnchor.Chirality](./chirality-swift.enum.md)
  A value that indicates a left or right hand.
- [var description: String](./description.md)
  A textual representation of this anchor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/handanchor/istracked)*