# SPPose3DFloatMakeWith4x4Matrix

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
static SPPose3DFloat SPPose3DFloatMakeWith4x4Matrix(simd_float4x4 matrix);
```

## Return Value

A new pose structure.

## Discussion

Returns a new pose structure from the specified 4 x 4 matrix.

> **Note**: This function can’t extract rotation from a non-scale-rotate-translate matrix transform. In that case, the function returns @p SPPose3DFloatInvalid.

## Parameters

- `matrix`: The source matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/sppose3dfloatmakewith4x4matrix)*