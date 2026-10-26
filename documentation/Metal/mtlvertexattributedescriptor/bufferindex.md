# bufferIndex

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The index in the argument table for the associated vertex buffer.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var bufferIndex: Int { get set }
```

```objc
@property (nonatomic, assign) NSUInteger bufferIndex;
```

## See Also

### Related Documentation
- [func setVertexBuffer((any MTLBuffer)?, offset: Int, index: Int)](../mtlrendercommandencoder/setvertexbuffer%28_,offset,index%29.md)
  Assigns a buffer to an entry in the vertex shader argument table.
- [- setVertexBuffers:offsets:withRange:](../mtlrendercommandencoder/setvertexbuffers_offsets_withrange_.md)
  Assigns multiple buffers to a range of entries in the vertex shader argument table.
### Organizing the vertex attribute
- [var format: MTLVertexFormat](./format.md)
  The format of the vertex attribute.
- [var offset: Int](./offset.md)
  The location of an attribute in vertex data, determined by the byte offset from the start of the vertex data.
- [enum MTLVertexFormat](../mtlvertexformat.md)
  The vertex data format options for render pipelines.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlvertexattributedescriptor/bufferindex)*