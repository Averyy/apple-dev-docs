# init(forAccepting:)

**Framework**: UIKit  
**Kind**: init

Initializes a new paste configuration with the UTIs declared as supported by a specified class.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
convenience init(forAccepting aClass: any NSItemProviderReading.Type)
```

#### Return Value

A paste configuration initialized with acceptable uniform type identifiers (UTIs) supported by the specified class.

#### Discussion

When you use this initializer, the property [`readableTypeIdentifiersForItemProvider`](https://developer.apple.com/documentation/foundation/nsitemproviderreading/2888305-readabletypeidentifiersforitempr), implemented on `aClass`, is used to determine the acceptable UTIs.

## Parameters

- `aClass`: A class conforming to the   protocol.

## See Also

- [init()](uipasteconfiguration/init.md)
  Initializes a new paste configuration.
- [convenience init(acceptableTypeIdentifiers: [String])](uipasteconfiguration/init(acceptabletypeidentifiers:).md)
  Initializes a new paste configuration with a specified array of acceptable UTIs.
- [convenience init<T>(forAccepting: T.Type)](uipasteconfiguration/init(foraccepting:)-84r2r.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteconfiguration/init(foraccepting:)-6is3h)*