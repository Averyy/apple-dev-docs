# transform(fftSetup:log2n:source:destination:direction:)

**Framework**: Accelerate  
**Kind**: method

Performs a 1D fast Fourier transform.

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
static func transform(fftSetup: OpaquePointer, log2n: vDSP_Length, source: UnsafePointer<vDSP_SplitComplexDouble.SplitComplex>, destination: UnsafeMutablePointer<vDSP_SplitComplexDouble.SplitComplex>, direction: vDSP.FourierTransformDirection)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_splitcomplexdouble/transform(fftsetup:log2n:source:destination:direction:))*