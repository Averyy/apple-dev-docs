# geometryType

**Framework**: Model I/O  
**Kind**: property

The type of geometric primitives described by the submesh’s index buffer.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var geometryType: MDLGeometryType { get }
```

#### Discussion

This property determines how the sequence of indices in the submesh’s index buffer should be interpreted for rendering. For example, if the geometry type is [`MDLGeometryType.triangles`](mdlgeometrytype/triangles.md), each triangle to be rendered comes from an independent set of three indices, but if the geometry type is [`MDLGeometryType.triangleStrips`](mdlgeometrytype/trianglestrips.md), triangles to be rendered can come from overlapping sets of indices in the sequence. If the geometry type is [`MDLGeometryType.variableTopology`](mdlgeometrytype/variabletopology.md), the [`topology`](mdlsubmesh/topology.md) property describes the non-uniform layout of the index buffer.

## See Also

- [var indexBuffer: any MDLMeshBuffer](mdlsubmesh/indexbuffer.md)
  An object that provides index data for the submesh.
- [var indexCount: Int](mdlsubmesh/indexcount.md)
  The number of indices in the submesh’s index buffer.
- [var indexType: MDLIndexBitDepth](mdlsubmesh/indextype.md)
  The data type for each element in the submesh’s index buffer.
- [var topology: MDLSubmeshTopology?](mdlsubmesh/topology.md)
  A description of how the non-uniform layout of the submesh’s index buffer defines the shape of the mesh.
- [func indexBuffer(asIndexType: MDLIndexBitDepth) -> any MDLMeshBuffer](mdlsubmesh/indexbuffer(asindextype:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlsubmesh/geometrytype)*