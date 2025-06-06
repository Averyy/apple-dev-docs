# SSLSessionState

**Framework**: Security  
**Kind**: enum

The flags that represent the state of an SSL session.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
@frozen
enum SSLSessionState
```

## Topics

### Constants
- [SSLSessionState.idle](sslsessionstate/idle.md)
  No I/O has been performed yet.
- [SSLSessionState.handshake](sslsessionstate/handshake.md)
  The SSL handshake is in progress.
- [SSLSessionState.connected](sslsessionstate/connected.md)
  The SSL handshake is complete; the connection is ready for normal I/O.
- [SSLSessionState.closed](sslsessionstate/closed.md)
  The connection closed normally.
- [SSLSessionState.aborted](sslsessionstate/aborted.md)
  The connection aborted.
### Initializers
- [init?(rawValue: Int32)](sslsessionstate/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslsessionstate)*