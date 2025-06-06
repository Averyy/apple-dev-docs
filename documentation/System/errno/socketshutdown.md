# socketShutdown

**Framework**: System  
**Kind**: property

Can’t send after socket shutdown.

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
static var socketShutdown: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](adopting-errno.md)

#### Discussion

A request to send data wasn’t permitted because the socket had already been shut down with a previous `shutdown(2)` call.

The corresponding C error is `ESHUTDOWN`.

## See Also

- [static var notSocket: Errno](errno/notsocket.md)
  A socket operation was performed on something that isn’t a socket.
- [static var notSupportedOnSocket: Errno](errno/notsupportedonsocket.md)
  Operation not supported on socket.
- [static var socketIsConnected: Errno](errno/socketisconnected.md)
  Socket is already connected.
- [static var socketNotConnected: Errno](errno/socketnotconnected.md)
  Socket is not connected.
- [static var socketTypeNotSupported: Errno](errno/sockettypenotsupported.md)
  Socket type not supported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/socketshutdown)*