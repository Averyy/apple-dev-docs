# SPPose3DFloatMakeWithAffineTransform

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
static SPPose3DFloat SPPose3DFloatMakeWithAffineTransform(SPAffineTransform3DFloat transform);
```

#### Return Value

A pose with a position and rotation that are defined by an affine transform.

#### Discussion

Returns a pose with with a position and rotation that are defined by an affine transform.

> **Note**: This function can’t extract rotation from a non-scale-rotate-translate affine transform. In that case, the function returns @p SPPose3DFloatInvalid.

## Parameters

- `transform`: The source transform. The function only considers the transform’s rotation and translation components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/sppose3dfloatmakewithaffinetransform)*