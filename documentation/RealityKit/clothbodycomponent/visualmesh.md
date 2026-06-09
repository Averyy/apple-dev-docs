# visualMesh

**Framework**: RealityKit  
**Kind**: property

The dynamically deforming visual mesh of the cloth body, which you may read but not modify.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var visualMesh: LowLevelMesh? { get }
```

#### Discussion

This visual mesh will always be nil at first. The visual mesh becomes non-nil if the entity is part of a simulation and has a [`ModelComponent`](modelcomponent.md) whose mesh is not a [`LowLevelMesh`](lowlevelmesh.md). This is a dynamically deforming version of the mesh stored in the [`ModelComponent`](modelcomponent.md), and overrides the rendering.

The visual mesh is updated on the GPU after each simulation update. Subscribe to [`ClothSimulationEvents.AfterUpdate`](clothsimulationevents/afterupdate.md) to know when new data is available. To read the mesh contents on the GPU, encode your work using the scene’s `commandQueue` to ensure proper synchronization with the simulation’s GPU writes.

## See Also

- [var visualMeshWeights: PerClothVertexData<Float>?](clothbodycomponent/visualmeshweights.md)
  Optional weights by which the visual mesh should be deformed according to the simulation mesh.
- [var materialNames: [String]](clothbodycomponent/materialnames.md)
  The names of the body materials used by this cloth body.
- [ClothBodyComponent.PerVisualVertexData](clothbodycomponent/pervisualvertexdata.md)
  Stores per-vertex data for all visual vertices in a buffer.
- [ClothBodyComponent.PerSimulationVertexData](clothbodycomponent/persimulationvertexdata.md)
  Stores per-vertex data for all simulation vertices in a buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothbodycomponent/visualmesh)*