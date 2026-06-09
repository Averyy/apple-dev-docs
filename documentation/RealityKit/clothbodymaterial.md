# ClothBodyMaterial

**Framework**: RealityKit  
**Kind**: struct

A struct that represents a cloth body’s material.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct ClothBodyMaterial
```

## Topics

### Configuring stiffness and damping
- [var springStiffness: Float](clothbodymaterial/springstiffness.md)
  The resistance to compressing and stretching between adjacent particles.
- [var bendStiffness: Float](clothbodymaterial/bendstiffness.md)
  The resistance to bending between adjacent triangles.
- [var crossTetherStiffness: Float](clothbodymaterial/crosstetherstiffness.md)
  The resistance to shearing between opposing vertices.
- [var laplacianDamping: Float](clothbodymaterial/laplaciandamping.md)
  Damping applied to the velocities of the particles, based on the velocities of their connecting particles.
### Configuring friction
- [var staticFriction: Float](clothbodymaterial/staticfriction.md)
  The friction a cloth body particle experiences when in contact with another particle or collider with no relative motion.
- [var kineticFriction: Float](clothbodymaterial/kineticfriction.md)
  The friction a cloth body particle experiences when in contact with another particle or collider with relative motion.
### Initializers
- [init()](clothbodymaterial/init.md)
  Creates a new material for cloth bodies.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct ClothSimulationComponent](clothsimulationcomponent.md)
  A component that marks an entity as the simulation root of a localized cloth simulation.
- [struct ClothBodyComponent](clothbodycomponent.md)
  A component that simulates an entity as a deformable cloth body, when part of a cloth simulation.
- [struct ClothGrabComponent](clothgrabcomponent.md)
  A component that grabs and drags particles of cloth bodies using either a ray or a volume, as determined by the `mode` property.
- [struct ClothForceVolumeComponent](clothforcevolumecomponent.md)
  A component that creates a force volume applying forces to any intersecting cloth body particles.
- [struct ClothQueryVolumeComponent](clothqueryvolumecomponent.md)
  A component that defines a volume for querying particles of cloth bodies.
- [struct ClothCoordinateSpace](clothcoordinatespace.md)
  Defines a reference frame within a cloth simulation.
- [struct PerClothVertexData](perclothvertexdata.md)
  A generic type that stores per-vertex data in a buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothbodymaterial)*