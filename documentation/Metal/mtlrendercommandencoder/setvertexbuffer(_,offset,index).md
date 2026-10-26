# setVertexBuffer(_:offset:index:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Assigns a buffer to an entry in the vertex shader argument table.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func setVertexBuffer(_ buffer: (any MTLBuffer)?, offset: Int, index: Int)
```

```objc
- (void) setVertexBuffer:(id<MTLBuffer>) buffer offset:(NSUInteger) offset atIndex:(NSUInteger) index;
```

## Mentions

- [Improving CPU performance by using argument buffers](../improving-cpu-performance-by-using-argument-buffers.md)

#### Discussion

By default, the buffer at each index is `nil`.

## Parameters

- `buffer`: An [`MTLBuffer`](../mtlbuffer.md) instance the command assigns to an entry in the vertex shader argument table for buffers.
- `offset`: An integer that represents the location, in bytes, from the start of `buffer` where the vertex shader argument data begins.

  See the [Metal feature set tables (PDF)](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) to check for offset alignment requirements for buffers in `device` and `constant` address space.
- `index`: An integer that represents the entry in the vertex shader argument table for buffers that stores a record of `buffer` and `offset`.

## See Also

### Assigning buffers
- [func setVertexBuffer((any MTLBuffer)?, offset: Int, attributeStride: Int, index: Int)](./setvertexbuffer%28_,offset,attributestride,index%29.md)
- [func setVertexBuffers([(any MTLBuffer)?], offsets: [Int], range: Range<Int>)](./setvertexbuffers%28_,offsets,range%29.md)
  Assigns multiple buffers to a range of entries in the vertex shader argument table.
- [func setVertexBuffers([(any MTLBuffer)?], offsets: [Int], attributeStrides: [Int], range: Range<Int>)](./setvertexbuffers%28_,offsets,attributestrides,range%29.md)
- [func setVertexBytes(UnsafeRawPointer, length: Int, index: Int)](./setvertexbytes%28_,length,index%29.md)
  Creates a buffer from bytes and assigns it to an entry in the vertex shader argument table.
- [func setVertexBytes(UnsafeRawPointer, length: Int, attributeStride: Int, index: Int)](./setvertexbytes%28_,length,attributestride,index%29.md)
- [func setVertexBufferOffset(Int, index: Int)](./setvertexbufferoffset%28_,index%29.md)
  Updates an entry in the vertex shader argument table with a new location within the entry’s current buffer.
- [func setVertexBufferOffset(offset: Int, attributeStride: Int, index: Int)](./setvertexbufferoffset%28offset,attributestride,index%29.md)
- [- setVertexBuffers:offsets:withRange:](./setvertexbuffers_offsets_withrange_.md)
  Assigns multiple buffers to a range of entries in the vertex shader argument table.
- [- setVertexBuffers:offsets:attributeStrides:withRange:](./setvertexbuffers_offsets_attributestrides_withrange_.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setvertexbuffer(_:offset:index:))*