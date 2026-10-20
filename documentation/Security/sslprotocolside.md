# SSLProtocolSide

**Framework**: Security  
**Kind**: enum  
**Role**: Enumeration

The flags that indicate whether a context is for the server or client side of a connection.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
@frozen
enum SSLProtocolSide
```

```c
enum SSLProtocolSide : int;
```

#### Overview

Use one of these flags with the [`SSLCreateContext(_:_:_:)`](./sslcreatecontext%28_,_,_%29.md) function to indicate whether the context is intended for the server side or client side of a connection.

## Topics

### Constants
- [SSLProtocolSide.serverSide](./sslprotocolside/serverside.md)
  Server side.
- [SSLProtocolSide.clientSide](./sslprotocolside/clientside.md)
  Client side.
### Initializers
- [init?(rawValue: Int32)](./sslprotocolside/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslprotocolside)*