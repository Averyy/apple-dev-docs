# transform(dftSetup:inputReal:inputImaginary:outputReal:outputImaginary:)

**Framework**: Accelerate  
**Kind**: method

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
static func transform<U, V>(dftSetup: OpaquePointer, inputReal: U, inputImaginary: U, outputReal: inout V, outputImaginary: inout V) where U : AccelerateBuffer, V : AccelerateMutableBuffer, U.Element == Double, V.Element == Double
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/vectorizabledouble/transform(dftsetup:inputreal:inputimaginary:outputreal:outputimaginary:))*