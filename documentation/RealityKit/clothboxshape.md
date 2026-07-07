# ClothBoxShape

**Framework**: RealityKit  
**Kind**: struct

Shape representing a box.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct ClothBoxShape
```

## Topics

### Creating a box shape
- [init(size: SIMD3<Float>)](clothboxshape/init(size:).md)
  Creates a box shape with the given size.
### Accessing the dimensions
- [var size: SIMD3<Float>](clothboxshape/size.md)
  The size of the box along each axis.

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
- [struct ClothRoundedBoxShape](clothroundedboxshape.md)
  Shape representing a box with rounded edges.
- [struct ClothSphereShape](clothsphereshape.md)
  Shape representing a sphere.
- [struct ClothCapsuleShape](clothcapsuleshape.md)
  Shape representing a capsule (full height is `height + 2 * radius`).
- [enum ClothVolumeShape](clothvolumeshape.md)
  Shape suitable for use as a volume.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothboxshape)*