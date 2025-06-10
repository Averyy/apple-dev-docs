# makeFFTSetup(log2n:radix:)

**Framework**: Accelerate  
**Kind**: method

Returns a setup structure to perform a fast Fourier transform.

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
static func makeFFTSetup(log2n: vDSP_Length, radix: vDSP.Radix) -> OpaquePointer?
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_splitcomplexdouble/makefftsetup(log2n:radix:))*