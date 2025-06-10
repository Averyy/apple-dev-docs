# vDSP_FFT16_copv

**Framework**: Accelerate  
**Kind**: func

Performs a 16-element FFT on interleaved-complex data.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
void vDSP_FFT16_copv(float * __Output, const float * __Input, FFTDirection __Direction);
```

#### Discussion

> 💡 **Tip**:  To learn how the vDSP library scales and arranges the FFT output, see [`Understanding data packing for Fourier transforms`](understanding-data-packing-for-fourier-transforms.md).

## Parameters

- `__Output`: A vector-block-aligned output array.
- `__Input`: A vector-block-aligned input array.
- `__Direction`: A flag that specifies the transform direction. Pass   to transform from the time domain to the frequency domain. Pass   to transform from the frequency domain to the time domain.

## See Also

- [vDSP_FFT32_copv](vdsp_fft32_copv.md)
  Performs a 32-element FFT on interleaved-complex data.
- [vDSP_FFT16_zopv](vdsp_fft16_zopv.md)
  Performs a 16-element FFT on split-complex data.
- [vDSP_FFT32_zopv](vdsp_fft32_zopv.md)
  Performs a 32-element FFT on split-complex data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_fft16_copv)*