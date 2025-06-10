# vDSP_vfltu8D

**Framework**: Accelerate  
**Kind**: func

Converts an array of unsigned 8-bit integers to double-precision floating-point values.

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
extern void vDSP_vfltu8D(const unsigned char * __A, vDSP_Stride __IA, double * __C, vDSP_Stride __IC, vDSP_Length __N);
```

## Parameters

- `__A`: The input vector.
- `__IA`: The distance between the elements in the input vector.
- `__C`: The output vector.
- `__IC`: The distance between the elements in the output vector.
- `__N`: The number of elements that the function processes.

## See Also

- [vDSP_vflt8D](vdsp_vflt8d.md)
  Converts a vector of signed 8-bit integers to double-precision floating-point values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vfltu8d)*