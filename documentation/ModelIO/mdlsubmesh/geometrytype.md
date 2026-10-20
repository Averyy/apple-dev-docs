# geometryType

**Framework**: Model I/O  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) MDLGeometryType geometryType;
```

#### Discussion

This property determines how the sequence of indices in the submesh’s index buffer should be interpreted for rendering. For example, if the geometry type is [`MDLGeometryType.triangles`](../mdlgeometrytype/triangles.md), each triangle to be rendered comes from an independent set of three indices, but if the geometry type is [`MDLGeometryType.triangleStrips`](../mdlgeometrytype/trianglestrips.md), triangles to be rendered can come from overlapping sets of indices in the sequence. If the geometry type is [`MDLGeometryType.variableTopology`](../mdlgeometrytype/variabletopology.md), the [`topology`](./topology.md) property describes the non-uniform layout of the index buffer.

## See Also

### Working with a Submesh’s Index Buffer
- [var indexBuffer: any MDLMeshBuffer](./indexbuffer.md)
  An object that provides index data for the submesh.
- [var indexCount: Int](./indexcount.md)
  The number of indices in the submesh’s index buffer.
- [var indexType: MDLIndexBitDepth](./indextype.md)
  The data type for each element in the submesh’s index buffer.
- [var topology: MDLSubmeshTopology?](./topology.md)
  A description of how the non-uniform layout of the submesh’s index buffer defines the shape of the mesh.
- [func indexBuffer(asIndexType: MDLIndexBitDepth) -> any MDLMeshBuffer](./indexbuffer%28asindextype%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlsubmesh/geometrytype)*