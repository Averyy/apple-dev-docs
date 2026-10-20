# vDSP.DFT

**Framework**: Accelerate  
**Kind**: class  
**Role**: Class

A single- and double-precision discrete Fourier transform.

**Availability**:
- iOS 13.0+ - Deprecated
- iPadOS 13.0+ - Deprecated
- Mac Catalyst 13.0+ - Deprecated
- macOS 10.15+ - Deprecated
- tvOS 13.0+ - Deprecated
- visionOS
- watchOS 6.0+ - Deprecated

> **Deprecated**: Use [`vDSP.DiscreteFourierTransform`](./discretefouriertransform.md) instead.

## Declaration

```swift
class DFT<T> where T : vDSP_FloatingPointDiscreteFourierTransformable
```

## Topics

### Initializers
- [init?(previous: vDSP.DFT<T>?, count: Int, direction: vDSP.FourierTransformDirection, transformType: vDSP.DFTTransformType, ofType: T.Type)](./dft/init%28previous,count,direction,transformtype,oftype%29.md)
  Initializes a new discrete Fourier transform instance.
### Instance Methods
- [func transform<U>(inputReal: U, inputImaginary: U) -> (real: [T], imaginary: [T])](./dft/transform%28inputreal,inputimaginary%29.md)
  Returns a discrete Fourier transform.
- [func transform<U, V>(inputReal: U, inputImaginary: U, outputReal: inout V, outputImaginary: inout V)](./dft/transform%28inputreal,inputimaginary,outputreal,outputimaginary%29.md)
  Computes an out-of-place discrete Fourier transform.

## See Also

### Objects that simplify discrete Fourier transforms
- [class DiscreteFourierTransform](./discretefouriertransform.md)
  An object that provides forward and inverse discrete Fourier transforms on single- or double-precision collections of interleaved or split-complex data.
- [vDSP.DFTTransformType](./dfttransformtype.md)
  Discrete Fourier transform types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/dft)*