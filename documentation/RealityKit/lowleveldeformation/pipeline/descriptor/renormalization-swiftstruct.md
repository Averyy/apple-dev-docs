# LowLevelDeformation.Pipeline.Descriptor.Renormalization

**Framework**: RealityKit  
**Kind**: struct

An object that describes which vertex attributes to renormalize to unit length after deformation.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Renormalization
```

## Topics

### Structures
- [LowLevelDeformation.Pipeline.Descriptor.Renormalization.VertexSemanticOutputs](lowleveldeformation/pipeline/descriptor/renormalization-swift.struct/vertexsemanticoutputs.md)
  Identifies which vertex attributes are renormalized to unit length.
### Initializers
- [init(outputs: LowLevelDeformation.Pipeline.Descriptor.Renormalization.VertexSemanticOutputs, triangleIndexType: MTLIndexType, adjacencyIndexType: MTLIndexType, adjacencyEndIndexType: MTLIndexType)](lowleveldeformation/pipeline/descriptor/renormalization-swift.struct/init(outputs:triangleindextype:adjacencyindextype:adjacencyendindextype:).md)
  Creates a renormalization descriptor.
### Instance Properties
- [var adjacencyEndIndexType: MTLIndexType](lowleveldeformation/pipeline/descriptor/renormalization-swift.struct/adjacencyendindextype.md)
  The data type of the per-vertex adjacency end-indices buffer.
- [var adjacencyIndexType: MTLIndexType](lowleveldeformation/pipeline/descriptor/renormalization-swift.struct/adjacencyindextype.md)
  The data type of the per-vertex adjacencies buffer.
- [var outputs: LowLevelDeformation.Pipeline.Descriptor.Renormalization.VertexSemanticOutputs](lowleveldeformation/pipeline/descriptor/renormalization-swift.struct/outputs.md)
  The vertex attributes to renormalize to unit length.
- [var triangleIndexType: MTLIndexType](lowleveldeformation/pipeline/descriptor/renormalization-swift.struct/triangleindextype.md)
  The data type of the triangle index buffer.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveldeformation/pipeline/descriptor/renormalization-swift.struct)*