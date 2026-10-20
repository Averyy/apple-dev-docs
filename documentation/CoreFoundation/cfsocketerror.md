# CFSocketError

**Framework**: Core Foundation  
**Kind**: enum  
**Role**: Enumeration

Error codes for many CFSocket functions.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
enum CFSocketError
```

```c
enum CFSocketError : CFIndex;
```

## Topics

### Constants
- [CFSocketError.success](./cfsocketerror/success.md)
  The socket operation succeeded.
- [CFSocketError.error](./cfsocketerror/error.md)
  The socket operation failed.
- [CFSocketError.timeout](./cfsocketerror/timeout.md)
  The socket operation timed out.
### Initializers
- [init?(rawValue: CFIndex)](./cfsocketerror/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Constants
- [struct CFSocketCallBackType](./cfsocketcallbacktype.md)
  Types of socket activity that can cause the callback function of a CFSocket object to be called.
- [CFSocket Flags](./api-1560944-cfsocket-flags.md)
  Flags that can be set on a CFSocket object to control its behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfsocketerror)*