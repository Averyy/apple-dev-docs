# transform2D(fftSetup:width:height:source:destination:direction:)

**Framework**: Accelerate  
**Kind**: method

Performs a 2D fast Fourier transform.

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
static func transform2D(fftSetup: OpaquePointer, width: Int, height: Int, source: UnsafePointer<vDSP_SplitComplexDouble.SplitComplex>, destination: UnsafeMutablePointer<vDSP_SplitComplexDouble.SplitComplex>, direction: vDSP.FourierTransformDirection)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_splitcomplexdouble/transform2d(fftsetup:width:height:source:destination:direction:))*