# CFSocketError

**Framework**: Core Foundation  
**Kind**: enum

Error codes for many CFSocket functions.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
enum CFSocketError
```

## Topics

### Constants
- [CFSocketError.success](cfsocketerror/success.md)
  The socket operation succeeded.
- [CFSocketError.error](cfsocketerror/error.md)
  The socket operation failed.
- [CFSocketError.timeout](cfsocketerror/timeout.md)
  The socket operation timed out.
### Initializers
- [init?(rawValue: CFIndex)](cfsocketerror/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct CFSocketCallBackType](cfsocketcallbacktype.md)
  Types of socket activity that can cause the callback function of a CFSocket object to be called.
- [CFSocket Flags](1560944-cfsocket-flags.md)
  Flags that can be set on a CFSocket object to control its behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfsocketerror)*