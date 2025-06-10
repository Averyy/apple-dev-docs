# SSLProtocolSide

**Framework**: Security  
**Kind**: enum

The flags that indicate whether a context is for the server or client side of a connection.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
@frozen
enum SSLProtocolSide
```

#### Overview

Use one of these flags with the [`SSLCreateContext(_:_:_:)`](sslcreatecontext(_:_:_:).md) function to indicate whether the context is intended for the server side or client side of a connection.

## Topics

### Constants
- [SSLProtocolSide.serverSide](sslprotocolside/serverside.md)
  Server side.
- [SSLProtocolSide.clientSide](sslprotocolside/clientside.md)
  Client side.
### Initializers
- [init?(rawValue: Int32)](sslprotocolside/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslprotocolside)*