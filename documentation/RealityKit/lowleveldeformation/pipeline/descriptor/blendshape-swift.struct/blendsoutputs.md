# blendsOutputs

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

Indicates which vertices of the tangent frame are blended in addition to positions. Currently supported: [normal|tangent]

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var blendsOutputs: LowLevelDeformation.Pipeline.Descriptor.BlendShape.VertexSemanticOutputs
```

## See Also

### Configuring blended attributes
- [LowLevelDeformation.Pipeline.Descriptor.BlendShape.VertexSemanticOutputs](./vertexsemanticoutputs.md)
  Identifies which tangent-frame attributes are blended in addition to positions.
- [var computesBitangent: Bool](./computesbitangent.md)
  Indicates if bitangents should be recomputed from blended normals and tangents. Only valid if blendsOutputs = [normal, tangent].


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveldeformation/pipeline/descriptor/blendshape-swift.struct/blendsoutputs)*