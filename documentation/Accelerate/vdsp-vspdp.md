# vDSP_vspdp

**Framework**: Accelerate  
**Kind**: func

Converts a single-precision vector to a double-precision vector.

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
extern void vDSP_vspdp(const float * __A, vDSP_Stride __IA, double * __C, vDSP_Stride __IC, vDSP_Length __N);
```

## Parameters

- `__A`: The input vector.
- `__IA`: The distance between the elements in the input vector.
- `__C`: The output vector.
- `__IC`: The distance between the elements in the output vector.
- `__N`: The number of elements that the function processes.

## See Also

- [vDSP_vdpsp](vdsp_vdpsp.md)
  Converts a double-precision vector to a single-precision vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vspdp)*