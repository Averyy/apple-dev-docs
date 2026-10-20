# handSkeleton

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

The current position and orientation of joints on a hand.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
var handSkeleton: HandSkeleton? { get }
```

## See Also

### Getting hand information
- [var originFromAnchorTransform: simd_float4x4](./originfromanchortransform.md)
  The location and orientation of a hand in world space.
- [var chirality: HandAnchor.Chirality](./chirality-swift.property.md)
  The chirality of this hand.
- [HandAnchor.Chirality](./chirality-swift.enum.md)
  A value that indicates a left or right hand.
- [var isTracked: Bool](./istracked.md)
  A Boolean value that indicates whether ARKit is currently tracking this hand.
- [var description: String](./description.md)
  A textual representation of this anchor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/handanchor/handskeleton)*