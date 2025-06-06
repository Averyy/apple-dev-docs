# NSStringFromProtocol(_:)

**Framework**: Foundation  
**Kind**: func

Returns the name of a protocol as a string.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func NSStringFromProtocol(_ proto: Protocol) -> String
```

#### Return Value

A string containing the name of `proto`.

## Parameters

- `proto`: A protocol.

## See Also

- [func NSClassFromString(String) -> AnyClass?](nsclassfromstring(_:).md)
  Obtains a class by name.
- [func NSStringFromClass(AnyClass) -> String](nsstringfromclass(_:).md)
  Returns the name of a class as a string.
- [func NSSelectorFromString(String) -> Selector](nsselectorfromstring(_:).md)
  Returns the selector with a given name.
- [func NSStringFromSelector(Selector) -> String](nsstringfromselector(_:).md)
  Returns a string representation of a given selector.
- [func NSProtocolFromString(String) -> Protocol?](nsprotocolfromstring(_:).md)
  Returns a the protocol with a given name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstringfromprotocol(_:))*