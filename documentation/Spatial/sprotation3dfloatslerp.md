# SPRotation3DFloatSlerp

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
static SPRotation3DFloat SPRotation3DFloatSlerp(SPRotation3DFloat from, SPRotation3DFloat to, float t);
```

## Return Value

A new rotation. When @p t=0, the result is the @p from rotation. When @p t=1.0, the result is the @p to rotation. For any other value of @p t, the result is a spherical linear interpolation between the two rotations.

## Discussion

Returns the spherical linear interpolation along the shortest arc between two rotations.

## Parameters

- `from`: The starting rotation.
- `to`: The ending rotation.
- `t`: The value, between @p 0 and @p 1, that the function interpolates at.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/sprotation3dfloatslerp)*