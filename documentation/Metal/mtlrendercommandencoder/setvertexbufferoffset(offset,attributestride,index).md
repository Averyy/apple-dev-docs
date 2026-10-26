# setVertexBufferOffset(offset:attributeStride:index:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func setVertexBufferOffset(offset: Int, attributeStride stride: Int, index: Int)
```

```objc
- (void) setVertexBufferOffset:(NSUInteger) offset attributeStride:(NSUInteger) stride atIndex:(NSUInteger) index;
```

## See Also

### Assigning buffers
- [func setVertexBuffer((any MTLBuffer)?, offset: Int, index: Int)](./setvertexbuffer%28_,offset,index%29.md)
  Assigns a buffer to an entry in the vertex shader argument table.
- [func setVertexBuffer((any MTLBuffer)?, offset: Int, attributeStride: Int, index: Int)](./setvertexbuffer%28_,offset,attributestride,index%29.md)
- [func setVertexBuffers([(any MTLBuffer)?], offsets: [Int], range: Range<Int>)](./setvertexbuffers%28_,offsets,range%29.md)
  Assigns multiple buffers to a range of entries in the vertex shader argument table.
- [func setVertexBuffers([(any MTLBuffer)?], offsets: [Int], attributeStrides: [Int], range: Range<Int>)](./setvertexbuffers%28_,offsets,attributestrides,range%29.md)
- [func setVertexBytes(UnsafeRawPointer, length: Int, index: Int)](./setvertexbytes%28_,length,index%29.md)
  Creates a buffer from bytes and assigns it to an entry in the vertex shader argument table.
- [func setVertexBytes(UnsafeRawPointer, length: Int, attributeStride: Int, index: Int)](./setvertexbytes%28_,length,attributestride,index%29.md)
- [func setVertexBufferOffset(Int, index: Int)](./setvertexbufferoffset%28_,index%29.md)
  Updates an entry in the vertex shader argument table with a new location within the entry’s current buffer.
- [- setVertexBuffers:offsets:withRange:](./setvertexbuffers_offsets_withrange_.md)
  Assigns multiple buffers to a range of entries in the vertex shader argument table.
- [- setVertexBuffers:offsets:attributeStrides:withRange:](./setvertexbuffers_offsets_attributestrides_withrange_.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setvertexbufferoffset(offset:attributestride:index:))*