# ClothForceVolumeComponent

**Framework**: RealityKit  
**Kind**: struct

A component that creates a force volume applying forces to any intersecting cloth body particles.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct ClothForceVolumeComponent
```

## Topics

### Creating a force volume
- [init(shape: ClothVolumeShape)](clothforcevolumecomponent/init(shape:).md)
  Creates a cloth force volume component with the given shape.
### Applying forces
- [var windForce: SIMD3<Float>](clothforcevolumecomponent/windforce.md)
  The wind force applied to particles inside the volume.
- [var constantForce: SIMD3<Float>](clothforcevolumecomponent/constantforce.md)
  The constant force applied to particles inside the volume.
### Shaping the volume
- [var shape: ClothVolumeShape](clothforcevolumecomponent/shape.md)
  The shape of the volume.
- [var falloffStart: Float](clothforcevolumecomponent/falloffstart.md)
  The depth (in meters) inside the volume at which the total force starts to linearly fall off.
### Adding force noise
- [var noiseAmplitude: Float](clothforcevolumecomponent/noiseamplitude.md)
  The amplitude of the noise applied to particles inside the volume.
- [var noiseFrequency: Float](clothforcevolumecomponent/noisefrequency.md)
  The frequency of the noise applied to particles inside the volume.

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
- [struct ClothQueryVolumeComponent](clothqueryvolumecomponent.md)
  A component that defines a volume for querying particles of cloth bodies.
- [struct ClothCoordinateSpace](clothcoordinatespace.md)
  Defines a reference frame within a cloth simulation.
- [struct PerClothVertexData](perclothvertexdata.md)
  A generic type that stores per-vertex data in a buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothforcevolumecomponent)*