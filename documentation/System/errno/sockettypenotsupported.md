# socketTypeNotSupported

**Framework**: System  
**Kind**: property  
**Role**: Type Property

Socket type not supported.

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
static var socketTypeNotSupported: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](../adopting-errno.md)

#### Discussion

Support for the socket type hasn’t been configured into the system or no implementation for it exists.

The corresponding C error is `ESOCKTNOSUPPORT`.

## See Also

### Network Socket Errors
- [static var notSocket: Errno](./notsocket.md)
  A socket operation was performed on something that isn’t a socket.
- [static var notSupportedOnSocket: Errno](./notsupportedonsocket.md)
  Operation not supported on socket.
- [static var socketIsConnected: Errno](./socketisconnected.md)
  Socket is already connected.
- [static var socketNotConnected: Errno](./socketnotconnected.md)
  Socket is not connected.
- [static var socketShutdown: Errno](./socketshutdown.md)
  Can’t send after socket shutdown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/sockettypenotsupported)*