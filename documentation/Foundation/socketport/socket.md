# socket

**Framework**: Foundation  
**Kind**: property

The receiver’s native socket identifier on the platform.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var socket: SocketNativeHandle { get }
```

#### Discussion

In macOS, the native socket identifier is an integer file descriptor.

## See Also

- [var address: Data](socketport/address.md)
  The receiver’s socket address structure stored inside an [`NSData`](nsdata.md) object.
- [var `protocol`: Int32](socketport/protocol.md)
  The protocol that the receiver uses for communication.
- [var protocolFamily: Int32](socketport/protocolfamily.md)
  The protocol family that the receiver uses for communication.
- [var socketType: Int32](socketport/sockettype.md)
  The receiver’s socket type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/socketport/socket)*