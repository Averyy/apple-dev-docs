# vDSP_zcspecD

**Framework**: Accelerate  
**Kind**: func

Computes the cross-spectrum of two complex double-precision vectors.

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
extern void vDSP_zcspecD(const DSPDoubleSplitComplex * __A, const DSPDoubleSplitComplex * __B, const DSPDoubleSplitComplex * __C, vDSP_Length __N);
```

#### Discussion

This function is the same as [`vDSP_zcspec`](vdsp_zcspec.md), except for the types of vectors `A`, `B`, and `C`.

## See Also

- [vDSP_zcspec](vdsp_zcspec.md)
  Computes the cross-spectrum of two complex single-precision vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_zcspecd)*