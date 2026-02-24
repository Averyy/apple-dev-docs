# setVertexBuffer(_:offset:index:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Assigns a buffer to an entry in the vertex shader argument table.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func setVertexBuffer(_ buffer: (any MTLBuffer)?, offset: Int, index: Int)
```

## Mentions

- [Improving CPU performance by using argument buffers](improving-cpu-performance-by-using-argument-buffers.md)

#### Discussion

By default, the buffer at each index is `nil`.

## Parameters

- `buffer`: An [`MTLBuffer`](mtlbuffer.md) instance the command assigns to an entry in the vertex shader argument table for buffers.
- `offset`: An integer that represents the location, in bytes, from the start of `buffer` where the vertex shader argument data begins. See the [`Metal feature set tables (PDF)`](https://developer.apple.comhttps://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) to check for offset alignment requirements for buffers in `device` and `constant` address space.
- `index`: An integer that represents the entry in the vertex shader argument table for buffers that stores a record of `buffer` and `offset`.

## See Also

- [func setVertexBuffer((any MTLBuffer)?, offset: Int, attributeStride: Int, index: Int)](mtlrendercommandencoder/setvertexbuffer(_:offset:attributestride:index:).md)
- [func setVertexBuffers([(any MTLBuffer)?], offsets: [Int], range: Range<Int>)](mtlrendercommandencoder/setvertexbuffers(_:offsets:range:).md)
  Assigns multiple buffers to a range of entries in the vertex shader argument table.
- [func setVertexBuffers([(any MTLBuffer)?], offsets: [Int], attributeStrides: [Int], range: Range<Int>)](mtlrendercommandencoder/setvertexbuffers(_:offsets:attributestrides:range:).md)
- [func setVertexBytes(UnsafeRawPointer, length: Int, index: Int)](mtlrendercommandencoder/setvertexbytes(_:length:index:).md)
  Creates a buffer from bytes and assigns it to an entry in the vertex shader argument table.
- [func setVertexBytes(UnsafeRawPointer, length: Int, attributeStride: Int, index: Int)](mtlrendercommandencoder/setvertexbytes(_:length:attributestride:index:).md)
- [func setVertexBufferOffset(Int, index: Int)](mtlrendercommandencoder/setvertexbufferoffset(_:index:).md)
  Updates an entry in the vertex shader argument table with a new location within the entry’s current buffer.
- [func setVertexBufferOffset(offset: Int, attributeStride: Int, index: Int)](mtlrendercommandencoder/setvertexbufferoffset(offset:attributestride:index:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setvertexbuffer(_:offset:index:))*