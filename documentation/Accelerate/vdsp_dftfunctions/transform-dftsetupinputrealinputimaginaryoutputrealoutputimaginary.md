# transform(dftSetup:inputReal:inputImaginary:outputReal:outputImaginary:)

**Framework**: Accelerate  
**Kind**: method  
**Required**: Yes

**Availability**:
- iOS 13.0+ - Deprecated
- iPadOS 13.0+ - Deprecated
- Mac Catalyst ?+
- macOS 10.15+ - Deprecated
- tvOS 13.0+ - Deprecated
- watchOS 6.0+ - Deprecated
- Unknown ?+ - Deprecated
- visionOS ?+

## Declaration

```swift
static func transform<U, V>(dftSetup: OpaquePointer, inputReal: U, inputImaginary: U, outputReal: inout V, outputImaginary: inout V) where U : AccelerateBuffer, V : AccelerateMutableBuffer, Self.Scalar == U.Element, U.Element == V.Element
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_dftfunctions/transform(dftsetup:inputreal:inputimaginary:outputreal:outputimaginary:))*