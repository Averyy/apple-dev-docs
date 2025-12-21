# bufferIndex

**Framework**: Metal  
**Kind**: property

The index in the argument table for the associated vertex buffer.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var bufferIndex: Int { get set }
```

## See Also

- [func setVertexBuffer((any MTLBuffer)?, offset: Int, index: Int)](mtlrendercommandencoder/setvertexbuffer(_:offset:index:).md)
  Assigns a buffer to an entry in the vertex shader argument table.
- [var format: MTLVertexFormat](mtlvertexattributedescriptor/format.md)
  The format of the vertex attribute.
- [var offset: Int](mtlvertexattributedescriptor/offset.md)
  The location of an attribute in vertex data, determined by the byte offset from the start of the vertex data.
- [enum MTLVertexFormat](mtlvertexformat.md)
  Values that specify the organization of function vertex data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlvertexattributedescriptor/bufferindex)*