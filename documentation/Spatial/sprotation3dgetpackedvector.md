# SPRotation3DGetPackedVector

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
static simd_packed_double4 SPRotation3DGetPackedVector(SPRotation3D rotation);
```

#### Return Value

A new packed simd vector, where elements `0`, `1`, and `2` are the imaginary parts, and element `3` is the real part.

#### Discussion

Creates a packed simd vector from a Spatial rotation structure.

## Parameters

- `rotation`: The source rotation structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/sprotation3dgetpackedvector)*