# vDSP_vfixr16D

**Framework**: Accelerate  
**Kind**: func

Converts a vector of double-precision floating-point values to signed 16-bit integer values, and rounds towards the nearest integer.

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
extern void vDSP_vfixr16D(const double * __A, vDSP_Stride __IA, short * __C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

This function is the same as [`vDSP_vfixr16`](vdsp_vfixr16.md), except for the type of vector `A`.

## Parameters

- `__A`: The input vector.
- `__IA`: The distance between the elements in the input vector.
- `__C`: The output vector.
- `__IC`: The distance between the elements in the output vector.
- `__N`: The number of elements that the function processes.

## See Also

- [vDSP_vfix16D](vdsp_vfix16d.md)
  Converts a vector of double-precision floating-point values to signed 16-bit integer values, and rounds towards zero.
- [vDSP_vfixu16D](vdsp_vfixu16d.md)
  Converts a vector of double-precision floating-point values to unsigned 16-bit integer values, and rounds towards zero.
- [vDSP_vfixru16D](vdsp_vfixru16d.md)
  Converts a vector of double-precision floating-point values to unsigned 16-bit integer values, and rounds towards the nearest integer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vfixr16d)*