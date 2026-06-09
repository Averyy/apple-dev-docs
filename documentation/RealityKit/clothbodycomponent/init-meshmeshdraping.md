# init(mesh:meshDraping:)

**Framework**: RealityKit  
**Kind**: init

Creates a new cloth body component.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(mesh: ClothMeshResource, meshDraping: ClothPoseResource? = nil)
```

#### Discussion

The body component must be attached to an entity that is a descendant of a simulation root (an entity with a [`ClothSimulationComponent`](clothsimulationcomponent.md)) in order to be active.

## Parameters

- `mesh`: The (simulation) mesh of the cloth body, which defines its at-rest shape.
- `meshDraping`: An optional initial pose for the body.

## See Also

- [var mesh: ClothMeshResource](clothbodycomponent/mesh.md)
  The (simulation) mesh of the cloth body that defines the rest pose of the body.
- [var initialMeshDraping: ClothPoseResource?](clothbodycomponent/initialmeshdraping.md)
  An optional pose that specifies an already draped configuration of the cloth at the start of the simulation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothbodycomponent/init(mesh:meshdraping:))*