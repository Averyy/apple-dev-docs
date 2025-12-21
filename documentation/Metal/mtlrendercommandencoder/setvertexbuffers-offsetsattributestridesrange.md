# setVertexBuffers(_:offsets:attributeStrides:range:)

**Framework**: Metal  
**Kind**: method

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+

## Declaration

```swift
func setVertexBuffers(_ buffers: [(any MTLBuffer)?], offsets: [Int], attributeStrides: [Int], range: Range<Int>)
```

## See Also

- [func setVertexBuffer((any MTLBuffer)?, offset: Int, index: Int)](mtlrendercommandencoder/setvertexbuffer(_:offset:index:).md)
  Assigns a buffer to an entry in the vertex shader argument table.
- [func setVertexBuffer((any MTLBuffer)?, offset: Int, attributeStride: Int, index: Int)](mtlrendercommandencoder/setvertexbuffer(_:offset:attributestride:index:).md)
- [func setVertexBuffers([(any MTLBuffer)?], offsets: [Int], range: Range<Int>)](mtlrendercommandencoder/setvertexbuffers(_:offsets:range:).md)
  Assigns multiple buffers to a range of entries in the vertex shader argument table.
- [func setVertexBytes(UnsafeRawPointer, length: Int, index: Int)](mtlrendercommandencoder/setvertexbytes(_:length:index:).md)
  Creates a buffer from bytes and assigns it to an entry in the vertex shader argument table.
- [func setVertexBytes(UnsafeRawPointer, length: Int, attributeStride: Int, index: Int)](mtlrendercommandencoder/setvertexbytes(_:length:attributestride:index:).md)
- [func setVertexBufferOffset(Int, index: Int)](mtlrendercommandencoder/setvertexbufferoffset(_:index:).md)
  Updates an entry in the vertex shader argument table with a new location within the entry’s current buffer.
- [func setVertexBufferOffset(offset: Int, attributeStride: Int, index: Int)](mtlrendercommandencoder/setvertexbufferoffset(offset:attributestride:index:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setvertexbuffers(_:offsets:attributestrides:range:))*