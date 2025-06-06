# addTypeIdentifiers(forAccepting:)

**Framework**: UIKit  
**Kind**: method

Expands the array of accepted UTIs for a paste configuration, based on those declared as supported by a specified class.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func addTypeIdentifiers(forAccepting aClass: any NSItemProviderReading.Type)
```

#### Discussion

This method uses the property [`readableTypeIdentifiersForItemProvider`](https://developer.apple.com/documentation/foundation/nsitemproviderreading/2888305-readabletypeidentifiersforitempr), implemented on `aClass`, to determine the uniform type identifiers (UTIs) to add to the paste configuration’s [`acceptableTypeIdentifiers`](uipasteconfiguration/acceptabletypeidentifiers.md) array.

## Parameters

- `aClass`: A class conforming to the   protocol.

## See Also

- [func addAcceptableTypeIdentifiers([String])](uipasteconfiguration/addacceptabletypeidentifiers(_:).md)
  Adds an array of UTI strings to a paste configuration, increasing the variety of types the paste configuration accepts.
- [func addTypeIdentifiers<T>(forAccepting: T.Type)](uipasteconfiguration/addtypeidentifiers(foraccepting:)-8af7o.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteconfiguration/addtypeidentifiers(foraccepting:)-4fvd6)*