# vDSP_vssq

**Framework**: Accelerate  
**Kind**: func

Computes the signed squared value of each element in the supplied single-precision vector.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
extern void vDSP_vssq(const float * __A, vDSP_Stride __IA, float * __C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

This performs the following operation:

![mathematical formula](https://docs-assets.developer.apple.com/published/973243688ac83b4c62bc2b02248b410e/media-2557726%402x.png)

## Parameters

- `__A`: Single-precision real input vector.
- `__IA`: Address stride for  .
- `__C`: Single-precision real output vector.
- `__IC`: Address stride for  .
- `__N`: The number of elements to process.

## See Also

- [vDSP_vsq](vdsp_vsq.md)
  Computes the squared value of each element in the supplied single-precision vector.
- [vDSP_vsqD](vdsp_vsqd.md)
  Computes the squared value of each element in the supplied double-precision vector.
- [vDSP_vssqD](vdsp_vssqd.md)
  Computes the signed squared value of each element in the supplied double-precision vector.
- [vDSP_zvmags](vdsp_zvmags.md)
  Computes the squared magnitude value of each element in the supplied complex single-precision vector.
- [vDSP_zvmagsD](vdsp_zvmagsd.md)
  Computes the squared magnitude value of each element in the supplied complex double-precision vector.
- [vDSP_zvmgsa](vdsp_zvmgsa.md)
  Complex vector magnitudes square and add; single precision.
- [vDSP_zvmgsaD](vdsp_zvmgsad.md)
  Complex vector magnitudes square and add; double precision.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vssq)*