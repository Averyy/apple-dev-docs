# networkUnreachable

**Framework**: System  
**Kind**: property  
**Role**: Type Property

Network is unreachable.

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
static var networkUnreachable: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](../adopting-errno.md)

## Discussion

A socket operation was attempted to an unreachable network.

The corresponding C error is `ENETUNREACH`.

## See Also

### Network Errors
- [static var connectionAbort: Errno](./connectionabort.md)
  Software caused a connection abort.
- [static var connectionRefused: Errno](./connectionrefused.md)
  Connection refused.
- [static var connectionReset: Errno](./connectionreset.md)
  Connection reset by peer.
- [static var hostIsDown: Errno](./hostisdown.md)
  The host is down.
- [static var messageTooLong: Errno](./messagetoolong.md)
  Message too long.
- [static var networkDown: Errno](./networkdown.md)
  Network is down.
- [static var networkReset: Errno](./networkreset.md)
  Network dropped connection on reset.
- [static var noBufferSpace: Errno](./nobufferspace.md)
  No buffer space available.
- [static var noRouteToHost: Errno](./noroutetohost.md)
  No route to host.
- [static var notSupported: Errno](./notsupported.md)
  Not supported.
- [static var timedOut: Errno](./timedout.md)
  Operation timed out.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/networkunreachable)*