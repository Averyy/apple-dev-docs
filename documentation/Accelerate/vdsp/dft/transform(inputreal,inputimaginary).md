# transform(inputReal:inputImaginary:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Instance Method

Returns a discrete Fourier transform.

**Availability**:
- iOS 13.0+ - Deprecated
- iPadOS 13.0+ - Deprecated
- Mac Catalyst 13.0+ - Deprecated
- macOS 10.15+ - Deprecated
- tvOS 13.0+ - Deprecated
- visionOS
- watchOS 6.0+ - Deprecated

> **Deprecated**: Use `vDSP.DiscreteFourierTransform`.

## Declaration

```swift
func transform<U>(inputReal: U, inputImaginary: U) -> (real: [T], imaginary: [T]) where T == U.Element, U : AccelerateBuffer
```

## See Also

### Instance Methods
- [func transform<U, V>(inputReal: U, inputImaginary: U, outputReal: inout V, outputImaginary: inout V)](./transform%28inputreal,inputimaginary,outputreal,outputimaginary%29.md)
  Computes an out-of-place discrete Fourier transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/dft/transform(inputreal:inputimaginary:))*