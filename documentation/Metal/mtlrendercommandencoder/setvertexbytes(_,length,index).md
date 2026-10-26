# setVertexBytes(_:length:index:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Creates a buffer from bytes and assigns it to an entry in the vertex shader argument table.

**Availability**:
- iOS 8.3+
- iPadOS 8.3+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func setVertexBytes(_ bytes: UnsafeRawPointer, length: Int, index: Int)
```

```objc
- (void) setVertexBytes:(const void *) bytes length:(NSUInteger) length atIndex:(NSUInteger) index;
```

#### Discussion

The method is equivalent to creating an [`MTLBuffer`](../mtlbuffer.md) instance that contains the same data as `bytes` and calling the [`setVertexBuffer(_:offset:index:)`](./setvertexbuffer%28_,offset,index%29.md) method. However, this method avoids the overhead of creating a buffer to store your data; instead, Metal manages the data.

> ❗ **Important**:  Only call this method for single-use data that’s smaller than 4 KB.

For data that’s more than 4 KB, create an [`MTLBuffer`](../mtlbuffer.md) instance and pass it to [`setVertexBuffer(_:offset:index:)`](./setvertexbuffer%28_,offset,index%29.md).

By default, the buffer at each index is `nil`.

## Parameters

- `bytes`: A pointer to argument data the method copies to an [`MTLBuffer`](../mtlbuffer.md) and assigns to an entry in the vertex shader argument table for buffers.
- `length`: The number of bytes the method copies from the `bytes` pointer.
- `index`: An integer that represents the entry in the vertex shader argument table for buffers that stores a record of the [`MTLBuffer`](../mtlbuffer.md) the method creates from `bytes`.

## See Also

### Assigning buffers
- [func setVertexBuffer((any MTLBuffer)?, offset: Int, index: Int)](./setvertexbuffer%28_,offset,index%29.md)
  Assigns a buffer to an entry in the vertex shader argument table.
- [func setVertexBuffer((any MTLBuffer)?, offset: Int, attributeStride: Int, index: Int)](./setvertexbuffer%28_,offset,attributestride,index%29.md)
- [func setVertexBuffers([(any MTLBuffer)?], offsets: [Int], range: Range<Int>)](./setvertexbuffers%28_,offsets,range%29.md)
  Assigns multiple buffers to a range of entries in the vertex shader argument table.
- [func setVertexBuffers([(any MTLBuffer)?], offsets: [Int], attributeStrides: [Int], range: Range<Int>)](./setvertexbuffers%28_,offsets,attributestrides,range%29.md)
- [func setVertexBytes(UnsafeRawPointer, length: Int, attributeStride: Int, index: Int)](./setvertexbytes%28_,length,attributestride,index%29.md)
- [func setVertexBufferOffset(Int, index: Int)](./setvertexbufferoffset%28_,index%29.md)
  Updates an entry in the vertex shader argument table with a new location within the entry’s current buffer.
- [func setVertexBufferOffset(offset: Int, attributeStride: Int, index: Int)](./setvertexbufferoffset%28offset,attributestride,index%29.md)
- [- setVertexBuffers:offsets:withRange:](./setvertexbuffers_offsets_withrange_.md)
  Assigns multiple buffers to a range of entries in the vertex shader argument table.
- [- setVertexBuffers:offsets:attributeStrides:withRange:](./setvertexbuffers_offsets_attributestrides_withrange_.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setvertexbytes(_:length:index:))*