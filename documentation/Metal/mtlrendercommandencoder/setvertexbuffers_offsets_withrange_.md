# setVertexBuffers:offsets:withRange:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Assigns multiple buffers to a range of entries in the vertex shader argument table.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```objc
- (void) setVertexBuffers:(id<MTLBuffer> const[]) buffers offsets:(const NSUInteger[]) offsets withRange:(NSRange) range;
```

## Discussion

By default, the buffer at each index is `nil`.

> **Note**:  The Swift version of this method is [`setVertexBuffers(_:offsets:range:)`](./setvertexbuffers%28_,offsets,range%29.md).

## Parameters

- `buffers`: A pointer to a C array of [`MTLBuffer`](../mtlbuffer.md) instances the command assigns to entries in the vertex shader argument table for buffers.
- `offsets`: A pointer to a C array of unsigned integers. Each element represents the location, in bytes, from the start of the corresponding [`MTLBuffer`](../mtlbuffer.md) element in `buffers` where the vertex shader argument data begins.

  See the [Metal feature set tables (PDF)](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) to check for offset alignment requirements for buffers in `device` and `constant` address space.
- `range`: A span of integers that represent the entries in the vertex shader argument table for buffers. Each entry stores a record of the corresponding element in `buffers` and `offsets`.

## See Also

### Assigning buffers
- [func setVertexBuffer((any MTLBuffer)?, offset: Int, index: Int)](./setvertexbuffer%28_,offset,index%29.md)
  Assigns a buffer to an entry in the vertex shader argument table.
- [func setVertexBuffer((any MTLBuffer)?, offset: Int, attributeStride: Int, index: Int)](./setvertexbuffer%28_,offset,attributestride,index%29.md)
- [- setVertexBuffers:offsets:attributeStrides:withRange:](./setvertexbuffers_offsets_attributestrides_withrange_.md)
- [func setVertexBytes(UnsafeRawPointer, length: Int, index: Int)](./setvertexbytes%28_,length,index%29.md)
  Creates a buffer from bytes and assigns it to an entry in the vertex shader argument table.
- [func setVertexBytes(UnsafeRawPointer, length: Int, attributeStride: Int, index: Int)](./setvertexbytes%28_,length,attributestride,index%29.md)
- [func setVertexBufferOffset(Int, index: Int)](./setvertexbufferoffset%28_,index%29.md)
  Updates an entry in the vertex shader argument table with a new location within the entry’s current buffer.
- [func setVertexBufferOffset(offset: Int, attributeStride: Int, index: Int)](./setvertexbufferoffset%28offset,attributestride,index%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setvertexbuffers:offsets:withrange:)*