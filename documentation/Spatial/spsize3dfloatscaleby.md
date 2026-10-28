# SPSize3DFloatScaleBy

**Framework**: Spatial  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```c
static SPSize3DFloat SPSize3DFloatScaleBy(SPSize3DFloat size, float x, float y, float z);
```

## Return Value

A size that’s scaled by the specified values.

## Discussion

Returns a size with dimensions scaled by the specified values.

## Parameters

- `size`: The source size.
- `x`: The scale value along the @p width dimension.
- `y`: The scale value along the @p height dimension.
- `z`: The scale value along the @p depth dimension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spsize3dfloatscaleby)*