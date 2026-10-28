# extendedInterfaceCreator

**Framework**: TVMLKit  
**Kind**: property  
**Role**: Instance Property

The interface that is being extended.

**Availability**:
- tvOS 9.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
var extendedInterfaceCreator: (any TVInterfaceCreating)? { get set }
```

```objc
@property (nonatomic, strong, nullable) id<TVInterfaceCreating> extendedInterfaceCreator;
```

## Mentions

- [Creating TVML Elements](../creating-tvml-elements.md)

## Discussion

An app can extend or override framework implementation by setting the [`extendedInterfaceCreator`](./extendedinterfacecreator.md) property. An app must provide its own methods to handle custom registered elements.

## See Also

### Extending an Interface
- [class func shared() -> Self](./shared%28%29.md)
  Returns the singleton instance of the interface factory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvinterfacefactory/extendedinterfacecreator)*