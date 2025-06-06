# setBuffers(_:offsets:range:)

**Framework**: Metal  
**Kind**: method

Binds multiple buffers to the buffer argument table at once, allowing compute kernels to access their data on the GPU.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst ?+
- macOS 10.11+
- tvOS 8.0+
- visionOS ?+

## Declaration

```swift
func setBuffers(_ buffers: [(any MTLBuffer)?], offsets: [Int], range: Range<Int>)
```

#### Discussion

> ❗ **Important**:  This method requires that the length of `buffers` and `offsets` are equal to the length of `range`.

 This method requires that the length of `buffers` and `offsets` are equal to the length of `range`.

For buffers binding to an argument using the `device` address space, align the offset to the data type’s size. The maximum size for an offset is `16` bytes.

For buffers in the `constant` address space, the minimum alignment depends on the hardware running your app. See the [`Metal feature set tables (PDF)`](https://developer.apple.comhttps://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) for information on each Apple GPU family.

Rebinding an already bound buffer causes a Metal error.

## Parameters

- `buffers`: The   instances to bind to the buffer argument table.
- `offsets`: An array of offsets, each of which specifies where the data begins, in bytes, from the start of its corresponding buffer.
- `range`: The argument table indices to bind each of the   to, in the order they appear.

## See Also

- [func setBuffer((any MTLBuffer)?, offset: Int, index: Int)](mtlcomputecommandencoder/setbuffer(_:offset:index:).md)
  Binds a buffer to the buffer argument table, allowing compute kernels to access its data on the GPU.
- [func setBuffer(any MTLBuffer, offset: Int, attributeStride: Int, index: Int)](mtlcomputecommandencoder/setbuffer(_:offset:attributestride:index:).md)
  Binds a buffer with a stride to the buffer argument table, allowing compute kernels to access its data on the GPU.
- [func setBuffers([(any MTLBuffer)?], offsets: [Int], attributeStrides: [Int], range: Range<Int>)](mtlcomputecommandencoder/setbuffers(_:offsets:attributestrides:range:).md)
  Binds multiple buffers with data in stride to the buffer argument table at once, allowing compute kernels to access their data on the GPU.
- [func setBufferOffset(Int, index: Int)](mtlcomputecommandencoder/setbufferoffset(_:index:).md)
  Changes where the data begins in a buffer already bound to the buffer argument table.
- [func setBufferOffset(offset: Int, attributeStride: Int, index: Int)](mtlcomputecommandencoder/setbufferoffset(offset:attributestride:index:).md)
  Changes where the data begins and the distance between adjacent elements in a buffer already bound to the buffer argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/setbuffers(_:offsets:range:))*