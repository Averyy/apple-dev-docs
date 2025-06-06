# format

**Framework**: Model I/O  
**Kind**: property

The format of per-vertex data for the attribute.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var format: MDLVertexFormat { get set }
```

#### Discussion

A [`MDLVertexFormat`](mdlvertexformat.md) value describes the number of vector components for an attribute, as well as the data type of each component, and, for special packed formats, the layout of components.

## See Also

- [var name: String](mdlvertexattribute/name.md)
  An identifier for the semantic use of the vertex attribute.
- [var offset: Int](mdlvertexattribute/offset.md)
  The offset, in bytes, of vertex data for the attribute in a vertex buffer, relative to the start of data for each vertex.
- [var bufferIndex: Int](mdlvertexattribute/bufferindex.md)
  The index of the vertex buffer containing data for this attribute in a mesh’s [`vertexBuffers`](mdlmesh/vertexbuffers.md) array.
- [var initializationValue: vector_float4](mdlvertexattribute/initializationvalue.md)
  The default value for vertex data for this attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlvertexattribute/format)*