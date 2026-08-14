# LowLevelDeformation.VertexAttribute

**Framework**: RealityKit  
**Kind**: struct

An object that describes the format and stride of a single vertex attribute.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct VertexAttribute
```

## Topics

### Creating a vertex attribute
- [init(semantic: LowLevelDeformation.VertexSemantic, format: MTLVertexFormat, stride: Int)](lowleveldeformation/vertexattribute/init(semantic:format:stride:).md)
  Creates a vertex attribute.
### Accessing layout information
- [var stride: Int](lowleveldeformation/vertexattribute/stride.md)
  The distance, in bytes, between consecutive vertices for this attribute.
### Instance Properties
- [var format: MTLVertexFormat](lowleveldeformation/vertexattribute/format.md)
  The format of the vertex attribute.
- [var semantic: LowLevelDeformation.VertexSemantic](lowleveldeformation/vertexattribute/semantic.md)
  The semantic of the vertex attribute.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var input: LowLevelDeformation.Mesh](lowleveldeformation/input.md)
  The input vertex data for this deformation.
- [var output: LowLevelDeformation.Mesh](lowleveldeformation/output.md)
  The output vertex data for this deformation.
- [LowLevelDeformation.Mesh](lowleveldeformation/mesh.md)
  A handle to the input or output vertex data of a [`LowLevelDeformation`](lowleveldeformation.md).
- [var vertexCount: Int](lowleveldeformation/vertexcount.md)
  The number of vertices in the mesh.
- [LowLevelDeformation.VertexSemantic](lowleveldeformation/vertexsemantic.md)
  Designates the intended usage of a vertex attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveldeformation/vertexattribute)*