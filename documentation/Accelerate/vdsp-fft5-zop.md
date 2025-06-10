# vDSP_fft5_zop

**Framework**: Accelerate  
**Kind**: func

Computes a single-precision out-of-place radix-5 complex FFT, either forward or inverse.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
extern void vDSP_fft5_zop(FFTSetup __Setup, const DSPSplitComplex * __A, vDSP_Stride __IA, const DSPSplitComplex * __C, vDSP_Stride __IC, vDSP_Length __Log2N, FFTDirection __Direction);
```

#### Discussion

The number of input and output values processed equals 5 times the power of 2 specified by parameter `Log2N`.

This performs the following operation:

![mathematical formula](https://docs-assets.developer.apple.com/published/eb29785edfeb7d08fb16365ec2755c59/media-2557819%402x.png)

where F is `Direction`, j is the square root of `-1`, and N is two raised to the power of `Log2N`.

See also functions [`vDSP_create_fftsetup`](https://developer.apple.com/documentation/kernel/1580009-vdsp_create_fftsetup), [`vDSP_destroy_fftsetup`](https://developer.apple.com/documentation/kernel/1579978-vdsp_destroy_fftsetup), and [`vDSP Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Performance/Conceptual/vDSP_Programming_Guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40005147).

## Parameters

- `__Setup`: A setup object returned from a previous call to  .   must be specified in the call to  .   is preserved for reuse.
- `__A`: Complex input vector.
- `__IA`: Stride between elements in  . The value of   should be 1 for best performance.
- `__C`: Complex output vector.
- `__IC`: Stride between elements in  . The value of   should be 1 for best performance.
- `__Log2N`: The base 2 exponent of the number of elements to process in a single input signal.   must be between 3 and 15, inclusive.
- `__Direction`: A forward/inverse directional flag, which must specify   (+1) or   (-1).

## See Also

- [vDSP_fft3_zop](vdsp_fft3_zop.md)
  Computes a single-precision out-of-place radix-3 complex FFT, either forward or inverse.
- [vDSP_fft3_zopD](vdsp_fft3_zopd.md)
  Computes a double-precision out-of-place radix-3 complex FFT, either forward or inverse.
- [vDSP_fft5_zopD](vdsp_fft5_zopd.md)
  Computes a double-precision out-of-place radix-5 complex FFT, either forward or inverse.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_fft5_zop)*