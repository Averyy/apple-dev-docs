# notSocket

**Framework**: System  
**Kind**: property

A socket operation was performed on something that isn’t a socket.

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
static var notSocket: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](adopting-errno.md)

#### Discussion

The corresponding C error is `ENOTSOCK`.

## See Also

- [static var notSupportedOnSocket: Errno](errno/notsupportedonsocket.md)
  Operation not supported on socket.
- [static var socketIsConnected: Errno](errno/socketisconnected.md)
  Socket is already connected.
- [static var socketNotConnected: Errno](errno/socketnotconnected.md)
  Socket is not connected.
- [static var socketShutdown: Errno](errno/socketshutdown.md)
  Can’t send after socket shutdown.
- [static var socketTypeNotSupported: Errno](errno/sockettypenotsupported.md)
  Socket type not supported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/notsocket)*