# timedOut

**Framework**: System  
**Kind**: property

Operation timed out.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
static var timedOut: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](adopting-errno.md)

#### Discussion

A `connect(2)`, `connectx(2)` or `send(2)` request failed because the connected party didn’t properly respond within the required period of time. The timeout period is dependent on the communication protocol.

The corresponding C error is `ETIMEDOUT`.

## See Also

- [static var connectionAbort: Errno](errno/connectionabort.md)
  Software caused a connection abort.
- [static var connectionRefused: Errno](errno/connectionrefused.md)
  Connection refused.
- [static var connectionReset: Errno](errno/connectionreset.md)
  Connection reset by peer.
- [static var hostIsDown: Errno](errno/hostisdown.md)
  The host is down.
- [static var messageTooLong: Errno](errno/messagetoolong.md)
  Message too long.
- [static var networkDown: Errno](errno/networkdown.md)
  Network is down.
- [static var networkReset: Errno](errno/networkreset.md)
  Network dropped connection on reset.
- [static var networkUnreachable: Errno](errno/networkunreachable.md)
  Network is unreachable.
- [static var noBufferSpace: Errno](errno/nobufferspace.md)
  No buffer space available.
- [static var noRouteToHost: Errno](errno/noroutetohost.md)
  No route to host.
- [static var notSupported: Errno](errno/notsupported.md)
  Not supported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/timedout)*