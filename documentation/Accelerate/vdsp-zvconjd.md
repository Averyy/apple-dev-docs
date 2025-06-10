# vDSP_zvconjD

**Framework**: Accelerate  
**Kind**: func

Calculates the complex conjugate of the values in a double-precision vector using the specified stride.

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
extern void vDSP_zvconjD(const DSPDoubleSplitComplex * __A, vDSP_Stride __IA, const DSPDoubleSplitComplex * __C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

This function is the same as [`vDSP_zvconj`](vdsp_zvconj.md), except for the types of vectors `A` and `C`.

## See Also

- [vDSP_zvconj](vdsp_zvconj.md)
  Calculates the complex conjugate of the values in a single-precision vector using the specified stride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_zvconjd)*