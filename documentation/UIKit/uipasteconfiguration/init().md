# init()

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Initializes a new paste configuration.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
init()
```

```objc
- (instancetype) init;
```

#### Return Value

A paste configuration that has no acceptable uniform type identifiers (UTIs).

#### Discussion

Use this initializer to create a paste configuration that has an empty [`acceptableTypeIdentifiers`](./acceptabletypeidentifiers.md) array. After you create the paste configuration, you can use its [`addAcceptableTypeIdentifiers(_:)`](./addacceptabletypeidentifiers%28_%29.md) method or [`addTypeIdentifiers(forAccepting:)`](./addtypeidentifiers%28foraccepting%29-4fvd6.md) method to add acceptable UTIs to the array.

## See Also

### Initializing a paste configuration
- [convenience init(acceptableTypeIdentifiers: [String])](./init%28acceptabletypeidentifiers%29.md)
  Initializes a new paste configuration with a specified array of acceptable UTIs.
- [convenience init(forAccepting: any NSItemProviderReading.Type)](./init%28foraccepting%29-6is3h.md)
  Initializes a new paste configuration with the UTIs declared as supported by a specified class.
- [convenience init<T>(forAccepting: T.Type)](./init%28foraccepting%29-84r2r.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteconfiguration/init())*