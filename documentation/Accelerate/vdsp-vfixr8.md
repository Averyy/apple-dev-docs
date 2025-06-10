# vDSP_vfixr8

**Framework**: Accelerate  
**Kind**: func

Converts a vector of single-precision floating-point values to signed 8-bit integer values, and rounds towards the nearest integer.

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
extern void vDSP_vfixr8(const float * __A, vDSP_Stride __IA, char * __C, vDSP_Stride __IC, vDSP_Length __N);
```

## Parameters

- `__A`: The input vector.
- `__IA`: The distance between the elements in the input vector.
- `__C`: The output vector.
- `__IC`: The distance between the elements in the output vector.
- `__N`: The number of elements that the function processes.

## See Also

- [vDSP_vfix8](vdsp_vfix8.md)
  Converts a vector of single-precision floating-point values to signed 8-bit integer values, and rounds towards zero.
- [vDSP_vfixu8](vdsp_vfixu8.md)
  Converts a vector of single-precision floating-point values to unsigned 8-bit integer values, and rounds towards zero.
- [vDSP_vfixru8](vdsp_vfixru8.md)
  Converts a vector of single-precision floating-point values to unsigned 8-bit integer values, and rounds towards the nearest integer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vfixr8)*