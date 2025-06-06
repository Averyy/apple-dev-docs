# indexCount

**Framework**: Model I/O  
**Kind**: property

The number of indices in the submesh’s index buffer.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var indexCount: Int { get }
```

#### Discussion

Use this index count when rendering the submesh.

## See Also

- [var indexBuffer: any MDLMeshBuffer](mdlsubmesh/indexbuffer.md)
  An object that provides index data for the submesh.
- [var indexType: MDLIndexBitDepth](mdlsubmesh/indextype.md)
  The data type for each element in the submesh’s index buffer.
- [var geometryType: MDLGeometryType](mdlsubmesh/geometrytype.md)
  The type of geometric primitives described by the submesh’s index buffer.
- [var topology: MDLSubmeshTopology?](mdlsubmesh/topology.md)
  A description of how the non-uniform layout of the submesh’s index buffer defines the shape of the mesh.
- [func indexBuffer(asIndexType: MDLIndexBitDepth) -> any MDLMeshBuffer](mdlsubmesh/indexbuffer(asindextype:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlsubmesh/indexcount)*