# transform(input:output:direction:)

**Framework**: Accelerate  
**Kind**: method

Computes an out-of-place fast Fourier transform.

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
func transform<T>(input: T, output: inout T, direction: vDSP.FourierTransformDirection) where T : vDSP_FourierTransformable
```

## See Also

- [func forward(input: DSPSplitComplex, output: inout DSPSplitComplex)](vdsp/fft/forward(input:output:).md)
  Computes an out-of-place forward fast Fourier transform.
- [func inverse(input: DSPSplitComplex, output: inout DSPSplitComplex)](vdsp/fft/inverse(input:output:).md)
  Computes an out-of-place inverse fast Fourier transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/fft/transform(input:output:direction:))*