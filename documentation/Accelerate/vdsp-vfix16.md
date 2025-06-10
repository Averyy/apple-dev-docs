# vDSP_vfix16

**Framework**: Accelerate  
**Kind**: func

Converts a vector of single-precision floating-point values to signed 16-bit integer values, and rounds towards zero.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
extern void vDSP_vfix16(const float * __A, vDSP_Stride __IA, short * __C, vDSP_Stride __IC, vDSP_Length __N);
```

## Parameters

- `__A`: The input vector.
- `__IA`: The distance between the elements in the input vector.
- `__C`: The output vector.
- `__IC`: The distance between the elements in the output vector.
- `__N`: The number of elements that the function processes.

## See Also

- [vDSP_vfixr16](vdsp_vfixr16.md)
  Converts a vector of single-precision floating-point values to signed 16-bit integer values, and rounds towards the nearest integer.
- [vDSP_vfixu16](vdsp_vfixu16.md)
  Converts a vector of single-precision floating-point values to unsigned 16-bit integer values, and rounds towards zero.
- [vDSP_vfixru16](vdsp_vfixru16.md)
  Converts a vector of single-precision floating-point values to unsigned 16-bit integer values, and rounds towards the nearest integer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vfix16)*