# noBufferSpace

**Framework**: System  
**Kind**: property

No buffer space available.

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
static var noBufferSpace: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](adopting-errno.md)

#### Discussion

An operation on a socket or pipe wasn’t performed because the system lacked sufficient buffer space or because a queue was full.

The corresponding C error is `ENOBUFS`.

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
- [static var noRouteToHost: Errno](errno/noroutetohost.md)
  No route to host.
- [static var notSupported: Errno](errno/notsupported.md)
  Not supported.
- [static var timedOut: Errno](errno/timedout.md)
  Operation timed out.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/nobufferspace)*