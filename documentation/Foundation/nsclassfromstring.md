# NSClassFromString(_:)

**Framework**: Foundation  
**Kind**: func

Obtains a class by name.

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
func NSClassFromString(_ aClassName: String) -> AnyClass?
```

#### Return Value

The class object named by `aClassName`, or `nil` if no class by that name is currently loaded. If `aClassName` is `nil`, returns `nil`.

## Parameters

- `aClassName`: The name of a class.

## See Also

- [func NSStringFromClass(AnyClass) -> String](nsstringfromclass(_:).md)
  Returns the name of a class as a string.
- [func NSSelectorFromString(String) -> Selector](nsselectorfromstring(_:).md)
  Returns the selector with a given name.
- [func NSStringFromSelector(Selector) -> String](nsstringfromselector(_:).md)
  Returns a string representation of a given selector.
- [func NSStringFromProtocol(Protocol) -> String](nsstringfromprotocol(_:).md)
  Returns the name of a protocol as a string.
- [func NSProtocolFromString(String) -> Protocol?](nsprotocolfromstring(_:).md)
  Returns a the protocol with a given name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsclassfromstring(_:))*