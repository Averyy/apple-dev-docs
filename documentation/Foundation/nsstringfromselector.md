# NSStringFromSelector(_:)

**Framework**: Foundation  
**Kind**: func

Returns a string representation of a given selector.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func NSStringFromSelector(_ aSelector: Selector) -> String
```

#### Return Value

A string representation of `aSelector`.

## Parameters

- `aSelector`: A selector.

## See Also

- [func NSClassFromString(String) -> AnyClass?](nsclassfromstring(_:).md)
  Obtains a class by name.
- [func NSStringFromClass(AnyClass) -> String](nsstringfromclass(_:).md)
  Returns the name of a class as a string.
- [func NSSelectorFromString(String) -> Selector](nsselectorfromstring(_:).md)
  Returns the selector with a given name.
- [func NSStringFromProtocol(Protocol) -> String](nsstringfromprotocol(_:).md)
  Returns the name of a protocol as a string.
- [func NSProtocolFromString(String) -> Protocol?](nsprotocolfromstring(_:).md)
  Returns a the protocol with a given name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstringfromselector(_:))*