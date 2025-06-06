# socketIsConnected

**Framework**: System  
**Kind**: property

Socket is already connected.

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
static var socketIsConnected: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](adopting-errno.md)

#### Discussion

A `connect(2)` or `connectx(2)` request was made on an already connected socket, or a `sendto(2)` or `sendmsg(2)` request was made on a connected socket specified a destination when already connected.

The corresponding C error is `EISCONN`.

## See Also

- [static var notSocket: Errno](errno/notsocket.md)
  A socket operation was performed on something that isn’t a socket.
- [static var notSupportedOnSocket: Errno](errno/notsupportedonsocket.md)
  Operation not supported on socket.
- [static var socketNotConnected: Errno](errno/socketnotconnected.md)
  Socket is not connected.
- [static var socketShutdown: Errno](errno/socketshutdown.md)
  Can’t send after socket shutdown.
- [static var socketTypeNotSupported: Errno](errno/sockettypenotsupported.md)
  Socket type not supported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/socketisconnected)*