# indexBuffer(asIndexType:)

**Framework**: Model I/O  
**Kind**: method

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func indexBuffer(asIndexType indexType: MDLIndexBitDepth) -> any MDLMeshBuffer
```

## See Also

- [var indexBuffer: any MDLMeshBuffer](mdlsubmesh/indexbuffer.md)
  An object that provides index data for the submesh.
- [var indexCount: Int](mdlsubmesh/indexcount.md)
  The number of indices in the submesh’s index buffer.
- [var indexType: MDLIndexBitDepth](mdlsubmesh/indextype.md)
  The data type for each element in the submesh’s index buffer.
- [var geometryType: MDLGeometryType](mdlsubmesh/geometrytype.md)
  The type of geometric primitives described by the submesh’s index buffer.
- [var topology: MDLSubmeshTopology?](mdlsubmesh/topology.md)
  A description of how the non-uniform layout of the submesh’s index buffer defines the shape of the mesh.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlsubmesh/indexbuffer(asindextype:))*