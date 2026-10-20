# LowLevelDeformation.VertexSemantic

**Framework**: RealityKit  
**Kind**: enum  
**Role**: Enumeration

Designates the intended usage of a vertex attribute.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
enum VertexSemantic
```

## Topics

### Identifying vertex attributes
- [LowLevelDeformation.VertexSemantic.position](./vertexsemantic/position.md)
  The semantic for vertex position data.
- [LowLevelDeformation.VertexSemantic.normal](./vertexsemantic/normal.md)
  The semantic for surface normal data.
- [LowLevelDeformation.VertexSemantic.tangent](./vertexsemantic/tangent.md)
  The semantic for surface tangent vector data.
- [LowLevelDeformation.VertexSemantic.bitangent](./vertexsemantic/bitangent.md)
  The semantic for surface bitangent vector data.
- [LowLevelDeformation.VertexSemantic.uv](./vertexsemantic/uv.md)
  Texture coordinate (for input to renormalization).

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing mesh data
- [var input: LowLevelDeformation.Mesh](./input.md)
  The input vertex data for this deformation.
- [var output: LowLevelDeformation.Mesh](./output.md)
  The output vertex data for this deformation.
- [LowLevelDeformation.Mesh](./mesh.md)
  A handle to the input or output vertex data of a [`LowLevelDeformation`](../lowleveldeformation.md).
- [var vertexCount: Int](./vertexcount.md)
  The number of vertices in the mesh.
- [LowLevelDeformation.VertexAttribute](./vertexattribute.md)
  An object that describes the format and stride of a single vertex attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveldeformation/vertexsemantic)*