# vDSP_fft2d_zropD

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Computes a 2D forward or inverse out-of-place, double-precision real FFT.

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
extern void vDSP_fft2d_zropD(FFTSetupD __Setup, const DSPDoubleSplitComplex *__A, vDSP_Stride __IA0, vDSP_Stride __IA1, const DSPDoubleSplitComplex *__C, vDSP_Stride __IC0, vDSP_Stride __IC1, vDSP_Length __Log2N0, vDSP_Length __Log2N1, FFTDirection __Direction);
```

## Discussion

> 💡 **Tip**:  To learn how the vDSP library scales and arranges the FFT output, see [Understanding data packing for Fourier transforms](./understanding-data-packing-for-fourier-transforms.md).

## Parameters

- `__Setup`: The FFT setup structure for this transform. The setup’s structure `Log2N` must be greater than or equal to this function’s `Log2N0` and `Log2N1`.
- `__A`: A pointer to the input data.
- `__IA0`: The stride between the elements in a row of `A`, set to 1 for best performance.
- `__IA1`: The increment, in elements, between consecutive elements in a column of `A,` which is also the distance between adjacent rows of `A`. Unless `A` is a submatrix, pass `0` to have the function calculate the default column stride as the row stride ( `__IA0)` multiplied by the column count.
- `__C`: A pointer to the output data.
- `__IC0`: The stride between the elements in a row of `C`, set to 1 for best performance.
- `__IC1`: The increment, in elements, between consecutive elements in a column of `C,` which is also the distance between adjacent rows of `C`. Unless `C` is a submatrix, pass `0` to have the function calculate the default column stride as the row stride ( `__IC0)` multiplied by the column count.
- `__Log2N0`: The base 2 exponent of the number of columns to process for each row.
- `__Log2N1`: The base 2 exponent of the number of rows to process. For example, to process 64 rows of 128 columns, specify `7` for `Log2N0` and `6` for `Log2N1`.
- `__Direction`: A flag that specifies the transform direction. Pass [`kFFTDirection_Forward`](../kernel/api-1645049-anonymous/kfftdirection_forward.md) to transform from the spatial domain to the frequency domain. Pass [`kFFTDirection_Inverse`](../kernel/api-1645049-anonymous/kfftdirection_inverse.md) to transform from the frequency domain to the spatial domain.

## See Also

### Out-of-Place FFT Functions
- [vDSP_fft2d_zrop](./vdsp_fft2d_zrop.md)
  Computes a 2D forward or inverse out-of-place, single-precision real FFT.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_fft2d_zropd)*