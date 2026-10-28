# NSStringFromProtocol(_:)

**Framework**: Foundation  
**Kind**: func  
**Role**: Function

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

```c
extern NSString *NSStringFromProtocol(Protocol *proto);
```

## Return Value

A string containing the name of `proto`.

## Parameters

- `proto`: A protocol.

## See Also

### Type Lookup
- [func NSClassFromString(String) -> AnyClass?](./nsclassfromstring%28_%29.md)
  Obtains a class by name.
- [func NSStringFromClass(AnyClass) -> String](./nsstringfromclass%28_%29.md)
  Returns the name of a class as a string.
- [func NSSelectorFromString(String) -> Selector](./nsselectorfromstring%28_%29.md)
  Returns the selector with a given name.
- [func NSStringFromSelector(Selector) -> String](./nsstringfromselector%28_%29.md)
  Returns a string representation of a given selector.
- [func NSProtocolFromString(String) -> Protocol?](./nsprotocolfromstring%28_%29.md)
  Returns a the protocol with a given name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstringfromprotocol(_:))*