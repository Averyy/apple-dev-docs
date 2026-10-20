# format

**Framework**: Model I/O  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readwrite) MDLVertexFormat format;
```

#### Discussion

A [`MDLVertexFormat`](../mdlvertexformat.md) value describes the number of vector components for an attribute, as well as the data type of each component, and, for special packed formats, the layout of components.

## See Also

### Inspecting a Vertex Attribute
- [var name: String](./name.md)
  An identifier for the semantic use of the vertex attribute.
- [var offset: Int](./offset.md)
  The offset, in bytes, of vertex data for the attribute in a vertex buffer, relative to the start of data for each vertex.
- [var bufferIndex: Int](./bufferindex.md)
  The index of the vertex buffer containing data for this attribute in a mesh’s [`vertexBuffers`](../mdlmesh/vertexbuffers.md) array.
- [var initializationValue: vector_float4](./initializationvalue.md)
  The default value for vertex data for this attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlvertexattribute/format)*