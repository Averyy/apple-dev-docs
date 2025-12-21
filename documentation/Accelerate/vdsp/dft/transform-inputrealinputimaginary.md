# transform(inputReal:inputImaginary:)

**Framework**: Accelerate  
**Kind**: method

Returns a discrete Fourier transform.

**Availability**:
- iOS 13.0+ - Deprecated
- iPadOS 13.0+ - Deprecated
- Mac Catalyst ?+
- macOS 10.15+ - Deprecated
- tvOS 13.0+ - Deprecated
- visionOS ?+
- watchOS 6.0+ - Deprecated

## Declaration

```swift
func transform<U>(inputReal: U, inputImaginary: U) -> (real: [T], imaginary: [T]) where T == U.Element, U : AccelerateBuffer
```

## See Also

- [func transform<U, V>(inputReal: U, inputImaginary: U, outputReal: inout V, outputImaginary: inout V)](vdsp/dft/transform(inputreal:inputimaginary:outputreal:outputimaginary:).md)
  Computes an out-of-place discrete Fourier transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/dft/transform(inputreal:inputimaginary:))*