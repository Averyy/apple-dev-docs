# vDSP_fftm_zripD

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Computes a forward or inverse in-place, double-precision real FFT on multiple signals.

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
extern void vDSP_fftm_zripD(FFTSetupD __Setup, const DSPDoubleSplitComplex *__C, vDSP_Stride __IC, vDSP_Stride __IM, vDSP_Length __Log2N, vDSP_Length __M, FFTDirection __Direction);
```

#### Discussion

> 💡 **Tip**:  To learn how the vDSP library scales and arranges the FFT output, see [Understanding data packing for Fourier transforms](./understanding-data-packing-for-fourier-transforms.md).

## Parameters

- `__Setup`: The FFT setup structure for this transform. The setup’s structure `Log2N` must be greater than or equal to this function’s `Log2N`.
- `__C`: A pointer to the input-output data.
- `__IC`: The stride between the elements in `C`, set to 1 for best performance.
- `__IM`: The increment, in complex elements, between input signals. This parameter also specifies the length of each input signal in split-complex format.
- `__Log2N`: The base 2 exponent of the number of elements to process in a single input signal. For example, to process 512 elements, specify 9 for parameter `Log2N`.
- `__M`: The number of input signals.
- `__Direction`: A flag that specifies the transform direction. Pass [`kFFTDirection_Forward`](../kernel/api-1645049-anonymous/kfftdirection_forward.md) to transform from the time domain to the frequency domain. Pass [`kFFTDirection_Inverse`](../kernel/api-1645049-anonymous/kfftdirection_inverse.md) to transform from the frequency domain to the time domain.

## See Also

### In-Place FFT Functions
- [vDSP_fftm_zrip](./vdsp_fftm_zrip.md)
  Computes a forward or inverse in-place, single-precision real FFT on multiple signals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_fftm_zripd)*