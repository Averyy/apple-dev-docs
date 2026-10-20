# LowLevelDeformation.Mesh

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

A handle to the input or output vertex data of a [`LowLevelDeformation`](../lowleveldeformation.md).

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct Mesh
```

## Topics

### Setting vertex data
- [func setVertices(any MTLBuffer, offset: Int, semantic: LowLevelDeformation.VertexSemantic) throws](./mesh/setvertices%28_,offset,semantic%29.md)
  Binds a Metal buffer to the vertex attribute with the specified semantic.

## See Also

### Accessing mesh data
- [var input: LowLevelDeformation.Mesh](./input.md)
  The input vertex data for this deformation.
- [var output: LowLevelDeformation.Mesh](./output.md)
  The output vertex data for this deformation.
- [var vertexCount: Int](./vertexcount.md)
  The number of vertices in the mesh.
- [LowLevelDeformation.VertexSemantic](./vertexsemantic.md)
  Designates the intended usage of a vertex attribute.
- [LowLevelDeformation.VertexAttribute](./vertexattribute.md)
  An object that describes the format and stride of a single vertex attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveldeformation/mesh)*