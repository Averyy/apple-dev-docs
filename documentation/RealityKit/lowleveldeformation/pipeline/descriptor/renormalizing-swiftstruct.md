# LowLevelDeformation.Pipeline.Descriptor.Renormalizing

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
struct Renormalizing
```

## Topics

### Creating a renormalizing descriptor
- [init(renormalizesNormals: Bool, renormalizesTangents: Bool, renormalizesBitangents: Bool, triangleIndexType: MTLIndexType, adjacencyIndexType: MTLIndexType, adjacencyEndIndexType: MTLIndexType)](lowleveldeformation/pipeline/descriptor/renormalizing-swift.struct/init(renormalizesnormals:renormalizestangents:renormalizesbitangents:triangleindextype:adjacencyindextype:adjacencyendindextype:).md)
  Creates a renormalizing descriptor.
### Selecting attributes to renormalize
- [var renormalizesNormals: Bool](lowleveldeformation/pipeline/descriptor/renormalizing-swift.struct/renormalizesnormals.md)
  A Boolean value that indicates whether the pipeline renormalizes vertex normals.
- [var renormalizesTangents: Bool](lowleveldeformation/pipeline/descriptor/renormalizing-swift.struct/renormalizestangents.md)
  A Boolean value that indicates whether the pipeline renormalizes tangent vectors.
- [var renormalizesBitangents: Bool](lowleveldeformation/pipeline/descriptor/renormalizing-swift.struct/renormalizesbitangents.md)
  A Boolean value that indicates whether the pipeline renormalizes bitangent vectors.
### Configuring index buffer types
- [var triangleIndexType: MTLIndexType](lowleveldeformation/pipeline/descriptor/renormalizing-swift.struct/triangleindextype.md)
  The data type of the triangle index buffer.
- [var adjacencyIndexType: MTLIndexType](lowleveldeformation/pipeline/descriptor/renormalizing-swift.struct/adjacencyindextype.md)
  The data type of the per-vertex adjacencies buffer.
- [var adjacencyEndIndexType: MTLIndexType](lowleveldeformation/pipeline/descriptor/renormalizing-swift.struct/adjacencyendindextype.md)
  The data type of the per-vertex adjacency end-indices buffer.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var renormalizing: LowLevelDeformation.Pipeline.Descriptor.Renormalizing?](lowleveldeformation/pipeline/descriptor/renormalizing-swift.property.md)
  Renormalization parameters, or `nil` to omit renormalization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveldeformation/pipeline/descriptor/renormalizing-swift.struct)*