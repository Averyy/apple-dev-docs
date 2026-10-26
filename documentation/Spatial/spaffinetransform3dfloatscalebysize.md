# SPAffineTransform3DFloatScaleBySize

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
static SPAffineTransform3DFloat SPAffineTransform3DFloatScaleBySize(SPAffineTransform3DFloat transform, SPSize3DFloat scale);
```

#### Return Value

A transform that’s scaled by the specified value.

#### Discussion

Returns an affine transform that’s constructed by concatenating an existing affine transform and a scale specified by an @p SPSize3DFloat structure.

## Parameters

- `transform`: The source transform.
- `scale`: The scale value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spaffinetransform3dfloatscalebysize)*