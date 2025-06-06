# addTypeIdentifiers(forAccepting:)

**Framework**: UIKit  
**Kind**: method

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func addTypeIdentifiers<T>(forAccepting aClass: T.Type) where T : _ObjectiveCBridgeable, T._ObjectiveCType : NSItemProviderReading
```

## See Also

- [func addAcceptableTypeIdentifiers([String])](uipasteconfiguration/addacceptabletypeidentifiers(_:).md)
  Adds an array of UTI strings to a paste configuration, increasing the variety of types the paste configuration accepts.
- [func addTypeIdentifiers(forAccepting: any NSItemProviderReading.Type)](uipasteconfiguration/addtypeidentifiers(foraccepting:)-4fvd6.md)
  Expands the array of accepted UTIs for a paste configuration, based on those declared as supported by a specified class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteconfiguration/addtypeidentifiers(foraccepting:)-8af7o)*