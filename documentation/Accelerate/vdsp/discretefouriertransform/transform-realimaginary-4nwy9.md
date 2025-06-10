# transform(real:imaginary:)

**Framework**: Accelerate  
**Kind**: method

Returns the result of a single-precision discrete Fourier transform.

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
func transform<U>(real: U, imaginary: U) -> (real: [Float], imaginary: [Float]) where U : AccelerateBuffer, U.Element == Float
```

#### Return Value

A tuple of two arrays that represents the real and imaginary parts of the output.

## Parameters

- `real`: An array that contains the real parts of the input.
- `imaginary`: An array that contains the imaginary parts of the input.

## See Also

- [func transform<U>(real: U, imaginary: U) -> (real: [Double], imaginary: [Double])](vdsp/discretefouriertransform/transform(real:imaginary:)-82jag.md)
  Returns the result of a double-precision discrete Fourier transform.
- [func transform<U, V>(inputReal: U, inputImaginary: U, outputReal: inout V, outputImaginary: inout V)](vdsp/discretefouriertransform/transform(inputreal:inputimaginary:outputreal:outputimaginary:)-sihh.md)
  Computes a single-precision discrete Fourier transform.
- [func transform<U, V>(inputReal: U, inputImaginary: U, outputReal: inout V, outputImaginary: inout V)](vdsp/discretefouriertransform/transform(inputreal:inputimaginary:outputreal:outputimaginary:)-7115x.md)
  Computes a double-precision discrete Fourier transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/discretefouriertransform/transform(real:imaginary:)-4nwy9)*