# LowLevelDeformation.VertexSemantic

**Framework**: RealityKit  
**Kind**: enum

Designates the intended usage of a vertex attribute.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
enum VertexSemantic
```

## Topics

### Identifying vertex attributes
- [LowLevelDeformation.VertexSemantic.position](lowleveldeformation/vertexsemantic/position.md)
  The semantic for vertex position data.
- [LowLevelDeformation.VertexSemantic.normal](lowleveldeformation/vertexsemantic/normal.md)
  The semantic for surface normal data.
- [LowLevelDeformation.VertexSemantic.tangent](lowleveldeformation/vertexsemantic/tangent.md)
  The semantic for surface tangent vector data.
- [LowLevelDeformation.VertexSemantic.bitangent](lowleveldeformation/vertexsemantic/bitangent.md)
  The semantic for surface bitangent vector data.
- [LowLevelDeformation.VertexSemantic.uv](lowleveldeformation/vertexsemantic/uv.md)
  Texture coordinate (for input to renormalization).

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var input: LowLevelDeformation.Mesh](lowleveldeformation/input.md)
  The input vertex data for this deformation.
- [var output: LowLevelDeformation.Mesh](lowleveldeformation/output.md)
  The output vertex data for this deformation.
- [LowLevelDeformation.Mesh](lowleveldeformation/mesh.md)
  A handle to the input or output vertex data of a [`LowLevelDeformation`](lowleveldeformation.md).
- [var vertexCount: Int](lowleveldeformation/vertexcount.md)
  The number of vertices in the mesh.
- [LowLevelDeformation.VertexAttribute](lowleveldeformation/vertexattribute.md)
  An object that describes the format and stride of a single vertex attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveldeformation/vertexsemantic)*