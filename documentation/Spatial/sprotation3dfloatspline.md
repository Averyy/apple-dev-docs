# SPRotation3DFloatSpline

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
static SPRotation3DFloat SPRotation3DFloatSpline(SPRotation3DFloat r0, SPRotation3DFloat r1, SPRotation3DFloat r2, SPRotation3DFloat r3, float t);
```

## Return Value

A new rotation that’s the interpolated value between the two rotations along a spherical cubic spline.

## Discussion

Returns an interpolated value between two rotations along a spherical cubic spline.

The function interpolates between @p r1 and @p r2. @p r0 is the left endpoint of the previous interval, and @p r3 is the right endpoint of the next interval. Use this function to smoothly interpolate between a sequence of rotations.

## Parameters

- `r0`: The left endpoint of the previous interval.
- `r1`: The starting rotation.
- `r2`: The ending rotation.
- `r3`: The right endpoint of the next interval.
- `t`: The value, between @p 0 and @p 1, that the function interpolates at.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/sprotation3dfloatspline)*