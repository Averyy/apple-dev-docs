# initializationValue

**Framework**: Model I/O  
**Kind**: property

The default value for vertex data for this attribute.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var initializationValue: vector_float4 { get set }
```

#### Discussion

When you set the [`vertexDescriptor`](mdlmesh/vertexdescriptor.md) property of a [`MDLMesh`](mdlmesh.md) object, the mesh automatically formats its vertex buffers to match the new descriptor. If the vertex descriptor contains a vertex attribute that is not already present in the mesh, the mesh creates a new vertex buffer (or allocates space in an interleaved vertex buffer, if the vertex descriptor describes such) for the new attribute, and fills in per-vertex data for that attribute using this property’s value.

Although this property’s type is `vector_float4`, Model I/O  uses only the components of the vector that match the vertex attribute’s [`format`](mdlvertexattribute/format.md) property. For example, if you set this property’s value to the vector `{1, 2, 3, 4}` on a vertex attribute whose format is [`MDLVertexFormat.float2`](mdlvertexformat/float2.md), each vertex will be initialized with the value `{1, 2}`.

The default initialization value is the vector `{0, 0, 0, 1}`.

## See Also

- [var name: String](mdlvertexattribute/name.md)
  An identifier for the semantic use of the vertex attribute.
- [var format: MDLVertexFormat](mdlvertexattribute/format.md)
  The format of per-vertex data for the attribute.
- [var offset: Int](mdlvertexattribute/offset.md)
  The offset, in bytes, of vertex data for the attribute in a vertex buffer, relative to the start of data for each vertex.
- [var bufferIndex: Int](mdlvertexattribute/bufferindex.md)
  The index of the vertex buffer containing data for this attribute in a mesh’s [`vertexBuffers`](mdlmesh/vertexbuffers.md) array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlvertexattribute/initializationvalue)*