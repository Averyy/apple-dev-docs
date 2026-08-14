# ClothVolumeShape

**Framework**: RealityKit  
**Kind**: enum

Shape suitable for use as a volume.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
enum ClothVolumeShape
```

## Topics

### Specifying the volume shape
- [ClothVolumeShape.box(_:)](clothvolumeshape/box(_:).md)
  A box volume shape.
- [case roundedBox(ClothRoundedBoxShape)](clothvolumeshape/roundedbox(_:).md)
  A rounded box volume shape.
- [case sphere(ClothSphereShape)](clothvolumeshape/sphere(_:).md)
  A sphere volume shape.
- [case capsule(ClothCapsuleShape)](clothvolumeshape/capsule(_:).md)
  A capsule volume shape.
- [case plane(ClothPlaneShape)](clothvolumeshape/plane(_:).md)
  A plane volume shape.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct ClothMeshShape](clothmeshshape.md)
  Shape representing a mesh with a configurable inflation bias.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothvolumeshape)*