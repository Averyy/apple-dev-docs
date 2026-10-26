# MTL4BufferRangeMake(_:_:)

**Framework**: Metal  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
func MTL4BufferRangeMake(_ bufferAddress: MTLGPUAddress, _ length: UInt64) -> MTL4BufferRange
```

```c
static MTL4BufferRange MTL4BufferRangeMake(MTLGPUAddress bufferAddress, uint64_t length);
```

#### Discussion

Create a buffer range from a buffer’s GPU address (given by the gpuAddress property) and length. A length of (uint64_t)-1 represents the the range from the given address to the end of the buffer.

## See Also

### Supporting types
- [typealias MTLAxisAlignedBoundingBox](./mtlaxisalignedboundingbox-swift.typealias.md)
  The bounds for an axis-aligned bounding box.
- [typealias MTLPackedFloat3](./mtlpackedfloat3-swift.typealias.md)
  }
- [typealias MTLPackedFloat4x3](./mtlpackedfloat4x3-swift.typealias.md)
  A structure that contains the top three rows of a 4x4 matrix of 32-bit floating-point values, in column-major order.
- [func MTLPackedFloat3Make(Float, Float, Float) -> MTLPackedFloat3](./mtlpackedfloat3make%28_,_,_%29.md)
  Returns a new packed vector with three floating-point values.
- [struct MTL4BufferRange](./mtl4bufferrange.md)
- [MTLAxisAlignedBoundingBox](./mtlaxisalignedboundingbox-c.struct.md)
  The bounds for an axis-aligned bounding box.
- [MTLPackedFloat3](./mtlpackedfloat3-c.struct.md)
  A structure that contains three 32-bit floating-point values with no additional padding.
- [MTLPackedFloat4x3](./mtlpackedfloat4x3-c.struct.md)
  A structure that contains the top three rows of a 4x4 matrix of 32-bit floating-point values, in column-major order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4bufferrangemake(_:_:))*