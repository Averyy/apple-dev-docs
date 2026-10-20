# socket

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The receiver’s native socket identifier on the platform.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var socket: SocketNativeHandle { get }
```

```objc
@property (readonly) NSSocketNativeHandle socket;
```

#### Discussion

In macOS, the native socket identifier is an integer file descriptor.

## See Also

### Getting Information
- [var address: Data](./address.md)
  The receiver’s socket address structure stored inside an [`NSData`](../nsdata.md) object.
- [var `protocol`: Int32](./protocol.md)
  The protocol that the receiver uses for communication.
- [var protocolFamily: Int32](./protocolfamily.md)
  The protocol family that the receiver uses for communication.
- [var socketType: Int32](./sockettype.md)
  The receiver’s socket type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/socketport/socket)*