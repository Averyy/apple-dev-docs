# indexBuffer

**Framework**: Model I/O  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, retain, readonly) id<MDLMeshBuffer> indexBuffer;
```

#### Discussion

An index buffer contains indices, each of which identifies a vertex in the vertex buffers of the [`MDLMesh`](../mdlmesh.md) object containing the mesh. Together with the submesh’s [`geometryType`](./geometrytype.md) property, the sequence of indices determines how to interpret the mesh’s vertex data to construct the geometric form for a portion of the mesh.

## See Also

### Working with a Submesh’s Index Buffer
- [var indexCount: Int](./indexcount.md)
  The number of indices in the submesh’s index buffer.
- [var indexType: MDLIndexBitDepth](./indextype.md)
  The data type for each element in the submesh’s index buffer.
- [var geometryType: MDLGeometryType](./geometrytype.md)
  The type of geometric primitives described by the submesh’s index buffer.
- [var topology: MDLSubmeshTopology?](./topology.md)
  A description of how the non-uniform layout of the submesh’s index buffer defines the shape of the mesh.
- [func indexBuffer(asIndexType: MDLIndexBitDepth) -> any MDLMeshBuffer](./indexbuffer%28asindextype%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlsubmesh/indexbuffer)*