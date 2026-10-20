# init(forAccepting:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Initializes a new paste configuration with the UTIs declared as supported by a specified class.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
convenience init(forAccepting aClass: any NSItemProviderReading.Type)
```

```objc
- (instancetype) initWithTypeIdentifiersForAcceptingClass:(Class<NSItemProviderReading> *) aClass;
```

#### Return Value

A paste configuration initialized with acceptable uniform type identifiers (UTIs) supported by the specified class.

#### Discussion

When you use this initializer, the property [`readableTypeIdentifiersForItemProvider`](../../Foundation/nsitemproviderreading/readabletypeidentifiersforitemprovider.md), implemented on `aClass`, is used to determine the acceptable UTIs.

## Parameters

- `aClass`: A class conforming to the [`NSItemProviderReading`](../../Foundation/nsitemproviderreading.md) protocol.

## See Also

### Initializing a paste configuration
- [init()](./init%28%29.md)
  Initializes a new paste configuration.
- [convenience init(acceptableTypeIdentifiers: [String])](./init%28acceptabletypeidentifiers%29.md)
  Initializes a new paste configuration with a specified array of acceptable UTIs.
- [convenience init<T>(forAccepting: T.Type)](./init%28foraccepting%29-84r2r.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteconfiguration/init(foraccepting:)-6is3h)*