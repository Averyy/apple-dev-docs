# socketNotConnected

**Framework**: System  
**Kind**: property  
**Role**: Type Property

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

- [Adopting Swift Error Constants](../adopting-errno.md)

#### Discussion

A request to send or receive data wasn’t permitted because the socket wasn’t connected and, when sending on a datagram socket, no address was supplied.

The corresponding C error is `ENOTCONN`.

## See Also

### Network Socket Errors
- [static var notSocket: Errno](./notsocket.md)
  A socket operation was performed on something that isn’t a socket.
- [static var notSupportedOnSocket: Errno](./notsupportedonsocket.md)
  Operation not supported on socket.
- [static var socketIsConnected: Errno](./socketisconnected.md)
  Socket is already connected.
- [static var socketShutdown: Errno](./socketshutdown.md)
  Can’t send after socket shutdown.
- [static var socketTypeNotSupported: Errno](./sockettypenotsupported.md)
  Socket type not supported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/socketnotconnected)*