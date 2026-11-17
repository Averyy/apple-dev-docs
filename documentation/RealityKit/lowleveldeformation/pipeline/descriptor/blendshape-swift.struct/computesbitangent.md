# computesBitangent

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

Indicates if bitangents should be recomputed from blended normals and tangents. Only valid if blendsOutputs = [normal, tangent].

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var computesBitangent: Bool
```

## See Also

### Configuring blended attributes
- [var blendsOutputs: LowLevelDeformation.Pipeline.Descriptor.BlendShape.VertexSemanticOutputs](./blendsoutputs.md)
  Indicates which vertices of the tangent frame are blended in addition to positions. Currently supported: [normal|tangent]
- [LowLevelDeformation.Pipeline.Descriptor.BlendShape.VertexSemanticOutputs](./vertexsemanticoutputs.md)
  Identifies which tangent-frame attributes are blended in addition to positions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveldeformation/pipeline/descriptor/blendshape-swift.struct/computesbitangent)*