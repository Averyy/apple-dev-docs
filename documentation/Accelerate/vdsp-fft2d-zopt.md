# vDSP_fft2d_zopt

**Framework**: Accelerate  
**Kind**: func

Computes a 2D forward or inverse out-of-place, single-precision complex FFT using a temporary buffer.

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
extern void vDSP_fft2d_zopt(FFTSetup __Setup, const DSPSplitComplex * __A, vDSP_Stride __IA0, vDSP_Stride __IA1, const DSPSplitComplex * __C, vDSP_Stride __IC0, vDSP_Stride __IC1, const DSPSplitComplex * __Buffer, vDSP_Length __Log2N0, vDSP_Length __Log2N1, FFTDirection __Direction);
```

#### Discussion

> 💡 **Tip**:  To learn how the vDSP library scales and arranges the FFT output, see [`Understanding data packing for Fourier transforms`](understanding-data-packing-for-fourier-transforms.md).

## Parameters

- `__Setup`: The FFT setup structure for this transform. The setup’s structure   must be greater than or equal to this function’s   and  .
- `__A`: A pointer to the input data.
- `__IA0`: The stride between the elements in a row of  , set to 1 for best performance.
- `__IA1`: The increment, in elements, between consecutive elements in a column of   which is also the distance between adjacent rows of  . Unless   is a submatrix, pass   to have the function calculate the default column stride as the row stride (   multiplied by the column count.
- `__C`: A pointer to the output data.
- `__IC0`: The stride between the elements in a row of  , set to 1 for best performance.
- `__IC1`: The increment, in elements, between consecutive elements in a column of   which is also the distance between adjacent rows of  . Unless   is a submatrix, pass   to have the function calculate the default column stride as the row stride (   multiplied by the column count.
- `__Buffer`: A temporary vector that the operation uses for storing interim results. The real and imaginary parts of the buffer must both contain the lesser of  Log2N0  Log2N1 elements or 16,384 bytes. For best performance, the buffer addresses must be 16-byte aligned or better.
- `__Log2N0`: The base 2 exponent of the number of columns to process for each row.
- `__Log2N1`: The base 2 exponent of the number of rows to process. For example, to process 64 rows of 128 columns, specify   for   and   for  .
- `__Direction`: A flag that specifies the transform direction. Pass   to transform from the spatial domain to the frequency domain. Pass   to transform from the frequency domain to the spatial domain.

## See Also

- [vDSP_fft2d_zoptD](vdsp_fft2d_zoptd.md)
  Computes a 2D forward or inverse out-of-place, double-precision complex FFT using a temporary buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_fft2d_zopt)*