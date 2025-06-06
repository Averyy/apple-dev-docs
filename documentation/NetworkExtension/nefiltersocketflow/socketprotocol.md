# socketProtocol

**Framework**: Network Extension  
**Kind**: property

The protocol of the socket.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var socketProtocol: Int32 { get }
```

#### Discussion

Examples of protocols include `IPPROTO_TCP` and `IPPROTO_IP`.

## See Also

- [var remoteEndpoint: NWEndpoint?](nefiltersocketflow/remoteendpoint.md)
  An object containing details about the socket’s remote endpoint.
- [var remoteHostname: String?](nefiltersocketflow/remotehostname.md)
  The flow’s remote hostname, if applicable.
- [class NEFilterFlow](nefilterflow.md)
  The abstract base class for types that represent flows of network data.
- [var localEndpoint: NWEndpoint?](nefiltersocketflow/localendpoint.md)
  An object containing details about the socket’s local endpoint.
- [var socketFamily: Int32](nefiltersocketflow/socketfamily.md)
  The protocol family of the socket.
- [var socketType: Int32](nefiltersocketflow/sockettype.md)
  The type of the socket.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefiltersocketflow/socketprotocol)*