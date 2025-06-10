# vDSP_imgfirD

**Framework**: Accelerate  
**Kind**: func

Filters a double-precision image by performing a 2D convolution with an arbitrarily sized kernel.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
extern void vDSP_imgfirD(const double * __A, vDSP_Length __NR, vDSP_Length __NC, const double * __F, double * __C, vDSP_Length __P, vDSP_Length __Q);
```

#### Discussion

This function is the same as [`vDSP_imgfir`](vdsp_imgfir.md), except for the types of vectors `A`, `F`, and `C`.

## See Also

- [vDSP_imgfir](vdsp_imgfir.md)
  Filters a single-precision image by performing a 2D convolution with an arbitrarily sized kernel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_imgfird)*