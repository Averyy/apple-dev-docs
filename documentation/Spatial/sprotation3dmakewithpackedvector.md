# SPRotation3DMakeWithPackedVector

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
static SPRotation3D SPRotation3DMakeWithPackedVector(simd_packed_double4 source);
```

#### Return Value

A new rotation structure.

#### Discussion

Creates a Spatial rotation structure from a packed simd vector.

## Parameters

- `source`: The source vector that supplies the imaginary part of the quaternion from elements `0`, `1`, and `2`; and the real part from element `3`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/sprotation3dmakewithpackedvector)*