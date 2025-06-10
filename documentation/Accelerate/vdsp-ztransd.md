# vDSP_ztransD

**Framework**: Accelerate  
**Kind**: func

Divides a complex double-precision vector by a real double-precision vector.

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
extern void vDSP_ztransD(const double * __A, const DSPDoubleSplitComplex * __B, const DSPDoubleSplitComplex * __C, vDSP_Length __N);
```

#### Discussion

This function is the same as [`vDSP_ztrans`](vdsp_ztrans.md), except for the types of vectors `A`, `B`, and `C`.

## Parameters

- `__A`: Double-precision real input vector.
- `__B`: Double-precision complex input vector.
- `__C`: Double-precision complex output vector.
- `__N`: The number of elements to process.

## See Also

- [vDSP_ztrans](vdsp_ztrans.md)
  Divides a complex single-precision vector by a real single-precision vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_ztransd)*