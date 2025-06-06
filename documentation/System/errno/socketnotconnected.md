# socketNotConnected

**Framework**: System  
**Kind**: property

Socket is not connected.

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
static var socketNotConnected: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](adopting-errno.md)

#### Discussion

A request to send or receive data wasn’t permitted because the socket wasn’t connected and, when sending on a datagram socket, no address was supplied.

The corresponding C error is `ENOTCONN`.

## See Also

- [static var notSocket: Errno](errno/notsocket.md)
  A socket operation was performed on something that isn’t a socket.
- [static var notSupportedOnSocket: Errno](errno/notsupportedonsocket.md)
  Operation not supported on socket.
- [static var socketIsConnected: Errno](errno/socketisconnected.md)
  Socket is already connected.
- [static var socketShutdown: Errno](errno/socketshutdown.md)
  Can’t send after socket shutdown.
- [static var socketTypeNotSupported: Errno](errno/sockettypenotsupported.md)
  Socket type not supported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/socketnotconnected)*