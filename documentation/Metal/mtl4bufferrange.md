# MTL4BufferRange

**Framework**: Metal  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
struct MTL4BufferRange
```

```c
typedef struct MTL4BufferRange { ... } MTL4BufferRange;
```

#### Overview

A struct representing a range of a Metal buffer. The offset into the buffer is included in the address. The length is generally optional, which a value of (uint64_t)-1 representing the range from the given address to the end of the buffer. However, providing the length can enable more accurate API validation, especially when sub-allocating ranges of a buffer.

## Topics

### Initializers
- [init()](./mtl4bufferrange/init%28%29.md)
- [init(bufferAddress: MTLGPUAddress, length: UInt64)](./mtl4bufferrange/init%28bufferaddress,length%29.md)
### Instance Properties
- [var bufferAddress: MTLGPUAddress](./mtl4bufferrange/bufferaddress.md)
- [var length: UInt64](./mtl4bufferrange/length.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

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
- [func MTL4BufferRangeMake(MTLGPUAddress, UInt64) -> MTL4BufferRange](./mtl4bufferrangemake%28_,_%29.md)
- [MTLAxisAlignedBoundingBox](./mtlaxisalignedboundingbox-c.struct.md)
  The bounds for an axis-aligned bounding box.
- [MTLPackedFloat3](./mtlpackedfloat3-c.struct.md)
  A structure that contains three 32-bit floating-point values with no additional padding.
- [MTLPackedFloat4x3](./mtlpackedfloat4x3-c.struct.md)
  A structure that contains the top three rows of a 4x4 matrix of 32-bit floating-point values, in column-major order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4bufferrange)*