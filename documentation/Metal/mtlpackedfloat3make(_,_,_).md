# MTLPackedFloat3Make(_:_:_:)

**Framework**: Metal  
**Kind**: func  
**Role**: Function

Returns a new packed vector with three floating-point values.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
func MTLPackedFloat3Make(_ x: Float, _ y: Float, _ z: Float) -> MTLPackedFloat3
```

```c
static MTLPackedFloat3 MTLPackedFloat3Make(float x, float y, float z);
```

## Parameters

- `x`: The vector’s x coordinate.
- `y`: The vector’s y coordinate.
- `z`: The vector’s z coordinate.

## See Also

### Supporting types
- [typealias MTLAxisAlignedBoundingBox](./mtlaxisalignedboundingbox-swift.typealias.md)
  The bounds for an axis-aligned bounding box.
- [typealias MTLPackedFloat3](./mtlpackedfloat3-swift.typealias.md)
  }
- [typealias MTLPackedFloat4x3](./mtlpackedfloat4x3-swift.typealias.md)
  A structure that contains the top three rows of a 4x4 matrix of 32-bit floating-point values, in column-major order.
- [struct MTL4BufferRange](./mtl4bufferrange.md)
- [func MTL4BufferRangeMake(MTLGPUAddress, UInt64) -> MTL4BufferRange](./mtl4bufferrangemake%28_,_%29.md)
- [MTLAxisAlignedBoundingBox](./mtlaxisalignedboundingbox-c.struct.md)
  The bounds for an axis-aligned bounding box.
- [MTLPackedFloat3](./mtlpackedfloat3-c.struct.md)
  A structure that contains three 32-bit floating-point values with no additional padding.
- [MTLPackedFloat4x3](./mtlpackedfloat4x3-c.struct.md)
  A structure that contains the top three rows of a 4x4 matrix of 32-bit floating-point values, in column-major order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlpackedfloat3make(_:_:_:))*