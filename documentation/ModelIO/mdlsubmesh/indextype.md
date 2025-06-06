# indexType

**Framework**: Model I/O  
**Kind**: property

The data type for each element in the submesh’s index buffer.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var indexType: MDLIndexBitDepth { get }
```

#### Discussion

For optimum performance, an index buffer should generally use the smallest possible data type to fit its number of indices.

## See Also

- [var indexBuffer: any MDLMeshBuffer](mdlsubmesh/indexbuffer.md)
  An object that provides index data for the submesh.
- [var indexCount: Int](mdlsubmesh/indexcount.md)
  The number of indices in the submesh’s index buffer.
- [var geometryType: MDLGeometryType](mdlsubmesh/geometrytype.md)
  The type of geometric primitives described by the submesh’s index buffer.
- [var topology: MDLSubmeshTopology?](mdlsubmesh/topology.md)
  A description of how the non-uniform layout of the submesh’s index buffer defines the shape of the mesh.
- [func indexBuffer(asIndexType: MDLIndexBitDepth) -> any MDLMeshBuffer](mdlsubmesh/indexbuffer(asindextype:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlsubmesh/indextype)*