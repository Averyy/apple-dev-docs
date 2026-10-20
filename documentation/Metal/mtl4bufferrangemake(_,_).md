# MTL4BufferRangeMake(_:_:)

**Framework**: Metal  
**Kind**: func

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
func MTL4BufferRangeMake(_ bufferAddress: MTLGPUAddress, _ length: UInt64) -> MTL4BufferRange
```

#### Discussion

Create a buffer range from a buffer’s GPU address (given by the gpuAddress property) and length. A length of (uint64_t)-1 represents the the range from the given address to the end of the buffer.

## See Also

- [typealias MTLAxisAlignedBoundingBox](mtlaxisalignedboundingbox-swift.typealias.md)
  The bounds for an axis-aligned bounding box.
- [typealias MTLPackedFloat3](mtlpackedfloat3-swift.typealias.md)
  }
- [typealias MTLPackedFloat4x3](mtlpackedfloat4x3-swift.typealias.md)
  A structure that contains the top three rows of a 4x4 matrix of 32-bit floating-point values, in column-major order.
- [func MTLPackedFloat3Make(Float, Float, Float) -> MTLPackedFloat3](mtlpackedfloat3make(_:_:_:).md)
  Returns a new packed vector with three floating-point values.
- [struct MTL4BufferRange](mtl4bufferrange.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4bufferrangemake(_:_:))*