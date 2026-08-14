# LowLevelDeformation.Pipeline.Descriptor.BlendShape

**Framework**: RealityKit  
**Kind**: struct

The blend-shape configuration for a deformation pipeline.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct BlendShape
```

## Topics

### Structures
- [LowLevelDeformation.Pipeline.Descriptor.BlendShape.VertexSemanticOutputs](lowleveldeformation/pipeline/descriptor/blendshape-swift.struct/vertexsemanticoutputs.md)
  Identifies which tangent-frame attributes are blended in addition to positions.
### Initializers
- [init(blendsOutputs: LowLevelDeformation.Pipeline.Descriptor.BlendShape.VertexSemanticOutputs, computesBitangent: Bool)](lowleveldeformation/pipeline/descriptor/blendshape-swift.struct/init(blendsoutputs:computesbitangent:).md)
  Creates a blend-shape descriptor.
### Instance Properties
- [var blendsOutputs: LowLevelDeformation.Pipeline.Descriptor.BlendShape.VertexSemanticOutputs](lowleveldeformation/pipeline/descriptor/blendshape-swift.struct/blendsoutputs.md)
  Indicates which vertices of the tangent frame are blended in addition to positions. Currently supported: [normal|tangent]
- [var computesBitangent: Bool](lowleveldeformation/pipeline/descriptor/blendshape-swift.struct/computesbitangent.md)
  Indicates if bitangents should be recomputed from blended normals and tangents. Only valid if blendsOutputs = [normal, tangent].

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveldeformation/pipeline/descriptor/blendshape-swift.struct)*