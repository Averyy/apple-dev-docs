# vDSP_vsmfixu24

**Framework**: Accelerate  
**Kind**: func

Converts a vector of single-precision floating-point values to signed 24-bit integer values, and rounds towards the nearest integer.

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
extern void vDSP_vsmfixu24(const float * __A, vDSP_Stride __IA, const float * __B, vDSP_uint24 * __C, vDSP_Stride __IC, vDSP_Length __N);
```

## Parameters

- `__A`: The input vector.
- `__IA`: The distance between the elements in the input vector.
- `__B`: The scale that the function applies to source values before conversion.
- `__C`: The output vector.
- `__IC`: The distance between the elements in the output vector.
- `__N`: The number of elements that the function processes.

## See Also

- [vDSP_vsmfix24](vdsp_vsmfix24.md)
  Converts a vector of single-precision floating-point values to signed 24-bit integer values, and rounds towards zero.
- [struct vDSP_int24](vdsp_int24.md)
  A data structure that holds a 24-bit signed integer value.
- [struct vDSP_uint24](vdsp_uint24.md)
  A data structure that holds a 24-bit unsigned integer value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vsmfixu24)*