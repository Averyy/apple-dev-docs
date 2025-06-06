# remoteHostname

**Framework**: Network Extension  
**Kind**: property

The flow’s remote hostname, if applicable.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var remoteHostname: String? { get }
```

#### Discussion

This property is only populated for flows originating from create-by-name APIs like [`URLSession`](https://developer.apple.com/documentation/Foundation/URLSession) or [`Network`](https://developer.apple.com/documentation/Network).

## See Also

- [var remoteEndpoint: NWEndpoint?](nefiltersocketflow/remoteendpoint.md)
  An object containing details about the socket’s remote endpoint.
- [class NEFilterFlow](nefilterflow.md)
  The abstract base class for types that represent flows of network data.
- [var localEndpoint: NWEndpoint?](nefiltersocketflow/localendpoint.md)
  An object containing details about the socket’s local endpoint.
- [var socketFamily: Int32](nefiltersocketflow/socketfamily.md)
  The protocol family of the socket.
- [var socketType: Int32](nefiltersocketflow/sockettype.md)
  The type of the socket.
- [var socketProtocol: Int32](nefiltersocketflow/socketprotocol.md)
  The protocol of the socket.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefiltersocketflow/remotehostname)*