# vDSP_fft5_zopD

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Computes a double-precision out-of-place radix-5 complex FFT, either forward or inverse.

**Availability**:
- iOS 4.0+ - Deprecated in 9.0
- iPadOS 4.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.2+ - Deprecated in 10.11
- tvOS - Deprecated in 9.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

## Declaration

```c
extern void vDSP_fft5_zopD(FFTSetupD __Setup, const DSPDoubleSplitComplex *__A, vDSP_Stride __IA, const DSPDoubleSplitComplex *__C, vDSP_Stride __IC, vDSP_Length __Log2N, FFTDirection __Direction);
```

#### Discussion

The number of input and output values processed equals 5 times the power of 2 specified by parameter `Log2N`.

This is the same as [`vDSP_fft5_zop`](./vdsp_fft5_zop.md), except for the types of the `Setup` object and the `A` and `C` vectors.

See also functions  [`vDSP_create_fftsetupD`](./vdsp_create_fftsetupd.md), [`vDSP_destroy_fftsetupD`](./vdsp_destroy_fftsetupd.md), and [vDSP Programming Guide](https://developer.apple.com/library/archive/documentation/Performance/Conceptual/vDSP_Programming_Guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40005147).

## See Also

### Radix 3 and Radix 5 FFT Functions
- [vDSP_fft3_zop](./vdsp_fft3_zop.md)
  Computes a single-precision out-of-place radix-3 complex FFT, either forward or inverse.
- [vDSP_fft3_zopD](./vdsp_fft3_zopd.md)
  Computes a double-precision out-of-place radix-3 complex FFT, either forward or inverse.
- [vDSP_fft5_zop](./vdsp_fft5_zop.md)
  Computes a single-precision out-of-place radix-5 complex FFT, either forward or inverse.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_fft5_zopd)*