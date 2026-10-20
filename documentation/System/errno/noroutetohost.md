# noRouteToHost

**Framework**: System  
**Kind**: property  
**Role**: Type Property

No route to host.

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
static var noRouteToHost: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](../adopting-errno.md)

#### Discussion

A socket operation failed because the destination host was unreachable.

The corresponding C error is `EHOSTUNREACH`.

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
- [static var networkUnreachable: Errno](./networkunreachable.md)
  Network is unreachable.
- [static var noBufferSpace: Errno](./nobufferspace.md)
  No buffer space available.
- [static var notSupported: Errno](./notsupported.md)
  Not supported.
- [static var timedOut: Errno](./timedout.md)
  Operation timed out.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/noroutetohost)*