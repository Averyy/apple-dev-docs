# ClothBodyComponent.PerVisualVertexData

**Framework**: RealityKit  
**Kind**: typealias

Stores per-vertex data for all visual vertices in a buffer.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
typealias PerVisualVertexData = PerClothVertexData
```

## See Also

- [var visualMesh: LowLevelMesh?](clothbodycomponent/visualmesh.md)
  The dynamically deforming visual mesh of the cloth body, which you may read but not modify.
- [var visualMeshWeights: PerClothVertexData<Float>?](clothbodycomponent/visualmeshweights.md)
  Optional weights by which the visual mesh should be deformed according to the simulation mesh.
- [var materialNames: [String]](clothbodycomponent/materialnames.md)
  The names of the body materials used by this cloth body.
- [ClothBodyComponent.PerSimulationVertexData](clothbodycomponent/persimulationvertexdata.md)
  Stores per-vertex data for all simulation vertices in a buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothbodycomponent/pervisualvertexdata)*