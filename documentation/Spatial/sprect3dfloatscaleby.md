# SPRect3DFloatScaleBy

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
static SPRect3DFloat SPRect3DFloatScaleBy(SPRect3DFloat rect, float x, float y, float z);
```

#### Return Value

A rectangle that’s scaled by the specified values.

#### Discussion

Returns a rectangle with dimensions scaled by the specified values.

## Parameters

- `rect`: The source rectangle.
- `x`: The scale value along the @p width dimension.
- `y`: The scale value along the @p height dimension.
- `z`: The scale value along the @p depth dimension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/sprect3dfloatscaleby)*