# MTLPackedFloat4x3

**Framework**: Metal  
**Kind**: typealias

A structure that contains the top three rows of a 4x4 matrix of 32-bit floating-point values, in column-major order.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
typealias MTLPackedFloat4x3 = _MTLPackedFloat4x3
```

#### Discussion

Metal uses the values `[0,0,0,1]` as the bottom row of the `4x4` matrix.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [typealias MTLAxisAlignedBoundingBox](mtlaxisalignedboundingbox-swift.typealias.md)
  The bounds for an axis-aligned bounding box.
- [typealias MTLPackedFloat3](mtlpackedfloat3-swift.typealias.md)
  }
- [func MTLPackedFloat3Make(Float, Float, Float) -> MTLPackedFloat3](mtlpackedfloat3make(_:_:_:).md)
  Returns a new packed vector with three floating-point values.
- [struct MTL4BufferRange](mtl4bufferrange.md)
- [func MTL4BufferRangeMake(MTLGPUAddress, UInt64) -> MTL4BufferRange](mtl4bufferrangemake(_:_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlpackedfloat4x3-swift.typealias)*