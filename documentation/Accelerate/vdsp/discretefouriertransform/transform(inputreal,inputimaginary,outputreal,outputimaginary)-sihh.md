# transform(inputReal:inputImaginary:outputReal:outputImaginary:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Instance Method

Computes a single-precision discrete Fourier transform.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS
- watchOS 8.0+

## Declaration

```swift
func transform<U, V>(inputReal: U, inputImaginary: U, outputReal: inout V, outputImaginary: inout V) where U : AccelerateBuffer, V : AccelerateMutableBuffer, U.Element == Float, V.Element == Float
```

Available when `T` is `Float`.

## Parameters

- `inputReal`: An array that contains the real parts of the input.
- `inputImaginary`: An array that contains the imaginary parts of the input.
- `outputReal`: An array that contains the real parts of the output.
- `outputImaginary`: An array that contains the imaginary parts of the output.

## See Also

### Performing Split-Complex Discrete Fourier Transforms
- [func transform<U>(real: U, imaginary: U) -> (real: [Float], imaginary: [Float])](./transform%28real,imaginary%29-4nwy9.md)
  Returns the result of a single-precision discrete Fourier transform.
- [func transform<U>(real: U, imaginary: U) -> (real: [Double], imaginary: [Double])](./transform%28real,imaginary%29-82jag.md)
  Returns the result of a double-precision discrete Fourier transform.
- [func transform<U, V>(inputReal: U, inputImaginary: U, outputReal: inout V, outputImaginary: inout V)](./transform%28inputreal,inputimaginary,outputreal,outputimaginary%29-7115x.md)
  Computes a double-precision discrete Fourier transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/discretefouriertransform/transform(inputreal:inputimaginary:outputreal:outputimaginary:)-sihh)*