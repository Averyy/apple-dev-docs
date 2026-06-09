# ClothGrabComponent

**Framework**: RealityKit  
**Kind**: struct

A component that grabs and drags particles of cloth bodies using either a ray or a volume, as determined by the `mode` property.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct ClothGrabComponent
```

#### Overview

When `isGrabbing` is first set to true, a selection is made using the ray/volume. While `isGrabbing` remains true, the selected particles will be dragged to the position determined by the ray/volume. When `isGrabbing` is set to false, any selected particles are released and will once again be controlled by the simulation.

To smoothen the motion of particles dragged using a volume, `falloff` can be set to `.enabled`. This causes the strength of the particle dragging to fall off based on the distance from the volume surface.

## Topics

### Creating a grab component
- [init(mode: ClothGrabComponent.GrabMode)](clothgrabcomponent/init(mode:).md)
  Creates a cloth grab component with the given grab mode.
- [ClothGrabComponent.GrabMode](clothgrabcomponent/grabmode.md)
  Defines whether a grab component will select particles using a ray or a volume.
### Configuring the falloff
- [var falloff: ClothGrabComponent.Falloff](clothgrabcomponent/falloff-swift.property.md)
  Controls whether the grabbing strength falls off based on distance from the volume surface.
- [ClothGrabComponent.Falloff](clothgrabcomponent/falloff-swift.struct.md)
  Controls whether grab strength falls off based on particle distance from the volume surface.
### Checking the grab state
- [var isGrabbing: Bool](clothgrabcomponent/isgrabbing.md)
  Indicates whether particles are currently being grabbed.
### Instance Properties
- [var mode: ClothGrabComponent.GrabMode](clothgrabcomponent/mode.md)
  Mode that determines whether grabbing will be performed using a ray or a volume.

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
- [struct ClothForceVolumeComponent](clothforcevolumecomponent.md)
  A component that creates a force volume applying forces to any intersecting cloth body particles.
- [struct ClothQueryVolumeComponent](clothqueryvolumecomponent.md)
  A component that defines a volume for querying particles of cloth bodies.
- [struct ClothCoordinateSpace](clothcoordinatespace.md)
  Defines a reference frame within a cloth simulation.
- [struct PerClothVertexData](perclothvertexdata.md)
  A generic type that stores per-vertex data in a buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothgrabcomponent)*