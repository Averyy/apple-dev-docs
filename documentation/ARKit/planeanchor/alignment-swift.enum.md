# PlaneAnchor.Alignment

**Framework**: ARKit  
**Kind**: enum  
**Role**: Enumeration

The possible general orientations of a detected plane with respect to gravity.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
enum Alignment
```

## Topics

### Alignment Values
- [PlaneAnchor.Alignment.horizontal](./alignment-swift.enum/horizontal.md)
  The plane is in a horizontal orientation.
- [PlaneAnchor.Alignment.vertical](./alignment-swift.enum/vertical.md)
  The plane is in a vertical orientation.
- [PlaneAnchor.Alignment.slanted](./alignment-swift.enum/slanted.md)
  The plane is in a slanted orientation.
### Instance Properties
- [var description: String](./alignment-swift.enum/description.md)
  A textual representation of PlaneAnchor.Alignment

## Relationships

### Conforms To
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Inspecting a plane anchor
- [var originFromAnchorTransform: simd_float4x4](./originfromanchortransform.md)
  The location and orientation of a plane in world space.
- [var alignment: PlaneAnchor.Alignment](./alignment-swift.property.md)
  The general orientation of the detected plane with respect to gravity.
- [var surfaceClassification: SurfaceClassification](./surfaceclassification.md)
  Get the surface classification of this plane.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/planeanchor/alignment-swift.enum)*