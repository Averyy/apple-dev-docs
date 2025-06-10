# vDSP_vfltsm24

**Framework**: Accelerate  
**Kind**: func

Converts and scales a vector of signed 24-bit integers to single-precision floating-point values.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
extern void vDSP_vfltsm24(const vDSP_int24 * __A, vDSP_Stride __IA, const float * __B, float * __C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

The input and output values must point to different, non-overlapping regions of memory; it doesn’t work in-place.

## Parameters

- `__A`: The input vector.
- `__IA`: The distance between the elements in the input vector.
- `__B`: The single-precision scale factor.
- `__C`: The output vector.
- `__IC`: The distance between the elements in the output vector.
- `__N`: The number of elements that the function processes.

## See Also

- [vDSP_vflt24](vdsp_vflt24.md)
  Converts a vector of signed 24-bit integers to single-precision floating-point values.
- [vDSP_vfltu24](vdsp_vfltu24.md)
  Converts a vector of unsigned 24-bit integers to single-precision floating-point values.
- [vDSP_vfltsmu24](vdsp_vfltsmu24.md)
  Converts and scales a vector of unsigned 24-bit integers to single-precision floating-point values.
- [struct vDSP_int24](vdsp_int24.md)
  A data structure that holds a 24-bit signed integer value.
- [struct vDSP_uint24](vdsp_uint24.md)
  A data structure that holds a 24-bit unsigned integer value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vfltsm24)*