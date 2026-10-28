# vDSP_imgfir

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Filters a single-precision image by performing a 2D convolution with an arbitrarily sized kernel.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern void vDSP_imgfir(const float *__A, vDSP_Length __NR, vDSP_Length __NC, const float *__F, float *__C, vDSP_Length __P, vDSP_Length __Q);
```

## Discussion

This function performs a two-dimensional convolution on the signal `A` using the kernel `B`, leaving results in `C`. The function pads the perimeter of the output image with a border of (*P*-1)/2 rows of zeros on the top and bottom and (*Q*-1)/2 columns of zeros on the left and right:

![mathematical formula](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-2557832@2x.png)

## Parameters

- `__A`: Single-precision real input matrix.
- `__NR`: Number of rows in `A`.
- `__NC`: Number of columns in `A`.
- `__F`: Single-precision real matrix containing the filter.
- `__C`: Single-precision real output matrix.
- `__P`: Number of rows in `B`; the value of `P` must be odd.
- `__Q`: Number of columns in `B`; the value of `Q` must be odd.

## See Also

### Arbitrary-Size Kernel
- [vDSP_imgfirD](./vdsp_imgfird.md)
  Filters a double-precision image by performing a 2D convolution with an arbitrarily sized kernel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_imgfir)*