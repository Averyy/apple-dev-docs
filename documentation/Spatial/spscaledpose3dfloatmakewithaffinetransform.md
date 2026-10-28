# SPScaledPose3DFloatMakeWithAffineTransform

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
static SPScaledPose3DFloat SPScaledPose3DFloatMakeWithAffineTransform(SPAffineTransform3DFloat transform);
```

## Return Value

A scaled pose with a position and rotation that are defined by an affine transform.

## Discussion

Returns a scaled pose with with a position, rotation, and scale that are defined by an affine transform.

> **Note**: This function can’t extract rotation from a non-scale-rotate-translate affine transform. In that case, the function returns @p SPScaledPose3DFloatInvalid. If the specified  @p SPAffineTransform3DFloat doesn’t have uniform scale (that is,  @p SPAffineTransform3DFloatIsUniform returns  @p false), the function returns

## Parameters

- `transform`: The source transform. The function only considers the transform’s scale, rotation, and translation components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spscaledpose3dfloatmakewithaffinetransform)*