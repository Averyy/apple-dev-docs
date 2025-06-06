# messageTooLong

**Framework**: System  
**Kind**: property

Message too long.

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
static var messageTooLong: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](adopting-errno.md)

#### Discussion

A message sent on a socket was larger than the internal message buffer or some other network limit.

The corresponding C error is `EMSGSIZE`.

## See Also

- [static var connectionAbort: Errno](errno/connectionabort.md)
  Software caused a connection abort.
- [static var connectionRefused: Errno](errno/connectionrefused.md)
  Connection refused.
- [static var connectionReset: Errno](errno/connectionreset.md)
  Connection reset by peer.
- [static var hostIsDown: Errno](errno/hostisdown.md)
  The host is down.
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
- [static var timedOut: Errno](errno/timedout.md)
  Operation timed out.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/messagetoolong)*