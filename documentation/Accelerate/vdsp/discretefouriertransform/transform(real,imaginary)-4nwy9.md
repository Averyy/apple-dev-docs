# transform(real:imaginary:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Instance Method

Returns the result of a single-precision discrete Fourier transform.

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
func transform<U>(real: U, imaginary: U) -> (real: [Float], imaginary: [Float]) where U : AccelerateBuffer, U.Element == Float
```

Available when `T` is `Float`.

#### Return Value

A tuple of two arrays that represents the real and imaginary parts of the output.

## Parameters

- `real`: An array that contains the real parts of the input.
- `imaginary`: An array that contains the imaginary parts of the input.

## See Also

### Performing Split-Complex Discrete Fourier Transforms
- [func transform<U>(real: U, imaginary: U) -> (real: [Double], imaginary: [Double])](./transform%28real,imaginary%29-82jag.md)
  Returns the result of a double-precision discrete Fourier transform.
- [func transform<U, V>(inputReal: U, inputImaginary: U, outputReal: inout V, outputImaginary: inout V)](./transform%28inputreal,inputimaginary,outputreal,outputimaginary%29-sihh.md)
  Computes a single-precision discrete Fourier transform.
- [func transform<U, V>(inputReal: U, inputImaginary: U, outputReal: inout V, outputImaginary: inout V)](./transform%28inputreal,inputimaginary,outputreal,outputimaginary%29-7115x.md)
  Computes a double-precision discrete Fourier transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/discretefouriertransform/transform(real:imaginary:)-4nwy9)*