# vDSP_f5x5

**Framework**: Accelerate  
**Kind**: func

Filters a single-precision image by performing a 2D convolution with a 5 x 5 kernel.

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
extern void vDSP_f5x5(const float * __A, vDSP_Length __NR, vDSP_Length __NC, const float * __F, float * __C);
```

#### Discussion

This function filters an image by performing a two-dimensional convolution with a 5x5 kernel (`F`) on the input matrix A and storing the resulting image in the output matrix `C`.

This function zero-pads the perimeter of the output image with a border of width 1:

![mathematical formula](https://docs-assets.developer.apple.com/published/8399bdbfdb50bddc8eab89e6799eaf59/media-2557831%402x.png)

## Parameters

- `__A`: Single-precision real input matrix.
- `__NR`: The number of rows in  . The value of   must be greater than or equal to 5.
- `__NC`: The number of columns in  . The value of   must be even and greater than or equal to 6.
- `__F`: Single-precision real 5x5 kernel.
- `__C`: Single-precision real result matrix.

## See Also

- [vDSP_f3x3](vdsp_f3x3.md)
  Filters a single-precision image by performing a 2D convolution with a 3 x 3 kernel.
- [vDSP_f3x3D](vdsp_f3x3d.md)
  Filters a double-precision image by performing a 2D convolution with a 3 x 3 kernel.
- [vDSP_f5x5D](vdsp_f5x5d.md)
  Filters a double-precision image by performing a 2D convolution with a 5 x 5 kernel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_f5x5)*