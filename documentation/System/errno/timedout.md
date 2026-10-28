# timedOut

**Framework**: System  
**Kind**: property  
**Role**: Type Property

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

- [Adopting Swift Error Constants](../adopting-errno.md)

## Discussion

A `connect(2)`, `connectx(2)` or `send(2)` request failed because the connected party didn’t properly respond within the required period of time. The timeout period is dependent on the communication protocol.

The corresponding C error is `ETIMEDOUT`.

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
- [static var noRouteToHost: Errno](./noroutetohost.md)
  No route to host.
- [static var notSupported: Errno](./notsupported.md)
  Not supported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/timedout)*