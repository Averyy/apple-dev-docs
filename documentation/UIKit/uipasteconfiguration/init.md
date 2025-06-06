# init()

**Framework**: UIKit  
**Kind**: init

Initializes a new paste configuration.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init()
```

#### Return Value

A paste configuration that has no acceptable uniform type identifiers (UTIs).

#### Discussion

Use this initializer to create a paste configuration that has an empty [`acceptableTypeIdentifiers`](uipasteconfiguration/acceptabletypeidentifiers.md) array. After you create the paste configuration, you can use its [`addAcceptableTypeIdentifiers(_:)`](uipasteconfiguration/addacceptabletypeidentifiers(_:).md) method or [`addTypeIdentifiers(forAccepting:)`](uipasteconfiguration/addtypeidentifiers(foraccepting:)-4fvd6.md) method to add acceptable UTIs to the array.

## See Also

- [convenience init(acceptableTypeIdentifiers: [String])](uipasteconfiguration/init(acceptabletypeidentifiers:).md)
  Initializes a new paste configuration with a specified array of acceptable UTIs.
- [convenience init(forAccepting: any NSItemProviderReading.Type)](uipasteconfiguration/init(foraccepting:)-6is3h.md)
  Initializes a new paste configuration with the UTIs declared as supported by a specified class.
- [convenience init<T>(forAccepting: T.Type)](uipasteconfiguration/init(foraccepting:)-84r2r.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteconfiguration/init())*