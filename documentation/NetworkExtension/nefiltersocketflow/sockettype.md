# socketType

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

The type of the socket.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var socketType: Int32 { get }
```

```objc
@property (readonly) int socketType;
```

#### Discussion

Examples of socket types include `SOCK_STREAM` and `SOCK_DGRAM`.

## See Also

### Getting socket flow properties
- [var remoteEndpoint: NWEndpoint?](./remoteendpoint.md)
  An object containing details about the socket’s remote endpoint.
- [var remoteHostname: String?](./remotehostname.md)
  The flow’s remote hostname, if applicable.
- [class NEFilterFlow](../nefilterflow.md)
  The abstract base class for types that represent flows of network data.
- [var localEndpoint: NWEndpoint?](./localendpoint.md)
  An object containing details about the socket’s local endpoint.
- [var socketFamily: Int32](./socketfamily.md)
  The protocol family of the socket.
- [var socketProtocol: Int32](./socketprotocol.md)
  The protocol of the socket.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefiltersocketflow/sockettype)*