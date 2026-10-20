# socketType

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The receiver’s socket type.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var socketType: Int32 { get }
```

```objc
@property (readonly) int socketType;
```

## See Also

### Getting Information
- [var address: Data](./address.md)
  The receiver’s socket address structure stored inside an [`NSData`](../nsdata.md) object.
- [var `protocol`: Int32](./protocol.md)
  The protocol that the receiver uses for communication.
- [var protocolFamily: Int32](./protocolfamily.md)
  The protocol family that the receiver uses for communication.
- [var socket: SocketNativeHandle](./socket.md)
  The receiver’s native socket identifier on the platform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/socketport/sockettype)*