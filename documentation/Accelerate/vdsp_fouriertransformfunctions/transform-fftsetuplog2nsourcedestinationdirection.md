# transform(fftSetup:log2n:source:destination:direction:)

**Framework**: Accelerate  
**Kind**: method  
**Required**: Yes

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
static func transform(fftSetup: OpaquePointer, log2n: vDSP_Length, source: UnsafePointer<Self.SplitComplex>, destination: UnsafeMutablePointer<Self.SplitComplex>, direction: vDSP.FourierTransformDirection)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_fouriertransformfunctions/transform(fftsetup:log2n:source:destination:direction:))*