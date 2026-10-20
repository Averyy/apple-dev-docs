# offset

**Framework**: Model I/O  
**Kind**: property  
**Role**: Instance Property

The offset, in bytes, of vertex data for the attribute in a vertex buffer, relative to the start of data for each vertex.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var offset: Int { get set }
```

```objc
@property (nonatomic, readwrite) NSUInteger offset;
```

#### Discussion

For example, if a vertex buffer contains interleaved data for two attributes, the first attribute’s offset is typically zero, and the second attribute’s offset is at least the data size of the first attribute.

## See Also

### Inspecting a Vertex Attribute
- [var name: String](./name.md)
  An identifier for the semantic use of the vertex attribute.
- [var format: MDLVertexFormat](./format.md)
  The format of per-vertex data for the attribute.
- [var bufferIndex: Int](./bufferindex.md)
  The index of the vertex buffer containing data for this attribute in a mesh’s [`vertexBuffers`](../mdlmesh/vertexbuffers.md) array.
- [var initializationValue: vector_float4](./initializationvalue.md)
  The default value for vertex data for this attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlvertexattribute/offset)*