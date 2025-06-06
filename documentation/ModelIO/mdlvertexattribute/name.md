# name

**Framework**: Model I/O  
**Kind**: property

An identifier for the semantic use of the vertex attribute.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var name: String { get set }
```

#### Discussion

Depending on the source of data for a mesh—that is, which file format it was loaded from in a [`MDLAsset`](mdlasset.md) object, or whether it was programmatically created—a vertex attribute’s name can be either one of the constants listed in [`Vertex Attributes`](vertex-attributes.md) or an identifier specific to the file format.

## See Also

- [var format: MDLVertexFormat](mdlvertexattribute/format.md)
  The format of per-vertex data for the attribute.
- [var offset: Int](mdlvertexattribute/offset.md)
  The offset, in bytes, of vertex data for the attribute in a vertex buffer, relative to the start of data for each vertex.
- [var bufferIndex: Int](mdlvertexattribute/bufferindex.md)
  The index of the vertex buffer containing data for this attribute in a mesh’s [`vertexBuffers`](mdlmesh/vertexbuffers.md) array.
- [var initializationValue: vector_float4](mdlvertexattribute/initializationvalue.md)
  The default value for vertex data for this attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlvertexattribute/name)*