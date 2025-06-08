# vDSP.FFT2D

**Framework**: Accelerate  
**Kind**: class

A 2D single- and double-precision fast Fourier transform.

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
class FFT2D<T> where T : vDSP_FourierTransformable
```

## Topics

### Initializers
- [init?(width: Int, height: Int, ofType: T.Type)](vdsp/fft2d/init(width:height:oftype:).md)
  Initializes a new fast Fourier transform instance for 2D FFT.
### Instance Methods
- [func transform<T>(input: T, output: inout T, direction: vDSP.FourierTransformDirection)](vdsp/fft2d/transform(input:output:direction:).md)
  Computes an out-of-place 2D fast Fourier transform.

## Relationships

### Inherits From
- [vDSP.FFT](vdsp/fft.md)

## See Also

- [class FFT](vdsp/fft.md)
  A 1D single- and double-precision fast Fourier transform.
- [vDSP.FourierTransformDirection](vdsp/fouriertransformdirection.md)
  Fast Fourier transform directions.
- [vDSP.Radix](vdsp/radix.md)
  Fast Fourier transform radices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/fft2d)*