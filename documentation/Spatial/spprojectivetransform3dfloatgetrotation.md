# SPProjectiveTransform3DFloatGetRotation

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
static SPRotation3DFloat SPProjectiveTransform3DFloatGetRotation(SPProjectiveTransform3DFloat transform);
```

## Return Value

A rotation structure that represents the transform’s rotation.

## Discussion

Returns a projective transform’s rotation.

> **Note**: This function computes the rotation from the first three rows of the transform matrix and ignores the fourth row. If the projective transform isn’t an affine scale-rotate-translate transform, this function returns @p SPRotation3DFloatInvalid.

## Parameters

- `transform`: The source transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spprojectivetransform3dfloatgetrotation)*