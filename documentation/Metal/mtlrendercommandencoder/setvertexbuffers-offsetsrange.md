# setVertexBuffers(_:offsets:range:)

**Framework**: Metal  
**Kind**: method

Assigns multiple buffers to a range of entries in the vertex shader argument table.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst ?+
- macOS 10.11+
- tvOS 8.0+
- visionOS ?+

## Declaration

```swift
func setVertexBuffers(_ buffers: [(any MTLBuffer)?], offsets: [Int], range: Range<Int>)
```

#### Discussion

By default, the buffer at each index is `nil`.

> **Note**:  The Objective-C version of this method is [`setVertexBuffers:offsets:withRange:`](mtlrendercommandencoder/setvertexbuffers:offsets:withrange:.md).

## Parameters

- `buffers`: An array of   instances the command assigns to entries in the vertex shader argument table for buffers.
- `offsets`: See the   to check for offset alignment requirements for buffers in   and   address space.
- `range`: A span of integers that represent the entries in the vertex shader argument table for buffers. Each entry stores a record of the corresponding element in   and  .

## See Also

- [func setVertexBuffer((any MTLBuffer)?, offset: Int, index: Int)](mtlrendercommandencoder/setvertexbuffer(_:offset:index:).md)
  Assigns a buffer to an entry in the vertex shader argument table.
- [func setVertexBuffer((any MTLBuffer)?, offset: Int, attributeStride: Int, index: Int)](mtlrendercommandencoder/setvertexbuffer(_:offset:attributestride:index:).md)
- [func setVertexBuffers([(any MTLBuffer)?], offsets: [Int], attributeStrides: [Int], range: Range<Int>)](mtlrendercommandencoder/setvertexbuffers(_:offsets:attributestrides:range:).md)
- [func setVertexBytes(UnsafeRawPointer, length: Int, index: Int)](mtlrendercommandencoder/setvertexbytes(_:length:index:).md)
  Creates a buffer from bytes and assigns it to an entry in the vertex shader argument table.
- [func setVertexBytes(UnsafeRawPointer, length: Int, attributeStride: Int, index: Int)](mtlrendercommandencoder/setvertexbytes(_:length:attributestride:index:).md)
- [func setVertexBufferOffset(Int, index: Int)](mtlrendercommandencoder/setvertexbufferoffset(_:index:).md)
  Updates an entry in the vertex shader argument table with a new location within the entry’s current buffer.
- [func setVertexBufferOffset(offset: Int, attributeStride: Int, index: Int)](mtlrendercommandencoder/setvertexbufferoffset(offset:attributestride:index:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setvertexbuffers(_:offsets:range:))*