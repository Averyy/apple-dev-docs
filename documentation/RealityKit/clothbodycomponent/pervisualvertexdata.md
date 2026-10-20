# ClothBodyComponent.PerVisualVertexData

**Framework**: RealityKit  
**Kind**: typealias  
**Role**: Type Alias

Stores per-vertex data for all visual vertices in a buffer.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- visionOS 27.0+

## Declaration

```swift
typealias PerVisualVertexData = PerClothVertexData
```

## See Also

### Mapping the visual mesh
- [var visualMesh: LowLevelMesh?](./visualmesh.md)
  The dynamically deforming visual mesh of the cloth body, which you may read but not modify.
- [var visualMeshWeights: PerClothVertexData<Float>?](./visualmeshweights.md)
  Optional weights by which the visual mesh should be deformed according to the simulation mesh.
- [var materialNames: [String]](./materialnames.md)
  The names of the body materials used by this cloth body.
- [ClothBodyComponent.PerSimulationVertexData](./persimulationvertexdata.md)
  Stores per-vertex data for all simulation vertices in a buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothbodycomponent/pervisualvertexdata)*