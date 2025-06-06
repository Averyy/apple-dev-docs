# NSSelectorFromString(_:)

**Framework**: Foundation  
**Kind**: func

Returns the selector with a given name.

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
func NSSelectorFromString(_ aSelectorName: String) -> Selector
```

#### Return Value

The selector named by `aSelectorName`. If `aSelectorName` is `nil`, or cannot be converted to UTF-8 (this should be only due to insufficient memory), returns `(SEL)0`.

#### Discussion

To make a selector, [`NSSelectorFromString(_:)`](nsselectorfromstring(_:).md) passes a UTF-8 encoded character representation of `aSelectorName` to [`sel_registerName(_:)`](https://developer.apple.com/documentation/ObjectiveC/sel_registerName(_:)) and returns the value returned by that function. Note, therefore, that if the selector does not exist it is registered and the newly-registered selector is returned.

Recall that a colon (”:”) is part of a method name; `setHeight` is not the same as `setHeight:`.

## Parameters

- `aSelectorName`: A string of any length, with any characters, that represents the name of a selector.

## See Also

- [func NSClassFromString(String) -> AnyClass?](nsclassfromstring(_:).md)
  Obtains a class by name.
- [func NSStringFromClass(AnyClass) -> String](nsstringfromclass(_:).md)
  Returns the name of a class as a string.
- [func NSStringFromSelector(Selector) -> String](nsstringfromselector(_:).md)
  Returns a string representation of a given selector.
- [func NSStringFromProtocol(Protocol) -> String](nsstringfromprotocol(_:).md)
  Returns the name of a protocol as a string.
- [func NSProtocolFromString(String) -> Protocol?](nsprotocolfromstring(_:).md)
  Returns a the protocol with a given name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsselectorfromstring(_:))*