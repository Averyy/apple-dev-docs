# vDSP.DFT

**Framework**: Accelerate  
**Kind**: class

A single- and double-precision discrete Fourier transform.

**Availability**:
- iOS 13.0+ - Deprecated
- iPadOS 13.0+ - Deprecated
- Mac Catalyst ?+
- macOS 10.15+ - Deprecated
- tvOS 13.0+ - Deprecated
- visionOS ?+
- watchOS 6.0+ - Deprecated
- Unknown ?+ - Deprecated

## Declaration

```swift
class DFT<T> where T : vDSP_FloatingPointDiscreteFourierTransformable
```

## Topics

### Initializers
- [init?(previous: vDSP.DFT<T>?, count: Int, direction: vDSP.FourierTransformDirection, transformType: vDSP.DFTTransformType, ofType: T.Type)](vdsp/dft/init(previous:count:direction:transformtype:oftype:).md)
  Initializes a new discrete Fourier transform instance.
### Instance Methods
- [func transform<U>(inputReal: U, inputImaginary: U) -> (real: [T], imaginary: [T])](vdsp/dft/transform(inputreal:inputimaginary:).md)
  Returns a discrete Fourier transform.
- [func transform<U, V>(inputReal: U, inputImaginary: U, outputReal: inout V, outputImaginary: inout V)](vdsp/dft/transform(inputreal:inputimaginary:outputreal:outputimaginary:).md)
  Computes an out-of-place discrete Fourier transform.

## See Also

- [class DiscreteFourierTransform](vdsp/discretefouriertransform.md)
  An object that provides forward and inverse discrete Fourier transforms on single- or double-precision collections of interleaved or split-complex data.
- [vDSP.DFTTransformType](vdsp/dfttransformtype.md)
  Discrete Fourier transform types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/dft)*