# transform(input:output:direction:)

**Framework**: Accelerate  
**Kind**: method

Computes an out-of-place 2D fast Fourier transform.

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
override func transform<T>(input: T, output: inout T, direction: vDSP.FourierTransformDirection) where T : vDSP_FourierTransformable
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/fft2d/transform(input:output:direction:))*