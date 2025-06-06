# bufferIndex

**Framework**: Model I/O  
**Kind**: property

The index of the vertex buffer containing data for this attribute in a mesh’s [`vertexBuffers`](mdlmesh/vertexbuffers.md) array.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var bufferIndex: Int { get set }
```

#### Discussion

A mesh may store vertex data in either a  model, where data for each attribute lies in a separate vertex buffer, or in an  model. In the latter, multiple vertex attributes share the same buffer (and thus have the same [`bufferIndex`](mdlvertexattribute/bufferindex.md) value), and the [`format`](mdlvertexattribute/format.md) and [`offset`](mdlvertexattribute/offset.md) values (together with the [`stride`](mdlvertexbufferlayout/stride.md) value of a related [`MDLVertexBufferLayout`](mdlvertexbufferlayout.md) object) identify which bytes in that buffer refer to which vertex attributes.

## See Also

- [var name: String](mdlvertexattribute/name.md)
  An identifier for the semantic use of the vertex attribute.
- [var format: MDLVertexFormat](mdlvertexattribute/format.md)
  The format of per-vertex data for the attribute.
- [var offset: Int](mdlvertexattribute/offset.md)
  The offset, in bytes, of vertex data for the attribute in a vertex buffer, relative to the start of data for each vertex.
- [var initializationValue: vector_float4](mdlvertexattribute/initializationvalue.md)
  The default value for vertex data for this attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlvertexattribute/bufferindex)*