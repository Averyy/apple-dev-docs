# transform(inputReal:inputImaginary:outputReal:outputImaginary:)

**Framework**: Accelerate  
**Kind**: method

Computes a double-precision discrete Fourier transform.

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
func transform<U, V>(inputReal: U, inputImaginary: U, outputReal: inout V, outputImaginary: inout V) where U : AccelerateBuffer, V : AccelerateMutableBuffer, U.Element == Double, V.Element == Double
```

## Parameters

- `inputReal`: An array that contains the real parts of the input.
- `inputImaginary`: An array that contains the imaginary parts of the input.
- `outputReal`: An array that contains the real parts of the output.
- `outputImaginary`: An array that contains the imaginary parts of the output.

## See Also

- [func transform<U>(real: U, imaginary: U) -> (real: [Float], imaginary: [Float])](vdsp/discretefouriertransform/transform(real:imaginary:)-4nwy9.md)
  Returns the result of a single-precision discrete Fourier transform.
- [func transform<U>(real: U, imaginary: U) -> (real: [Double], imaginary: [Double])](vdsp/discretefouriertransform/transform(real:imaginary:)-82jag.md)
  Returns the result of a double-precision discrete Fourier transform.
- [func transform<U, V>(inputReal: U, inputImaginary: U, outputReal: inout V, outputImaginary: inout V)](vdsp/discretefouriertransform/transform(inputreal:inputimaginary:outputreal:outputimaginary:)-sihh.md)
  Computes a single-precision discrete Fourier transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/discretefouriertransform/transform(inputreal:inputimaginary:outputreal:outputimaginary:)-7115x)*