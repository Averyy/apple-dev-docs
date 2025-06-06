# localEndpoint

**Framework**: Network Extension  
**Kind**: property

An object containing details about the socket’s local endpoint.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var localEndpoint: NWEndpoint? { get }
```

#### Discussion

This endpoint object may be `nil` when the system calls your [`handleNewFlow(_:)`](nefilterdataprovider/handlenewflow(_:).md) method; if so, receiving network data populates the object. In such a case, the filter may still perform filtering, based on its socket type, socket family, or socket protocol.

## See Also

- [var remoteEndpoint: NWEndpoint?](nefiltersocketflow/remoteendpoint.md)
  An object containing details about the socket’s remote endpoint.
- [var remoteHostname: String?](nefiltersocketflow/remotehostname.md)
  The flow’s remote hostname, if applicable.
- [class NEFilterFlow](nefilterflow.md)
  The abstract base class for types that represent flows of network data.
- [var socketFamily: Int32](nefiltersocketflow/socketfamily.md)
  The protocol family of the socket.
- [var socketType: Int32](nefiltersocketflow/sockettype.md)
  The type of the socket.
- [var socketProtocol: Int32](nefiltersocketflow/socketprotocol.md)
  The protocol of the socket.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefiltersocketflow/localendpoint)*