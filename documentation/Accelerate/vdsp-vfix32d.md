# vDSP_vfix32D

**Framework**: Accelerate  
**Kind**: func

Converts a vector of double-precision floating-point values to signed 32-bit integer values, and rounds towards zero.

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
extern void vDSP_vfix32D(const double * __A, vDSP_Stride __IA, int * __C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

This function is the same as [`vDSP_vfix16`](https://developer.apple.com/documentation/kernel/1532172-vdsp_vfix16), except for the type of vector `A`.

## Parameters

- `__A`: The input vector.
- `__IA`: The distance between the elements in the input vector.
- `__C`: The output vector.
- `__IC`: The distance between the elements in the output vector.
- `__N`: The number of elements that the function processes.

## See Also

- [vDSP_vfixr32D](vdsp_vfixr32d.md)
  Converts a vector of double-precision floating-point values to signed 32-bit integer values, and rounds towards the nearest integer.
- [vDSP_vfixu32D](vdsp_vfixu32d.md)
  Converts a vector of double-precision floating-point values to unsigned 32-bit integer values, and rounds towards zero.
- [vDSP_vfixru32D](vdsp_vfixru32d.md)
  Converts a vector of double-precision floating-point values to unsigned 32-bit integer values, and rounds towards the nearest integer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vfix32d)*