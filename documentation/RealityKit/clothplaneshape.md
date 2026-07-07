# ClothPlaneShape

**Framework**: RealityKit  
**Kind**: struct

Shape representing an infinite plane that encloses one half of the world.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct ClothPlaneShape
```

#### Overview

The plane passes through the entity’s origin with the given `normal`. Everything on the side opposite the normal (including the plane itself) is considered inside the shape.

## Topics

### Creating a plane shape
- [init(normal: SIMD3<Float>, bias: Float)](clothplaneshape/init(normal:bias:).md)
  Creates a plane shape with the given normal and surface displacement.
### Configuring the plane
- [var bias: Float](clothplaneshape/bias.md)
  The distance by which the surface of the plane shape is displaced along the direction of its normal.
### Instance Properties
- [var normal: SIMD3<Float>](clothplaneshape/normal.md)
  The normal vector determining the orientation of the plane.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct ClothMeshShape](clothmeshshape.md)
  Shape representing a mesh with a configurable inflation bias.
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

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothplaneshape)*