# LowLevelDeformation.Pipeline.Descriptor.BlendShape

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

The blend-shape configuration for a deformation pipeline.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct BlendShape
```

## Topics

### Creating a blend shape configuration
- [init(blendsOutputs: LowLevelDeformation.Pipeline.Descriptor.BlendShape.VertexSemanticOutputs, computesBitangent: Bool)](./blendshape-swift.struct/init%28blendsoutputs,computesbitangent%29.md)
  Creates a blend-shape descriptor.
### Configuring blended attributes
- [var blendsOutputs: LowLevelDeformation.Pipeline.Descriptor.BlendShape.VertexSemanticOutputs](./blendshape-swift.struct/blendsoutputs.md)
  Indicates which vertices of the tangent frame are blended in addition to positions. Currently supported: [normal|tangent]
- [LowLevelDeformation.Pipeline.Descriptor.BlendShape.VertexSemanticOutputs](./blendshape-swift.struct/vertexsemanticoutputs.md)
  Identifies which tangent-frame attributes are blended in addition to positions.
- [var computesBitangent: Bool](./blendshape-swift.struct/computesbitangent.md)
  Indicates if bitangents should be recomputed from blended normals and tangents. Only valid if blendsOutputs = [normal, tangent].

## Relationships

### Conforms To
- [Sendable](../../../../Swift/sendable.md)
- [SendableMetatype](../../../../Swift/sendablemetatype.md)

## See Also

### Configuring blend shapes
- [var blendShape: LowLevelDeformation.Pipeline.Descriptor.BlendShape?](./blendshape-swift.property.md)
  Blend-shape parameters, or `nil` to omit blend-shape deformation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveldeformation/pipeline/descriptor/blendshape-swift.struct)*