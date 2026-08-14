# ClothMeshShape

**Framework**: RealityKit  
**Kind**: struct

Shape representing a mesh with a configurable inflation bias.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct ClothMeshShape
```

## Topics

### Creating a cloth mesh shape
- [init(mesh: ClothMeshResource, bias: Float)](clothmeshshape/init(mesh:bias:).md)
  Creates a mesh shape from the given mesh resource and inflation bias.
### Configuring the mesh shape
- [var mesh: ClothMeshResource](clothmeshshape/mesh.md)
  The mesh resource that this shape is based off.
- [var bias: Float](clothmeshshape/bias.md)
  The distance by which the vertices are extended outwards along the direction of their normals.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct ClothPlaneShape](clothplaneshape.md)
  Shape representing an infinite plane that encloses one half of the world.
- [struct ClothBoxShape](clothboxshape.md)
  Shape representing a box.
- [struct ClothRoundedBoxShape](clothroundedboxshape.md)
  Shape representing a box with rounded edges.
- [struct ClothSphereShape](clothsphereshape.md)
  Shape representing a sphere.
- [struct ClothCapsuleShape](clothcapsuleshape.md)
  Shape representing a capsule (full height is `height + 2 * radius`).
- [enum ClothVolumeShape](clothvolumeshape.md)
  Shape suitable for use as a volume.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothmeshshape)*