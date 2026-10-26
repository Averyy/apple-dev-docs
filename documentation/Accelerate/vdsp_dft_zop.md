# vDSP_DFT_zop

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

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
void vDSP_DFT_zop(const struct vDSP_DFT_SetupStruct *__Setup, const float *__Ir, const float *__Ii, vDSP_Stride __Is, float *__Or, float *__Oi, vDSP_Stride __Os, vDSP_DFT_Direction __Direction);
```

## See Also

### Functions for 1D Real FFT
- [In-Place Functions for 1D Real FFT](./in-place-functions-for-1d-real-fft.md)
  Perform fast Fourier transforms in place on 1D real data.
- [Out-of-Place Functions for 1D Real FFT](./out-of-place-functions-for-1d-real-fft.md)
  Perform fast Fourier transforms out of place on 1D real data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_dft_zop)*