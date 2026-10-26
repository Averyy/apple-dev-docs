# SPScaledPose3DFloatMakeWithProjectiveTransform

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
static SPScaledPose3DFloat SPScaledPose3DFloatMakeWithProjectiveTransform(SPProjectiveTransform3DFloat transform);
```

#### Return Value

A scaled pose with a scale, position and rotation that are defined by a projective transform.

#### Discussion

Returns a scaled pose with with a position, rotation, and scale that are defined by a projective transform.

> **Note**: This function can’t extract rotation from a non-scale-rotate-translate projective transform. In that case, the function returns @p SPScaledPose3DFloatInvalid. If the specified  @p SPProjectiveTransform3DFloat doesn’t have uniform scale (that is,  @p SPProjectiveTransform3DFloatIsUniform returns  @p false) the function returns

## Parameters

- `transform`: The source transform. The function only considers the transform’s scale, rotation, and translation components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spscaledpose3dfloatmakewithprojectivetransform)*