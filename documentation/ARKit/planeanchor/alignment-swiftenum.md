# PlaneAnchor.Alignment

**Framework**: ARKit  
**Kind**: enum

Values describing possible general orientations of a detected plane with respect to gravity.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
enum Alignment
```

## Topics

### Alignment Values
- [PlaneAnchor.Alignment.horizontal](planeanchor/alignment-swift.enum/horizontal.md)
  The plane is in a horizontal oriention.
- [PlaneAnchor.Alignment.vertical](planeanchor/alignment-swift.enum/vertical.md)
  The plane is in a vertical orientation.
### Enumeration Cases
- [PlaneAnchor.Alignment.slanted](planeanchor/alignment-swift.enum/slanted.md)
  The plane is in a slanted orientation.
### Instance Properties
- [var description: String](planeanchor/alignment-swift.enum/description.md)
  A textual representation of PlaneAnchor.Alignment

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var originFromAnchorTransform: simd_float4x4](planeanchor/originfromanchortransform.md)
  The location and orientation of a plane in world space.
- [var alignment: PlaneAnchor.Alignment](planeanchor/alignment-swift.property.md)
  The general orientation of the detected plane with respect to gravity.
- [var classification: PlaneAnchor.Classification](planeanchor/classification-swift.property.md)
  Get the classification of this plane.
- [PlaneAnchor.Classification](planeanchor/classification-swift.enum.md)
  The kinds of object classification a plane anchor can have.
- [var description: String](planeanchor/description.md)
  A textual representation of this anchor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/planeanchor/alignment-swift.enum)*