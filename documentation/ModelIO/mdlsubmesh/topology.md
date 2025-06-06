# topology

**Framework**: Model I/O  
**Kind**: property

A description of how the non-uniform layout of the submesh’s index buffer defines the shape of the mesh.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var topology: MDLSubmeshTopology? { get set }
```

#### Discussion

Submeshes with non-uniform topology can also contain edge and vertex crease information for use by the [`newSubdividedMesh(_:submeshIndex:subdivisionLevels:)`](mdlmesh/newsubdividedmesh(_:submeshindex:subdivisionlevels:).md) method.

## See Also

- [var indexBuffer: any MDLMeshBuffer](mdlsubmesh/indexbuffer.md)
  An object that provides index data for the submesh.
- [var indexCount: Int](mdlsubmesh/indexcount.md)
  The number of indices in the submesh’s index buffer.
- [var indexType: MDLIndexBitDepth](mdlsubmesh/indextype.md)
  The data type for each element in the submesh’s index buffer.
- [var geometryType: MDLGeometryType](mdlsubmesh/geometrytype.md)
  The type of geometric primitives described by the submesh’s index buffer.
- [func indexBuffer(asIndexType: MDLIndexBitDepth) -> any MDLMeshBuffer](mdlsubmesh/indexbuffer(asindextype:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlsubmesh/topology)*