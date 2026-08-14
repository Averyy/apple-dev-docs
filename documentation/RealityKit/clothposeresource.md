# ClothPoseResource

**Framework**: RealityKit  
**Kind**: class

A resource that defines a set of vertex positions for a cloth body.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final class ClothPoseResource
```

#### Overview

A pose resource provides an alternate set of positions for the vertices of a [`ClothMeshResource`](clothmeshresource.md); the topology is still determined by the mesh resource. One common use is to specify an already-draped starting configuration via [`initialMeshDraping`](clothbodycomponent/initialmeshdraping.md).

## Topics

### Creating a pose resource
- [convenience init(positions: [SIMD3<Float>]) throws](clothposeresource/init(positions:).md)
  Creates a cloth pose resource with the given vertex positions.
### Accessing pose positions
- [func withPositions<Result>((Span<SIMD3<Float>>) -> Result) -> Result](clothposeresource/withpositions(_:).md)
  Provides access to the positions of all the vertices within a callback.
- [func position(at: UInt32) -> SIMD3<Float>](clothposeresource/position(at:).md)
  Returns the position of the vertex at the given index.
- [var vertexCount: Int](clothposeresource/vertexcount.md)
  The number of vertices in the pose resource.

## Relationships

### Conforms To
- [Resource](resource.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class ClothMeshResource](clothmeshresource.md)
  A mesh resource that defines the topology and shape of a cloth body or a mesh-shaped cloth collider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothposeresource)*