# setVertexBuffers:offsets:attributeStrides:withRange:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```objc
- (void) setVertexBuffers:(id<MTLBuffer> const[]) buffers offsets:(const NSUInteger[]) offsets attributeStrides:(const NSUInteger[]) strides withRange:(NSRange) range;
```

## See Also

### Assigning buffers
- [func setVertexBuffer((any MTLBuffer)?, offset: Int, index: Int)](./setvertexbuffer%28_,offset,index%29.md)
  Assigns a buffer to an entry in the vertex shader argument table.
- [func setVertexBuffer((any MTLBuffer)?, offset: Int, attributeStride: Int, index: Int)](./setvertexbuffer%28_,offset,attributestride,index%29.md)
- [- setVertexBuffers:offsets:withRange:](./setvertexbuffers_offsets_withrange_.md)
  Assigns multiple buffers to a range of entries in the vertex shader argument table.
- [func setVertexBytes(UnsafeRawPointer, length: Int, index: Int)](./setvertexbytes%28_,length,index%29.md)
  Creates a buffer from bytes and assigns it to an entry in the vertex shader argument table.
- [func setVertexBytes(UnsafeRawPointer, length: Int, attributeStride: Int, index: Int)](./setvertexbytes%28_,length,attributestride,index%29.md)
- [func setVertexBufferOffset(Int, index: Int)](./setvertexbufferoffset%28_,index%29.md)
  Updates an entry in the vertex shader argument table with a new location within the entry’s current buffer.
- [func setVertexBufferOffset(offset: Int, attributeStride: Int, index: Int)](./setvertexbufferoffset%28offset,attributestride,index%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setvertexbuffers:offsets:attributestrides:withrange:)*