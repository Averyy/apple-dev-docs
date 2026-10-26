# vDSP_fft2d_zip

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Computes a 2D forward or inverse in-place, single-precision complex FFT.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern void vDSP_fft2d_zip(FFTSetup __Setup, const DSPSplitComplex *__C, vDSP_Stride __IC0, vDSP_Stride __IC1, vDSP_Length __Log2N0, vDSP_Length __Log2N1, FFTDirection __Direction);
```

## Mentions

- [Understanding data packing for Fourier transforms](./understanding-data-packing-for-fourier-transforms.md)

#### Discussion

> 💡 **Tip**:  To learn how the vDSP library scales and arranges the FFT output, see [Understanding data packing for Fourier transforms](./understanding-data-packing-for-fourier-transforms.md).

## Parameters

- `__Setup`: The FFT setup structure for this transform. The setup’s structure `Log2N` must be greater than or equal to this function’s `Log2N0` and `Log2N1`.
- `__C`: A pointer to the input-output data.
- `__IC0`: The stride between the elements in a row of `C`, set to 1 for best performance.
- `__IC1`: The increment, in elements, between consecutive elements in a column of `A,` which is also the distance between adjacent rows of `A`. Unless `A` is a submatrix, pass `0` to have the function calculate the default column stride as the row stride ( `__IA0)` multiplied by the column count.
- `__Log2N0`: The base 2 exponent of the number of columns to process for each row.
- `__Log2N1`: The base 2 exponent of the number of rows to process. For example, to process 64 rows of 128 columns, specify `7` for `Log2N0` and `6` for `Log2N1`.
- `__Direction`: A flag that specifies the transform direction. Pass [`kFFTDirection_Forward`](../kernel/api-1645049-anonymous/kfftdirection_forward.md) to transform from the spatial domain to the frequency domain. Pass [`kFFTDirection_Inverse`](../kernel/api-1645049-anonymous/kfftdirection_inverse.md) to transform from the frequency domain to the spatial domain.

## See Also

### In-Place FFT Functions
- [vDSP_fft2d_zipD](./vdsp_fft2d_zipd.md)
  Computes a 2D forward or inverse in-place, double-precision complex FFT.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_fft2d_zip)*