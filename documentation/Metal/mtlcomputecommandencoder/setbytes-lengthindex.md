# setBytes(_:length:index:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Copies data directly to the GPU to populate an entry in the buffer argument table.

**Availability**:
- iOS 8.3+
- iPadOS 8.3+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func setBytes(_ bytes: UnsafeRawPointer, length: Int, index: Int)
```

#### Discussion

> ❗ **Important**:  This method only works for data smaller than 4 kilobytes that doesn’t persist. Create an [`MTLBuffer`](mtlbuffer.md) instance if your data exceeds 4 KB, needs to persist on the GPU, or you access results on the CPU.

 This method only works for data smaller than 4 kilobytes that doesn’t persist. Create an [`MTLBuffer`](mtlbuffer.md) instance if your data exceeds 4 KB, needs to persist on the GPU, or you access results on the CPU.

This method allows Metal to copy data efficiently onto the GPU without the need for your own buffer. Binding data directly can improve performance, especially when making many small allocations.

## Parameters

- `bytes`: A pointer to where the data to copy starts.
- `length`: The number of bytes to copy.
- `index`: The index the data binds to in the argument table.

## See Also

- [func setBytes(UnsafeRawPointer, length: Int, attributeStride: Int, index: Int)](mtlcomputecommandencoder/setbytes(_:length:attributestride:index:).md)
  Copies data with a given stride directly to the GPU to populate an entry in the buffer argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/setbytes(_:length:index:))*