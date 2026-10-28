# notSupportedOnSocket

**Framework**: System  
**Kind**: property  
**Role**: Type Property

Operation not supported on socket.

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
static var notSupportedOnSocket: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](../adopting-errno.md)

## Discussion

The attempted operation isn’t supported for the type of socket referenced; for example, trying to accept a connection on a datagram socket.

The corresponding C error is `EOPNOTSUPP`.

## See Also

### Network Socket Errors
- [static var notSocket: Errno](./notsocket.md)
  A socket operation was performed on something that isn’t a socket.
- [static var socketIsConnected: Errno](./socketisconnected.md)
  Socket is already connected.
- [static var socketNotConnected: Errno](./socketnotconnected.md)
  Socket is not connected.
- [static var socketShutdown: Errno](./socketshutdown.md)
  Can’t send after socket shutdown.
- [static var socketTypeNotSupported: Errno](./sockettypenotsupported.md)
  Socket type not supported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/notsupportedonsocket)*