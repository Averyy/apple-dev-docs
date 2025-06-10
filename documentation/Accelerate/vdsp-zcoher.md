# vDSP_zcoher

**Framework**: Accelerate  
**Kind**: func

Computes the coherence function of two single-precision vectors.

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
extern void vDSP_zcoher(const float * __A, const float * __B, const DSPSplitComplex * __C, float * __D, vDSP_Length __N);
```

#### Discussion

This function computes the coherence function of two signals. The  inputs are the signals’ autospectra, real vectors `A` and `B`, and their cross-spectrum, complex vector `C`. Results are left in `D`.

(The autospectra and the cross-spectrum can be obtained from [`vDSP_zaspec`](vdsp_zaspec.md) and [`vDSP_zcspec`](vdsp_zcspec.md) respectively.)

![mathematical formula](https://docs-assets.developer.apple.com/published/7ce8a5479bc0579a4c4aeebc3ad1c452/media-2557787%402x.png)

## Parameters

- `__A`: Single-precision real input vector, with a stride of 1.
- `__B`: Single-precision real input vector, with a stride of 1.
- `__C`: Single-precision complex input vector, with a stride of 1.
- `__D`: Single-precision real output vector, with a stride of 1.
- `__N`: The number of elements to process.

## See Also

- [vDSP_zcoherD](vdsp_zcoherd.md)
  Computes the coherence function of two double-precision vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_zcoher)*