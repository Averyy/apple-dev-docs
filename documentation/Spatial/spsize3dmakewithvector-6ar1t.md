# SPSize3DMakeWithVector

**Framework**: Spatial  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```c
static SPSize3D SPSize3DMakeWithVector(simd_double3 xyz);
```

## Return Value

A new size stucture.

## Discussion

Creates a size structure with dimensions specified as a 3-element SIMD vector.

## Parameters

- `xyz`: The source vector.

## See Also

### Creating a 3D size structure
- [SPSize3DMakeWithPoint](./spsize3dmakewithpoint.md)
  Creates a size structure from the specified Spatial point.
- [SPSize3DMakeWithVector](./spsize3dmakewithvector-5cgfq.md)
  Creates a size structure from the specified double-precision vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spsize3dmakewithvector-6ar1t)*