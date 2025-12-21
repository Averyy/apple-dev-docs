# transform(inputReal:inputImaginary:outputReal:outputImaginary:)

**Framework**: Accelerate  
**Kind**: method

Computes an out-of-place discrete Fourier transform.

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
func transform<U, V>(inputReal: U, inputImaginary: U, outputReal: inout V, outputImaginary: inout V) where T == U.Element, U : AccelerateBuffer, V : AccelerateMutableBuffer, U.Element == V.Element
```

## See Also

- [func transform<U>(inputReal: U, inputImaginary: U) -> (real: [T], imaginary: [T])](vdsp/dft/transform(inputreal:inputimaginary:).md)
  Returns a discrete Fourier transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/dft/transform(inputreal:inputimaginary:outputreal:outputimaginary:))*