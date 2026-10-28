# socketFamily

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

The protocol family of the socket.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var socketFamily: Int32 { get }
```

```objc
@property (readonly) int socketFamily;
```

## Discussion

Examples of protocol families include symbols like `PF_INET` and `PF_INET6`.

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
- [var socketType: Int32](./sockettype.md)
  The type of the socket.
- [var socketProtocol: Int32](./socketprotocol.md)
  The protocol of the socket.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefiltersocketflow/socketfamily)*