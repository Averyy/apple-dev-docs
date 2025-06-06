# setBuffer(_:offset:index:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Binds a buffer to the buffer argument table, allowing compute kernels to access its data on the GPU.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func setBuffer(_ buffer: (any MTLBuffer)?, offset: Int, index: Int)
```

## Mentions

- [Improving CPU Performance by Using Argument Buffers](improving-cpu-performance-by-using-argument-buffers.md)

#### Discussion

For buffers binding to an argument using the `device` address space, align the offset to the data type’s size. The maximum size for an offset is `16` bytes.

For buffers in the `constant` address space, the minimum alignment depends on the hardware running your app. See the [`Metal feature set tables (PDF)`](https://developer.apple.comhttps://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) for information on each Apple GPU family.

Rebinding an already bound buffer causes a Metal error.

## Parameters

- `buffer`: The   instance to bind to the argument table.
- `offset`: The number of bytes to skip in the buffer before the first element of data.
- `index`: The index the buffer binds to in the argument table.

## See Also

- [func setBuffer(any MTLBuffer, offset: Int, attributeStride: Int, index: Int)](mtlcomputecommandencoder/setbuffer(_:offset:attributestride:index:).md)
  Binds a buffer with a stride to the buffer argument table, allowing compute kernels to access its data on the GPU.
- [func setBuffers([(any MTLBuffer)?], offsets: [Int], range: Range<Int>)](mtlcomputecommandencoder/setbuffers(_:offsets:range:).md)
  Binds multiple buffers to the buffer argument table at once, allowing compute kernels to access their data on the GPU.
- [func setBuffers([(any MTLBuffer)?], offsets: [Int], attributeStrides: [Int], range: Range<Int>)](mtlcomputecommandencoder/setbuffers(_:offsets:attributestrides:range:).md)
  Binds multiple buffers with data in stride to the buffer argument table at once, allowing compute kernels to access their data on the GPU.
- [func setBufferOffset(Int, index: Int)](mtlcomputecommandencoder/setbufferoffset(_:index:).md)
  Changes where the data begins in a buffer already bound to the buffer argument table.
- [func setBufferOffset(offset: Int, attributeStride: Int, index: Int)](mtlcomputecommandencoder/setbufferoffset(offset:attributestride:index:).md)
  Changes where the data begins and the distance between adjacent elements in a buffer already bound to the buffer argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/setbuffer(_:offset:index:))*