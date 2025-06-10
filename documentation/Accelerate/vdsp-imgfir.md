# vDSP_imgfir

**Framework**: Accelerate  
**Kind**: func

Filters a single-precision image by performing a 2D convolution with an arbitrarily sized kernel.

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
extern void vDSP_imgfir(const float * __A, vDSP_Length __NR, vDSP_Length __NC, const float * __F, float * __C, vDSP_Length __P, vDSP_Length __Q);
```

#### Discussion

This function performs a two-dimensional convolution on the signal `A` using the kernel `B`, leaving results in `C`. The function pads the perimeter of the output image with a border of (-1)/2 rows of zeros on the top and bottom and (-1)/2 columns of zeros on the left and right:

![mathematical formula](https://docs-assets.developer.apple.com/published/1d53b205203ed6c56403564e9d9c6425/media-2557832%402x.png)

## Parameters

- `__A`: Single-precision real input matrix.
- `__NR`: Number of rows in  .
- `__NC`: Number of columns in  .
- `__F`: Single-precision real matrix containing the filter.
- `__C`: Single-precision real output matrix.
- `__P`: Number of rows in  ; the value of   must be odd.
- `__Q`: Number of columns in  ; the value of   must be odd.

## See Also

- [vDSP_imgfirD](vdsp_imgfird.md)
  Filters a double-precision image by performing a 2D convolution with an arbitrarily sized kernel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_imgfir)*