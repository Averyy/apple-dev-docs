# protocolFamily

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The protocol family that the receiver uses for communication.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var protocolFamily: Int32 { get }
```

```objc
@property (readonly) int protocolFamily;
```

## Discussion

Possible values are defined in `<sys/socket.h>`, such as `AF_LOCAL`, `AF_INET`, and `AF_INET6`.

## See Also

### Getting Information
- [var address: Data](./address.md)
  The receiver’s socket address structure stored inside an [`NSData`](../nsdata.md) object.
- [var `protocol`: Int32](./protocol.md)
  The protocol that the receiver uses for communication.
- [var socket: SocketNativeHandle](./socket.md)
  The receiver’s native socket identifier on the platform.
- [var socketType: Int32](./sockettype.md)
  The receiver’s socket type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/socketport/protocolfamily)*