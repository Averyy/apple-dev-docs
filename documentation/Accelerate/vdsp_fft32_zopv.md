# vDSP_FFT32_zopv

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Performs a 32-element FFT on split-complex data.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
void vDSP_FFT32_zopv(float *__Or, float *__Oi, const float *__Ir, const float *__Ii, FFTDirection __Direction);
```

## Discussion

> 💡 **Tip**:  To learn how the vDSP library scales and arranges the FFT output, see [Understanding data packing for Fourier transforms](./understanding-data-packing-for-fourier-transforms.md).

## Parameters

- `__Or`: Output vector for real parts.
- `__Oi`: Output vector for imaginary parts.
- `__Ir`: Input vector for real parts.
- `__Ii`: Input vector for imaginary parts.
- `__Direction`: A flag that specifies the transform direction. Pass [`kFFTDirection_Forward`](../kernel/api-1645049-anonymous/kfftdirection_forward.md) to transform from the time domain to the frequency domain. Pass [`kFFTDirection_Inverse`](../kernel/api-1645049-anonymous/kfftdirection_inverse.md) to transform from the frequency domain to the time domain.

## See Also

### Fixed-Length FFT Functions
- [vDSP_FFT16_copv](./vdsp_fft16_copv.md)
  Performs a 16-element FFT on interleaved-complex data.
- [vDSP_FFT32_copv](./vdsp_fft32_copv.md)
  Performs a 32-element FFT on interleaved-complex data.
- [vDSP_FFT16_zopv](./vdsp_fft16_zopv.md)
  Performs a 16-element FFT on split-complex data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_fft32_zopv)*