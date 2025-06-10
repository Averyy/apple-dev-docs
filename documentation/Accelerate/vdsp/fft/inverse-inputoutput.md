# inverse(input:output:)

**Framework**: Accelerate  
**Kind**: method

Computes an out-of-place inverse fast Fourier transform.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
func inverse(input: DSPSplitComplex, output: inout DSPSplitComplex)
```

## See Also

- [func forward(input: DSPSplitComplex, output: inout DSPSplitComplex)](vdsp/fft/forward(input:output:).md)
  Computes an out-of-place forward fast Fourier transform.
- [func transform<T>(input: T, output: inout T, direction: vDSP.FourierTransformDirection)](vdsp/fft/transform(input:output:direction:).md)
  Computes an out-of-place fast Fourier transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/fft/inverse(input:output:))*