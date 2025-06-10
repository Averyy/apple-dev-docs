# vDSP_vfixr32

**Framework**: Accelerate  
**Kind**: func

Converts a vector of single-precision floating-point values to signed 32-bit integer values, and rounds towards the nearest integer.

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
extern void vDSP_vfixr32(const float * __A, vDSP_Stride __IA, int * __C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

If the resulting value is outside the bounds of the output type, the behavior is undefined. If you need to handle out-of-bounds data, you should use one of the functions in Clipping Operations on the data first.

## Parameters

- `__A`: The input vector.
- `__IA`: The distance between the elements in the input vector.
- `__C`: The output vector.
- `__IC`: The distance between the elements in the output vector.
- `__N`: The number of elements that the function processes.

## See Also

- [vDSP_vfix32](vdsp_vfix32.md)
  Converts a vector of single-precision floating-point values to signed 32-bit integer values, and rounds towards zero.
- [vDSP_vfixu32](vdsp_vfixu32.md)
  Converts a vector of single-precision floating-point values to unsigned 32-bit integer values, and rounds towards zero.
- [vDSP_vfixru32](vdsp_vfixru32.md)
  Converts a vector of single-precision floating-point values to unsigned 32-bit integer values, and rounds towards the nearest integer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vfixr32)*