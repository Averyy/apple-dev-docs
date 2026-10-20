# visualMeshWeights

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

Optional weights by which the visual mesh should be deformed according to the simulation mesh.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var visualMeshWeights: PerClothVertexData<Float>?
```

#### Discussion

A weight of 1 indicates that the simulation will fully control the corresponding visual vertex, whereas a weight of 0 indicates that the simulation will not affect the visual vertex at all.

## See Also

### Mapping the visual mesh
- [var visualMesh: LowLevelMesh?](./visualmesh.md)
  The dynamically deforming visual mesh of the cloth body, which you may read but not modify.
- [var materialNames: [String]](./materialnames.md)
  The names of the body materials used by this cloth body.
- [ClothBodyComponent.PerVisualVertexData](./pervisualvertexdata.md)
  Stores per-vertex data for all visual vertices in a buffer.
- [ClothBodyComponent.PerSimulationVertexData](./persimulationvertexdata.md)
  Stores per-vertex data for all simulation vertices in a buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothbodycomponent/visualmeshweights)*