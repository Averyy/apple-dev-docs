# ClothCapsuleShape

**Framework**: RealityKit  
**Kind**: struct

Shape representing a capsule (full height is `height + 2 * radius`).

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct ClothCapsuleShape
```

## Topics

### Creating a capsule shape
- [init(height: Float, radius: Float)](clothcapsuleshape/init(height:radius:).md)
  Creates a capsule shape with the given height and radius.
### Instance Properties
- [var height: Float](clothcapsuleshape/height.md)
  The length of the cylinder portion of the capsule.
- [var radius: Float](clothcapsuleshape/radius.md)
  The radius of the cylinder portion and the radius of each hemisphere.

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
- [struct ClothRoundedBoxShape](clothroundedboxshape.md)
  Shape representing a box with rounded edges.
- [struct ClothSphereShape](clothsphereshape.md)
  Shape representing a sphere.
- [enum ClothVolumeShape](clothvolumeshape.md)
  Shape suitable for use as a volume.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothcapsuleshape)*