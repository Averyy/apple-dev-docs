# shared()

**Framework**: TVMLKit  
**Kind**: method  
**Role**: Type Method

Returns the singleton instance of the interface factory.

**Availability**:
- tvOS 9.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
class func shared() -> Self
```

```objc
+ (instancetype) sharedInterfaceFactory;
```

## Mentions

- [Creating TVML Elements](../creating-tvml-elements.md)

#### Return Value

The shared interface factory.

## See Also

### Extending an Interface
- [var extendedInterfaceCreator: (any TVInterfaceCreating)?](./extendedinterfacecreator.md)
  The interface that is being extended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvinterfacefactory/shared())*