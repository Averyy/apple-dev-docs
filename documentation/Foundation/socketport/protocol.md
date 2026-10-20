# protocol

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The protocol that the receiver uses for communication.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var `protocol`: Int32 { get }
```

```objc
@property (readonly) int protocol;
```

## See Also

### Getting Information
- [var address: Data](./address.md)
  The receiver’s socket address structure stored inside an [`NSData`](../nsdata.md) object.
- [var protocolFamily: Int32](./protocolfamily.md)
  The protocol family that the receiver uses for communication.
- [var socket: SocketNativeHandle](./socket.md)
  The receiver’s native socket identifier on the platform.
- [var socketType: Int32](./sockettype.md)
  The receiver’s socket type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/socketport/protocol)*