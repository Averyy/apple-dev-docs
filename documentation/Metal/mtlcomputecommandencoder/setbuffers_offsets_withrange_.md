# setBuffers:offsets:withRange:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Binds multiple buffers to the buffer argument table at once, allowing compute kernels to access their data on the GPU.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```objc
- (void) setBuffers:(id<MTLBuffer> const[]) buffers offsets:(const NSUInteger[]) offsets withRange:(NSRange) range;
```

#### Discussion

> ❗ **Important**:  This method requires that the length of `buffers` and `offsets` are equal to the length of `range`.

For buffers binding to an argument using the `device` address space, align the offset to the data type’s size. The maximum size for an offset is `16` bytes.

For buffers in the `constant` address space, the minimum alignment depends on the hardware running your app. See the [Metal feature set tables (PDF)](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) for information on each Apple GPU family.

Rebinding an already bound buffer causes a Metal error.

## Parameters

- `buffers`: The [`MTLBuffer`](../mtlbuffer.md) instances to bind to the buffer argument table.
- `offsets`: An array of offsets, each of which specifies where the data begins, in bytes, from the start of its corresponding buffer.
- `range`: The argument table indices to bind each of the `buffers` to, in the order they appear.

## See Also

### Binding buffers
- [func setBuffer((any MTLBuffer)?, offset: Int, index: Int)](./setbuffer%28_,offset,index%29.md)
  Binds a buffer to the buffer argument table, allowing compute kernels to access its data on the GPU.
- [func setBuffer(any MTLBuffer, offset: Int, attributeStride: Int, index: Int)](./setbuffer%28_,offset,attributestride,index%29.md)
  Binds a buffer with a stride to the buffer argument table, allowing compute kernels to access its data on the GPU.
- [- setBuffers:offsets:attributeStrides:withRange:](./setbuffers_offsets_attributestrides_withrange_.md)
  Binds multiple buffers with data in stride to the buffer argument table at once, allowing compute kernels to access their data on the GPU.
- [func setBufferOffset(Int, index: Int)](./setbufferoffset%28_,index%29.md)
  Changes where the data begins in a buffer already bound to the buffer argument table.
- [func setBufferOffset(offset: Int, attributeStride: Int, index: Int)](./setbufferoffset%28offset,attributestride,index%29.md)
  Changes where the data begins and the distance between adjacent elements in a buffer already bound to the buffer argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/setbuffers:offsets:withrange:)*