# SPProjectiveTransform3DFloatScaleUniform

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
static SPProjectiveTransform3DFloat SPProjectiveTransform3DFloatScaleUniform(SPProjectiveTransform3DFloat transform, float scale);
```

#### Return Value

A transform that’s uniformly scaled by the specified value.

#### Discussion

Returns a projective transform that’s constructed by concatenating an existing projective transform and a uniform scale.

## Parameters

- `transform`: The source transform.
- `scale`: The scale value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spprojectivetransform3dfloatscaleuniform)*