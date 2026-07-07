# ClothRoundedBoxShape

**Framework**: RealityKit  
**Kind**: struct

Shape representing a box with rounded edges.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct ClothRoundedBoxShape
```

## Topics

### Creating a rounded box shape
- [init(size: SIMD3<Float>, edgeRadius: Float)](clothroundedboxshape/init(size:edgeradius:).md)
  Creates a rounded box shape with the given size and edge radius.
### Configuring the geometry
- [var size: SIMD3<Float>](clothroundedboxshape/size.md)
  The size of the box along each axis.
- [var edgeRadius: Float](clothroundedboxshape/edgeradius.md)
  The radius of the rounded edges.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct ClothMeshShape](clothmeshshape.md)
  Shape representing a mesh with a configurable inflation bias.
- [struct ClothPlaneShape](clothplaneshape.md)
  Shape representing an infinite plane that encloses one half of the world.
- [struct ClothBoxShape](clothboxshape.md)
  Shape representing a box.
- [struct ClothSphereShape](clothsphereshape.md)
  Shape representing a sphere.
- [struct ClothCapsuleShape](clothcapsuleshape.md)
  Shape representing a capsule (full height is `height + 2 * radius`).
- [enum ClothVolumeShape](clothvolumeshape.md)
  Shape suitable for use as a volume.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothroundedboxshape)*