# SPAffineTransform3DFloatGetRotation

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
static SPRotation3DFloat SPAffineTransform3DFloatGetRotation(SPAffineTransform3DFloat transform);
```

#### Return Value

A rotation structure that represents the transform’s rotation.

#### Discussion

Returns an affine transform’s rotation.

> **Note**: This function can’t extract rotation from a non-scale-rotate-translate affine transform. In that case, the function returns @p SPRotation3DFloatInvalid.

## Parameters

- `transform`: The source transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spaffinetransform3dfloatgetrotation)*