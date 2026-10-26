# setBuffer(_:offset:attributeStride:index:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Binds a buffer with a stride to the buffer argument table, allowing compute kernels to access its data on the GPU.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func setBuffer(_ buffer: any MTLBuffer, offset: Int, attributeStride stride: Int, index: Int)
```

```objc
- (void) setBuffer:(id<MTLBuffer>) buffer offset:(NSUInteger) offset attributeStride:(NSUInteger) stride atIndex:(NSUInteger) index;
```

#### Discussion

> ❗ **Important**:  Only call this method when the buffer is part of [`stageInputDescriptor`](../mtlcomputepipelinedescriptor/stageinputdescriptor.md) and has its stride set to [`MTLBufferLayoutStrideDynamic`](../mtlbufferlayoutstridedynamic.md).

For buffers binding to an argument using the `device` address space, align the offset to the data type’s size. The maximum size for an offset is `16` bytes.

For buffers in the `constant` address space, the minimum alignment depends on the hardware running your app. See the [Metal feature set tables (PDF)](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) for information on each Apple GPU family.

Rebinding an already bound buffer causes a Metal error.

## Parameters

- `buffer`: The [`MTLBuffer`](../mtlbuffer.md) instance to bind to the argument table.
- `offset`: The number of bytes to skip in the buffer before the first element of data.
- `stride`: The number of bytes between the start of one element and the start of the next.
- `index`: The index the buffer binds to in the argument table.

## See Also

### Binding buffers
- [func setBuffer((any MTLBuffer)?, offset: Int, index: Int)](./setbuffer%28_,offset,index%29.md)
  Binds a buffer to the buffer argument table, allowing compute kernels to access its data on the GPU.
- [func setBuffers([(any MTLBuffer)?], offsets: [Int], range: Range<Int>)](./setbuffers%28_,offsets,range%29.md)
  Binds multiple buffers to the buffer argument table at once, allowing compute kernels to access their data on the GPU.
- [func setBuffers([(any MTLBuffer)?], offsets: [Int], attributeStrides: [Int], range: Range<Int>)](./setbuffers%28_,offsets,attributestrides,range%29.md)
  Binds multiple buffers with data in stride to the buffer argument table at once, allowing compute kernels to access their data on the GPU.
- [func setBufferOffset(Int, index: Int)](./setbufferoffset%28_,index%29.md)
  Changes where the data begins in a buffer already bound to the buffer argument table.
- [func setBufferOffset(offset: Int, attributeStride: Int, index: Int)](./setbufferoffset%28offset,attributestride,index%29.md)
  Changes where the data begins and the distance between adjacent elements in a buffer already bound to the buffer argument table.
- [- setBuffers:offsets:withRange:](./setbuffers_offsets_withrange_.md)
  Binds multiple buffers to the buffer argument table at once, allowing compute kernels to access their data on the GPU.
- [- setBuffers:offsets:attributeStrides:withRange:](./setbuffers_offsets_attributestrides_withrange_.md)
  Binds multiple buffers with data in stride to the buffer argument table at once, allowing compute kernels to access their data on the GPU.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/setbuffer(_:offset:attributestride:index:))*