# vDSP_fft3_zop

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Computes a single-precision out-of-place radix-3 complex FFT, either forward or inverse.

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
extern void vDSP_fft3_zop(FFTSetup __Setup, const DSPSplitComplex *__A, vDSP_Stride __IA, const DSPSplitComplex *__C, vDSP_Stride __IC, vDSP_Length __Log2N, FFTDirection __Direction);
```

#### Discussion

The number of input and output values processed equals 3 times the power of 2 specified by parameter `Log2N`.

This performs the following operation:

![mathematical formula](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-2557819@2x.png)

where F is `Direction`, C is `A`, j is the square root of `-1`, and N is two raised to the power of `Log2N`.

See also functions [`vDSP_create_fftsetup`](../kernel/api-1580009-vdsp_create_fftsetup.md), [`vDSP_destroy_fftsetup`](../kernel/api-1579978-vdsp_destroy_fftsetup.md), and [vDSP Programming Guide](https://developer.apple.com/library/archive/documentation/Performance/Conceptual/vDSP_Programming_Guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40005147).

## Parameters

- `__Setup`: A setup object as returned by a call to [`vDSP_create_fftsetup`](../kernel/api-1580009-vdsp_create_fftsetup.md). [`kFFTRadix3`](../kernel/api-1645051-anonymous/kfftradix3.md) must be specified in the call to `vDSP_create_fftsetup`. `Setup` is preserved for reuse.
- `__A`: Complex input vector.

  > **Note**:  The input data may be modified.
- `__IA`: Stride between elements in `A`. The value of `IA` should be 1 for best performance.
- `__C`: Complex output vector.
- `__IC`: Stride between elements in `C`. The value of `IC` should be 1 for best performance.
- `__Log2N`: The base 2 exponent of the number of elements to process in a single input signal. `Log2N` must be between 3 and 15, inclusive.
- `__Direction`: A forward/inverse directional flag, which must specify [`kFFTDirection_Forward`](../kernel/api-1645049-anonymous/kfftdirection_forward.md) (+1) or [`kFFTDirection_Inverse`](../kernel/api-1645049-anonymous/kfftdirection_inverse.md) (-1)for an inverse transform.

## See Also

### Radix 3 and Radix 5 FFT Functions
- [vDSP_fft3_zopD](./vdsp_fft3_zopd.md)
  Computes a double-precision out-of-place radix-3 complex FFT, either forward or inverse.
- [vDSP_fft5_zop](./vdsp_fft5_zop.md)
  Computes a single-precision out-of-place radix-5 complex FFT, either forward or inverse.
- [vDSP_fft5_zopD](./vdsp_fft5_zopd.md)
  Computes a double-precision out-of-place radix-5 complex FFT, either forward or inverse.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_fft3_zop)*