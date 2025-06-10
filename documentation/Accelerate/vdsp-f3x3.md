# vDSP_f3x3

**Framework**: Accelerate  
**Kind**: func

Filters a single-precision image by performing a 2D convolution with a 3 x 3 kernel.

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
extern void vDSP_f3x3(const float * __A, vDSP_Length __NR, vDSP_Length __NC, const float * __F, float * __C);
```

#### Discussion

This function filters an image by performing a two-dimensional convolution with a 3x3 kernel (`F`) on the input matrix `A` and storing the resulting image in the output matrix `C`.

This function zero-pads the perimeter of the output image with a border of width 1:

![mathematical formula](https://docs-assets.developer.apple.com/published/e6b67b9c9d2ef78b6b080c9cc5321905/media-2557830%402x.png)

## Parameters

- `__A`: Single-precision real input matrix.
- `__NR`: The number of rows in  . The value of   must be greater than or equal to 3.
- `__NC`: The number of columns in  . The value of   must be even and greater than or equal to 4.
- `__F`: Single-precision real 3x3 kernel.
- `__C`: Single-precision real result matrix.

## See Also

- [vDSP_f3x3D](vdsp_f3x3d.md)
  Filters a double-precision image by performing a 2D convolution with a 3 x 3 kernel.
- [vDSP_f5x5](vdsp_f5x5.md)
  Filters a single-precision image by performing a 2D convolution with a 5 x 5 kernel.
- [vDSP_f5x5D](vdsp_f5x5d.md)
  Filters a double-precision image by performing a 2D convolution with a 5 x 5 kernel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_f3x3)*