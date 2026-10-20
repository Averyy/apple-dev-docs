# makeDFTSetup(previous:count:direction:transformType:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Type Method

**Availability**:
- iOS 13.0+ - Deprecated
- iPadOS 13.0+ - Deprecated
- Mac Catalyst 13.0+ - Deprecated
- macOS 10.15+ - Deprecated
- tvOS 13.0+ - Deprecated
- visionOS
- watchOS 6.0+ - Deprecated

> **Deprecated**: Use `vDSP.DiscreteFourierTransform`.

## Declaration

```swift
static func makeDFTSetup<T>(previous: vDSP.DFT<T>? = nil, count: Int, direction: vDSP.FourierTransformDirection, transformType: vDSP.DFTTransformType) -> OpaquePointer? where T : vDSP_FloatingPointDiscreteFourierTransformable
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/vectorizabledouble/makedftsetup(previous:count:direction:transformtype:))*