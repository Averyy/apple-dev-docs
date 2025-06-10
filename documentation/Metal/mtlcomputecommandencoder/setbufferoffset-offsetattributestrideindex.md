# setBufferOffset(offset:attributeStride:index:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Changes where the data begins and the distance between adjacent elements in a buffer already bound to the buffer argument table.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func setBufferOffset(offset: Int, attributeStride stride: Int, index: Int)
```

#### Discussion

> ❗ **Important**:  Only call this method when the buffer is part of [`stageInputDescriptor`](mtlcomputepipelinedescriptor/stageinputdescriptor.md) and has its stride set to [`MTLBufferLayoutStrideDynamic`](mtlbufferlayoutstridedynamic.md).

_ _Prefer calling this method to unbinding and then rebinding data.

For buffers binding to an argument using the `device` address space, align the offset to the data type’s size. The maximum size for an offset is `16` bytes.

For buffers in the `constant` address space, the minimum alignment depends on the hardware running your app. See the [`Metal feature set tables (PDF)`](https://developer.apple.comhttps://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) for information on each Apple GPU family.

## Parameters

- `offset`: Where the data to bind begins, in bytes, from the start of the bound buffer.
- `stride`: The number of bytes between the start of one element and the start of the next.
- `index`: The index of the buffer to change in the argument table.

## See Also

- [func setBuffer((any MTLBuffer)?, offset: Int, index: Int)](mtlcomputecommandencoder/setbuffer(_:offset:index:).md)
  Binds a buffer to the buffer argument table, allowing compute kernels to access its data on the GPU.
- [func setBuffer(any MTLBuffer, offset: Int, attributeStride: Int, index: Int)](mtlcomputecommandencoder/setbuffer(_:offset:attributestride:index:).md)
  Binds a buffer with a stride to the buffer argument table, allowing compute kernels to access its data on the GPU.
- [func setBuffers([(any MTLBuffer)?], offsets: [Int], range: Range<Int>)](mtlcomputecommandencoder/setbuffers(_:offsets:range:).md)
  Binds multiple buffers to the buffer argument table at once, allowing compute kernels to access their data on the GPU.
- [func setBuffers([(any MTLBuffer)?], offsets: [Int], attributeStrides: [Int], range: Range<Int>)](mtlcomputecommandencoder/setbuffers(_:offsets:attributestrides:range:).md)
  Binds multiple buffers with data in stride to the buffer argument table at once, allowing compute kernels to access their data on the GPU.
- [func setBufferOffset(Int, index: Int)](mtlcomputecommandencoder/setbufferoffset(_:index:).md)
  Changes where the data begins in a buffer already bound to the buffer argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/setbufferoffset(offset:attributestride:index:))*