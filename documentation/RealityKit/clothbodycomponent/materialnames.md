# materialNames

**Framework**: RealityKit  
**Kind**: property

The names of the body materials used by this cloth body.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var materialNames: [String]
```

#### Discussion

The default material is used if no matching material name is present in [`ClothSimulationComponent`](clothsimulationcomponent.md).

The material of the cloth body determines different properties about the physical behavior of the body, like its resistance to being stretched or the friction it experiences when colliding.

Note, only the first material name is used.

## See Also

- [var visualMesh: LowLevelMesh?](clothbodycomponent/visualmesh.md)
  The dynamically deforming visual mesh of the cloth body, which you may read but not modify.
- [var visualMeshWeights: PerClothVertexData<Float>?](clothbodycomponent/visualmeshweights.md)
  Optional weights by which the visual mesh should be deformed according to the simulation mesh.
- [ClothBodyComponent.PerVisualVertexData](clothbodycomponent/pervisualvertexdata.md)
  Stores per-vertex data for all visual vertices in a buffer.
- [ClothBodyComponent.PerSimulationVertexData](clothbodycomponent/persimulationvertexdata.md)
  Stores per-vertex data for all simulation vertices in a buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothbodycomponent/materialnames)*