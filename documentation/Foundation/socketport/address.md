# address

**Framework**: Foundation  
**Kind**: property

The receiver’s socket address structure stored inside an [`NSData`](nsdata.md) object.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var address: Data { get }
```

## See Also

- [init(remoteWithProtocolFamily: Int32, socketType: Int32, protocol: Int32, address: Data)](socketport/init(remotewithprotocolfamily:sockettype:protocol:address:).md)
  Initializes the receiver as a remote socket with the provided arguments.
- [init?(protocolFamily: Int32, socketType: Int32, protocol: Int32, address: Data)](socketport/init(protocolfamily:sockettype:protocol:address:).md)
  Initializes the receiver as a local socket with the provided arguments.
- [var `protocol`: Int32](socketport/protocol.md)
  The protocol that the receiver uses for communication.
- [var protocolFamily: Int32](socketport/protocolfamily.md)
  The protocol family that the receiver uses for communication.
- [var socket: SocketNativeHandle](socketport/socket.md)
  The receiver’s native socket identifier on the platform.
- [var socketType: Int32](socketport/sockettype.md)
  The receiver’s socket type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/socketport/address)*