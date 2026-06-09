# ClothQueryVolumeComponent

**Framework**: RealityKit  
**Kind**: struct

A component that defines a volume for querying particles of cloth bodies.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct ClothQueryVolumeComponent
```

## Topics

### Creating a query volume
- [init(shape: ClothVolumeShape)](clothqueryvolumecomponent/init(shape:).md)
  Creates a cloth query volume component with the given shape.
### Configuring the volume shape
- [var shape: ClothVolumeShape](clothqueryvolumecomponent/shape.md)
  The shape of the volume.
### Accessing query results
- [var queryEntities: [Entity]](clothqueryvolumecomponent/queryentities.md)
  The entities to query for intersections with the volume.

## Relationships

### Conforms To
- [Component](component.md)

## See Also

- [struct ClothSimulationComponent](clothsimulationcomponent.md)
  A component that marks an entity as the simulation root of a localized cloth simulation.
- [struct ClothBodyComponent](clothbodycomponent.md)
  A component that simulates an entity as a deformable cloth body, when part of a cloth simulation.
- [struct ClothBodyMaterial](clothbodymaterial.md)
  A struct that represents a cloth body’s material.
- [struct ClothGrabComponent](clothgrabcomponent.md)
  A component that grabs and drags particles of cloth bodies using either a ray or a volume, as determined by the `mode` property.
- [struct ClothForceVolumeComponent](clothforcevolumecomponent.md)
  A component that creates a force volume applying forces to any intersecting cloth body particles.
- [struct ClothCoordinateSpace](clothcoordinatespace.md)
  Defines a reference frame within a cloth simulation.
- [struct PerClothVertexData](perclothvertexdata.md)
  A generic type that stores per-vertex data in a buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothqueryvolumecomponent)*