# address

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The receiver’s socket address structure stored inside an [`NSData`](../nsdata.md) object.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var address: Data { get }
```

```objc
@property (copy, readonly) NSData * address;
```

## See Also

### Related Documentation
- [init(remoteWithProtocolFamily: Int32, socketType: Int32, protocol: Int32, address: Data)](./init%28remotewithprotocolfamily,sockettype,protocol,address%29.md)
  Initializes the receiver as a remote socket with the provided arguments.
- [init?(protocolFamily: Int32, socketType: Int32, protocol: Int32, address: Data)](./init%28protocolfamily,sockettype,protocol,address%29.md)
  Initializes the receiver as a local socket with the provided arguments.
### Getting Information
- [var `protocol`: Int32](./protocol.md)
  The protocol that the receiver uses for communication.
- [var protocolFamily: Int32](./protocolfamily.md)
  The protocol family that the receiver uses for communication.
- [var socket: SocketNativeHandle](./socket.md)
  The receiver’s native socket identifier on the platform.
- [var socketType: Int32](./sockettype.md)
  The receiver’s socket type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/socketport/address)*