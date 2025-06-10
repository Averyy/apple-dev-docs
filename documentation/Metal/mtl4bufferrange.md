# MTL4BufferRange

**Framework**: Metal  
**Kind**: struct

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct MTL4BufferRange
```

#### Overview

The length is generally optional, which a value of (uint64_t)-1 representing the range from the given address to the end of the buffer. However, providing the length can enable more accurate API validation, especially when sub-allocating ranges of a buffer.

## Topics

### Initializers
- [init()](mtl4bufferrange/init.md)
- [init(bufferAddress: UInt64, length: UInt64)](mtl4bufferrange/init(bufferaddress:length:).md)
### Instance Properties
- [var bufferAddress: UInt64](mtl4bufferrange/bufferaddress.md)
- [var length: UInt64](mtl4bufferrange/length.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [typealias MTLAxisAlignedBoundingBox](mtlaxisalignedboundingbox-swift.typealias.md)
  The bounds for an axis-aligned bounding box.
- [typealias MTLPackedFloat3](mtlpackedfloat3-swift.typealias.md)
  }
- [typealias MTLPackedFloat4x3](mtlpackedfloat4x3-swift.typealias.md)
  A structure that contains the top three rows of a 4x4 matrix of 32-bit floating-point values, in column-major order.
- [func MTLPackedFloat3Make(Float, Float, Float) -> MTLPackedFloat3](mtlpackedfloat3make(_:_:_:).md)
  Returns a new packed vector with three floating-point values.
- [func MTL4BufferRangeMake(UInt64, UInt64) -> MTL4BufferRange](mtl4bufferrangemake(_:_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4bufferrange)*