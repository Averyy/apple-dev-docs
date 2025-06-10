# setBytes(_:length:attributeStride:index:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Copies data with a given stride directly to the GPU to populate an entry in the buffer argument table.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func setBytes(_ bytes: UnsafeRawPointer, length: Int, attributeStride stride: Int, index: Int)
```

#### Discussion

> ❗ **Important**:  This method only works for data smaller than 4 kilobytes that doesn’t persist. Create an [`MTLBuffer`](mtlbuffer.md) instance if your data exceeds 4 KB, needs to persist on the GPU, or you access results on the CPU.

This method allows Metal to copy data directly onto the GPU, rather than creating a new [`MTLBuffer`](mtlbuffer.md) instance and binding it. Binding data directly can improve performance, especially when making many small allocations.

## Parameters

- `bytes`: A pointer to the memory where the data to copy starts.
- `length`: The number of bytes to copy.
- `stride`: The number of bytes between the start of one element and the start of the next.
- `index`: The index the data binds to in the argument table.

## See Also

- [func setBytes(UnsafeRawPointer, length: Int, index: Int)](mtlcomputecommandencoder/setbytes(_:length:index:).md)
  Copies data directly to the GPU to populate an entry in the buffer argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/setbytes(_:length:attributestride:index:))*