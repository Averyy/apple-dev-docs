# LowLevelDeformation.Mesh

**Framework**: RealityKit  
**Kind**: struct

A handle to the input or output vertex data of a [`LowLevelDeformation`](lowleveldeformation.md).

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Mesh
```

## Topics

### Setting vertex data
- [func setVertices(any MTLBuffer, offset: Int, semantic: LowLevelDeformation.VertexSemantic) throws(LowLevelDeformation.Error)](lowleveldeformation/mesh/setvertices(_:offset:semantic:).md)
  Binds a Metal buffer to the vertex attribute with the specified semantic.

## See Also

- [var input: LowLevelDeformation.Mesh](lowleveldeformation/input.md)
  The input vertex data for this deformation.
- [var output: LowLevelDeformation.Mesh](lowleveldeformation/output.md)
  The output vertex data for this deformation.
- [var vertexCount: Int](lowleveldeformation/vertexcount.md)
  The number of vertices in the mesh.
- [LowLevelDeformation.VertexSemantic](lowleveldeformation/vertexsemantic.md)
  Designates the intended usage of a vertex attribute.
- [LowLevelDeformation.VertexAttribute](lowleveldeformation/vertexattribute.md)
  An object that describes the format and stride of a single vertex attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveldeformation/mesh)*