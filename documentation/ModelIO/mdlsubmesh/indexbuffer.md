# indexBuffer

**Framework**: Model I/O  
**Kind**: property

An object that provides index data for the submesh.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var indexBuffer: any MDLMeshBuffer { get }
```

#### Discussion

An index buffer contains indices, each of which identifies a vertex in the vertex buffers of the [`MDLMesh`](mdlmesh.md) object containing the mesh. Together with the submesh’s [`geometryType`](mdlsubmesh/geometrytype.md) property, the sequence of indices determines how to interpret the mesh’s vertex data to construct the geometric form for a portion of the mesh.

## See Also

- [var indexCount: Int](mdlsubmesh/indexcount.md)
  The number of indices in the submesh’s index buffer.
- [var indexType: MDLIndexBitDepth](mdlsubmesh/indextype.md)
  The data type for each element in the submesh’s index buffer.
- [var geometryType: MDLGeometryType](mdlsubmesh/geometrytype.md)
  The type of geometric primitives described by the submesh’s index buffer.
- [var topology: MDLSubmeshTopology?](mdlsubmesh/topology.md)
  A description of how the non-uniform layout of the submesh’s index buffer defines the shape of the mesh.
- [func indexBuffer(asIndexType: MDLIndexBitDepth) -> any MDLMeshBuffer](mdlsubmesh/indexbuffer(asindextype:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlsubmesh/indexbuffer)*