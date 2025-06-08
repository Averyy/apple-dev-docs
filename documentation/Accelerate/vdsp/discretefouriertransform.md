# vDSP.DiscreteFourierTransform

**Framework**: Accelerate  
**Kind**: class

An object that provides forward and inverse discrete Fourier transforms on single- or double-precision collections of interleaved or split-complex data.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
class DiscreteFourierTransform<T> where T : vDSP_DiscreteFourierTransformable
```

#### Overview

Use a [`vDSP.DiscreteFourierTransform`](vdsp/discretefouriertransform.md) to perform discrete Fourier transforms (DFTs) on split-complex or interleaved data. To learn more about working with split-complex and interleaved data, see [`Performing Fourier transforms on interleaved-complex data`](performing-fourier-transforms-on-interleaved-complex-data.md).

To create a [`vDSP.DiscreteFourierTransform`](vdsp/discretefouriertransform.md) instance to work with interleaved data, pass either [`DSPComplex`](dspcomplex.md) or [`DSPDoubleComplex`](dspdoublecomplex.md) to [`init(previous:count:direction:transformType:ofType:)`](vdsp/discretefouriertransform/init(previous:count:direction:transformtype:oftype:).md). The following code shows how to perform a forward complex-to-complex DFT on the interleaved single-precision values in the `interleavedInput` array:

```swift
// The `interleavedInput` array contains `complexValuesCount` `DSPComplex` elements.
let interleavedInput: [DSPComplex] = [ ... ]

let interleavedDFT = try? vDSP.DiscreteFourierTransform(previous: nil,
                                                        count: complexValuesCount,
                                                        direction: .forward,
                                                        transformType: .complexComplex,
                                                        ofType: DSPComplex.self)

// On return, the `interleavedOutput` array contains an array of `DSPComplex`
// structures.
let interleavedOutput = interleavedDFT?.transform(input: interleavedInput)
```

To create a [`vDSP.DiscreteFourierTransform`](vdsp/discretefouriertransform.md) instance to work with split-complex data, pass either [`Float`](https://developer.apple.com/documentation/Swift/Float) or [`Double`](https://developer.apple.com/documentation/Swift/Double) to [`init(previous:count:direction:transformType:ofType:)`](vdsp/discretefouriertransform/init(previous:count:direction:transformtype:oftype:).md). Split-complex data stores the real and imaginary parts of each complex value in separate arrays. The following code shows how to perform forward complex-to-complex DFT on the split-complex single-precision values in the `splitComplexRealInput` and `splitComplexImaginaryInput` arrays:

```swift
var splitComplexRealInput: [Float] = [ ... ]
var splitComplexImaginaryInput: [Float] = [ ... ]

let splitComplexDFT = try? vDSP.DiscreteFourierTransform(previous: nil,
                                                         count: complexValuesCount,
                                                         direction: .forward,
                                                         transformType: .complexComplex,
                                                         ofType: Float.self)

// The `splitComplexOutput` tuple contains two arrays that represent the
// real and imaginary parts of the output.
let splitComplexOutput = splitComplexDFT?.transform(real: splitComplexRealInput,
                                                    imaginary: splitComplexImaginaryInput)
```

If the underlying data in both the `interleavedInput` array and the split-complex input arrays is the same, for each `i` in `0 ..< complexValuesCount`, the following is true`:`

```c
interleavedOutput[i].real ≈ splitComplexOutput.real[i]
interleavedOutput[i].imag ≈ splitComplexOutput.imaginary[i]
```

``

## Topics

### Creating a Discrete Fourier Transform Instance
- [init(previous: vDSP.DiscreteFourierTransform<Float>?, count: Int, direction: vDSP.FourierTransformDirection, transformType: vDSP.DFTTransformType, ofType: T.Type) throws](vdsp/discretefouriertransform/init(previous:count:direction:transformtype:oftype:).md)
  Returns a new discrete Fourier transform instance.
### Performing Split-Complex Discrete Fourier Transforms
- [func transform<U>(real: U, imaginary: U) -> (real: [Float], imaginary: [Float])](vdsp/discretefouriertransform/transform(real:imaginary:)-4nwy9.md)
  Returns the result of a single-precision discrete Fourier transform.
- [func transform<U>(real: U, imaginary: U) -> (real: [Double], imaginary: [Double])](vdsp/discretefouriertransform/transform(real:imaginary:)-82jag.md)
  Returns the result of a double-precision discrete Fourier transform.
- [func transform<U, V>(inputReal: U, inputImaginary: U, outputReal: inout V, outputImaginary: inout V)](vdsp/discretefouriertransform/transform(inputreal:inputimaginary:outputreal:outputimaginary:)-sihh.md)
  Computes a single-precision discrete Fourier transform.
- [func transform<U, V>(inputReal: U, inputImaginary: U, outputReal: inout V, outputImaginary: inout V)](vdsp/discretefouriertransform/transform(inputreal:inputimaginary:outputreal:outputimaginary:)-7115x.md)
  Computes a double-precision discrete Fourier transform.
### Performing Interleaved Discrete Fourier Transforms
- [func transform<U>(input: U) -> [DSPComplex]](vdsp/discretefouriertransform/transform(input:)-92b3l.md)
  Returns the result of a single-precision discrete Fourier transform.
- [func transform<U>(input: U) -> [DSPDoubleComplex]](vdsp/discretefouriertransform/transform(input:)-5si4h.md)
  Returns the result of a double-precision discrete Fourier transform.
- [func transform<U, V>(input: U, output: inout V)](vdsp/discretefouriertransform/transform(input:output:)-1k3hd.md)
  Computes a single-precision discrete Fourier transform.
- [func transform<U, V>(input: U, output: inout V)](vdsp/discretefouriertransform/transform(input:output:)-1tsod.md)
  Computes a double-precision discrete Fourier transform.

## See Also

- [vDSP.DFTTransformType](vdsp/dfttransformtype.md)
  Discrete Fourier transform types.
- [class DFT](vdsp/dft.md)
  A single- and double-precision discrete Fourier transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/discretefouriertransform)*