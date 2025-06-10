# applySingle(source:destination:delays:setup:sectionCount:count:)

**Framework**: Accelerate  
**Kind**: method

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
static func applySingle<U, V>(source: U, destination: inout V, delays: UnsafeMutablePointer<vDSP.VectorizableFloat.Scalar>, setup: vDSP_biquad_Setup, sectionCount: vDSP_Length, count: vDSP_Length) where U : AccelerateBuffer, V : AccelerateMutableBuffer, U.Element == Float, V.Element == Float
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/vectorizablefloat/applysingle(source:destination:delays:setup:sectioncount:count:))*