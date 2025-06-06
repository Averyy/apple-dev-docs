# NSStringFromClass(_:)

**Framework**: Foundation  
**Kind**: func

Returns the name of a class as a string.

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
func NSStringFromClass(_ aClass: AnyClass) -> String
```

#### Return Value

A string containing the name of `aClass`. If `aClass` is `nil`, returns `nil`.

## Parameters

- `aClass`: A class.

## See Also

- [func NSClassFromString(String) -> AnyClass?](nsclassfromstring(_:).md)
  Obtains a class by name.
- [func NSSelectorFromString(String) -> Selector](nsselectorfromstring(_:).md)
  Returns the selector with a given name.
- [func NSStringFromSelector(Selector) -> String](nsstringfromselector(_:).md)
  Returns a string representation of a given selector.
- [func NSStringFromProtocol(Protocol) -> String](nsstringfromprotocol(_:).md)
  Returns the name of a protocol as a string.
- [func NSProtocolFromString(String) -> Protocol?](nsprotocolfromstring(_:).md)
  Returns a the protocol with a given name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstringfromclass(_:))*