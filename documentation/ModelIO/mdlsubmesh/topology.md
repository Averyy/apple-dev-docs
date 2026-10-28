# topology

**Framework**: Model I/O  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, retain, nullable) MDLSubmeshTopology * topology;
```

## Discussion

Submeshes with non-uniform topology can also contain edge and vertex crease information for use by the [`newSubdividedMesh(_:submeshIndex:subdivisionLevels:)`](../mdlmesh/newsubdividedmesh%28_,submeshindex,subdivisionlevels%29.md) method.

## See Also

### Working with a Submesh’s Index Buffer
- [var indexBuffer: any MDLMeshBuffer](./indexbuffer.md)
  An object that provides index data for the submesh.
- [var indexCount: Int](./indexcount.md)
  The number of indices in the submesh’s index buffer.
- [var indexType: MDLIndexBitDepth](./indextype.md)
  The data type for each element in the submesh’s index buffer.
- [var geometryType: MDLGeometryType](./geometrytype.md)
  The type of geometric primitives described by the submesh’s index buffer.
- [func indexBuffer(asIndexType: MDLIndexBitDepth) -> any MDLMeshBuffer](./indexbuffer%28asindextype%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlsubmesh/topology)*