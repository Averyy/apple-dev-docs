# LowLevelDeformation.Pipeline.Descriptor.Renormalization

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

An object that describes which vertex attributes to renormalize to unit length after deformation.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct Renormalization
```

## Topics

### Creating a renormalization descriptor
- [init(outputs: LowLevelDeformation.Pipeline.Descriptor.Renormalization.VertexSemanticOutputs, triangleIndexType: MTLIndexType, adjacencyIndexType: MTLIndexType, adjacencyEndIndexType: MTLIndexType)](./renormalization-swift.struct/init%28outputs,triangleindextype,adjacencyindextype,adjacencyendindextype%29.md)
  Creates a renormalization descriptor.
### Selecting attributes to renormalize
- [var outputs: LowLevelDeformation.Pipeline.Descriptor.Renormalization.VertexSemanticOutputs](./renormalization-swift.struct/outputs.md)
  The vertex attributes to renormalize to unit length.
- [LowLevelDeformation.Pipeline.Descriptor.Renormalization.VertexSemanticOutputs](./renormalization-swift.struct/vertexsemanticoutputs.md)
  Identifies which vertex attributes are renormalized to unit length.
### Configuring index buffer types
- [var triangleIndexType: MTLIndexType](./renormalization-swift.struct/triangleindextype.md)
  The data type of the triangle index buffer.
- [var adjacencyIndexType: MTLIndexType](./renormalization-swift.struct/adjacencyindextype.md)
  The data type of the per-vertex adjacencies buffer.
- [var adjacencyEndIndexType: MTLIndexType](./renormalization-swift.struct/adjacencyendindextype.md)
  The data type of the per-vertex adjacency end-indices buffer.

## Relationships

### Conforms To
- [Sendable](../../../../Swift/sendable.md)
- [SendableMetatype](../../../../Swift/sendablemetatype.md)

## See Also

### Configuring renormalization
- [var renormalization: LowLevelDeformation.Pipeline.Descriptor.Renormalization?](./renormalization-swift.property.md)
  Renormalization parameters, or `nil` to omit renormalization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveldeformation/pipeline/descriptor/renormalization-swift.struct)*