# vDSP_fft_zopt

**Framework**: Accelerate  
**Kind**: func

Computes a forward or inverse out-of-place, single-precision complex FFT using a temporary buffer.

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
extern void vDSP_fft_zopt(FFTSetup __Setup, const DSPSplitComplex * __A, vDSP_Stride __IA, const DSPSplitComplex * __C, vDSP_Stride __IC, const DSPSplitComplex * __Buffer, vDSP_Length __Log2N, FFTDirection __Direction);
```

#### Discussion

> 💡 **Tip**:  To learn how the vDSP library scales and arranges the FFT output, see [`Understanding data packing for Fourier transforms`](understanding-data-packing-for-fourier-transforms.md).

## Parameters

- `__Setup`: The FFT setup structure for this transform. The setup’s structure   must be greater than or equal to this function’s  .
- `__A`: A pointer to the input data.
- `__IA`: The stride between the elements in  , set to 1 for best performance.
- `__C`: A pointer to the output data.
- `__IC`: The stride between the elements in  , set to 1 for best performance.
- `__Buffer`: A temporary vector that the operation uses for storing interim results. The real and imaginary parts of the buffer must both contain the lesser of  Log2N elements or 16,384 bytes. For best performance, the buffer addresses must be 16-byte aligned or better.
- `__Log2N`: The base 2 exponent of the number of elements to process. For example, to process 1024 elements, specify 10 for parameter  .
- `__Direction`: A flag that specifies the transform direction. Pass   to transform from the time domain to the frequency domain. Pass   to transform from the frequency domain to the time domain.

## See Also

- [vDSP_fft_zoptD](vdsp_fft_zoptd.md)
  Computes a forward or inverse out-of-place, double-precision complex FFT using a temporary buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_fft_zopt)*