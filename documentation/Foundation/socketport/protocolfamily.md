# protocolFamily

**Framework**: Foundation  
**Kind**: property

The protocol family that the receiver uses for communication.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var protocolFamily: Int32 { get }
```

#### Discussion

Possible values are defined in `<sys/socket.h>`, such as `AF_LOCAL`, `AF_INET`, and `AF_INET6`.

## See Also

- [var address: Data](socketport/address.md)
  The receiver’s socket address structure stored inside an [`NSData`](nsdata.md) object.
- [var `protocol`: Int32](socketport/protocol.md)
  The protocol that the receiver uses for communication.
- [var socket: SocketNativeHandle](socketport/socket.md)
  The receiver’s native socket identifier on the platform.
- [var socketType: Int32](socketport/sockettype.md)
  The receiver’s socket type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/socketport/protocolfamily)*