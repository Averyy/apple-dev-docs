# vDSP.FFT

**Framework**: Accelerate  
**Kind**: class

A 1D single- and double-precision fast Fourier transform.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
class FFT<T> where T : vDSP_FourierTransformable
```

## Topics

### Initializers
- [init?(log2n: vDSP_Length, radix: vDSP.Radix, ofType: T.Type)](vdsp/fft/init(log2n:radix:oftype:).md)
  Initializes a new fast Fourier transform instance.
### Instance Methods
- [func forward(input: DSPSplitComplex, output: inout DSPSplitComplex)](vdsp/fft/forward(input:output:).md)
  Computes an out-of-place forward fast Fourier transform.
- [func inverse(input: DSPSplitComplex, output: inout DSPSplitComplex)](vdsp/fft/inverse(input:output:).md)
  Computes an out-of-place inverse fast Fourier transform.
- [func transform<T>(input: T, output: inout T, direction: vDSP.FourierTransformDirection)](vdsp/fft/transform(input:output:direction:).md)
  Computes an out-of-place fast Fourier transform.
### Variables
- [var FFT_FORWARD: Int](fft_forward.md)
  Forward FFT.
- [var FFT_INVERSE: Int](fft_inverse.md)
  Inverse FFT.
- [var FFT_RADIX2: Int](fft_radix2.md)
- [var FFT_RADIX3: Int](fft_radix3.md)
- [var FFT_RADIX5: Int](fft_radix5.md)
- [var kFFTDirection_Forward: Int](kfftdirection_forward.md)
- [var kFFTDirection_Inverse: Int](kfftdirection_inverse.md)
- [var kFFTRadix2: Int](kfftradix2.md)
- [var kFFTRadix3: Int](kfftradix3.md)
- [var kFFTRadix5: Int](kfftradix5.md)

## Relationships

### Inherited By
- [vDSP.FFT2D](vdsp/fft2d.md)

## See Also

- [class FFT2D](vdsp/fft2d.md)
  A 2D single- and double-precision fast Fourier transform.
- [vDSP.FourierTransformDirection](vdsp/fouriertransformdirection.md)
  Fast Fourier transform directions.
- [vDSP.Radix](vdsp/radix.md)
  Fast Fourier transform radices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/fft)*