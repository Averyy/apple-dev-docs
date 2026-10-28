# MTLPackedFloat4x3

**Framework**: Metal  
**Kind**: struct  
**Role**: Structure

A structure that contains the top three rows of a 4x4 matrix of 32-bit floating-point values, in column-major order.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```c
typedef struct _MTLPackedFloat4x3 { ... } MTLPackedFloat4x3;
```

## Overview

Metal uses the values `[0,0,0,1]` as the bottom row of the `4x4` matrix.

## Topics

### Instance Properties
- [columns](./mtlpackedfloat4x3-c.struct/columns.md)

## See Also

### Supporting types
- [MTLAxisAlignedBoundingBox](./mtlaxisalignedboundingbox-c.struct.md)
  The bounds for an axis-aligned bounding box.
- [MTLPackedFloat3](./mtlpackedfloat3-c.struct.md)
  A structure that contains three 32-bit floating-point values with no additional padding.
- [func MTLPackedFloat3Make(Float, Float, Float) -> MTLPackedFloat3](./mtlpackedfloat3make%28_,_,_%29.md)
  Returns a new packed vector with three floating-point values.
- [struct MTL4BufferRange](./mtl4bufferrange.md)
- [func MTL4BufferRangeMake(MTLGPUAddress, UInt64) -> MTL4BufferRange](./mtl4bufferrangemake%28_,_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlpackedfloat4x3-c.struct)*