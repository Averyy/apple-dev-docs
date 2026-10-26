# vDSP_fftm_zropD

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Computes a forward or inverse out-of-place, double-precision real FFT on multiple signals.

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
extern void vDSP_fftm_zropD(FFTSetupD __Setup, const DSPDoubleSplitComplex *__A, vDSP_Stride __IA, vDSP_Stride __IMA, const DSPDoubleSplitComplex *__C, vDSP_Stride __IC, vDSP_Stride __IMC, vDSP_Length __Log2N, vDSP_Length __M, FFTDirection __Direction);
```

#### Discussion

> 💡 **Tip**:  To learn how the vDSP library scales and arranges the FFT output, see [Understanding data packing for Fourier transforms](./understanding-data-packing-for-fourier-transforms.md).

## Parameters

- `__Setup`: The FFT setup structure for this transform. The setup’s structure `Log2N` must be greater than or equal to this function’s `Log2N`.
- `__A`: A pointer to the input data.
- `__IA`: The stride between the elements in `A`, set to 1 for best performance.
- `__IMA`: The increment, in complex elements, between input signals. This parameter also specifies the length of each input signal in split-complex format.
- `__C`: A pointer to the output data.
- `__IC`: The stride between the elements in `C`, set to 1 for best performance.
- `__IMC`: The increment, in elements, between output signals. This parameter also specifies the length of each output signal.
- `__Log2N`: The base 2 exponent of the number of elements to process. For example, to process 1024 elements, specify 10 for parameter `Log2N`.
- `__M`: The number of input signals.
- `__Direction`: A flag that specifies the transform direction. Pass [`kFFTDirection_Forward`](../kernel/api-1645049-anonymous/kfftdirection_forward.md) to transform from the time domain to the frequency domain. Pass [`kFFTDirection_Inverse`](../kernel/api-1645049-anonymous/kfftdirection_inverse.md) to transform from the frequency domain to the time domain.

## See Also

### Out-of-Place FFT Functions
- [vDSP_fftm_zrop](./vdsp_fftm_zrop.md)
  Computes a forward or inverse out-of-place, single-precision real FFT on multiple signals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_fftm_zropd)*