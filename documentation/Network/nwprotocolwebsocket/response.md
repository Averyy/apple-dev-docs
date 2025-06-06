# NWProtocolWebSocket.Response

**Framework**: Network  
**Kind**: struct

A WebSocket handshake reponse sent from a server to a client.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
struct Response
```

## Topics

### Sending Handshake Responses
- [init(status: NWProtocolWebSocket.Response.Status, subprotocol: String?, additionalHeaders: [(name: String, value: String)]?)](nwprotocolwebsocket/response/init(status:subprotocol:additionalheaders:).md)
  Initializes a WebSocket server response with a status, selected subprotocol, and additional HTTP headers.
- [NWProtocolWebSocket.Response.Status](nwprotocolwebsocket/response/status-swift.enum.md)
  Status values that are sent with a WebSocket server response.
- [let status: NWProtocolWebSocket.Response.Status](nwprotocolwebsocket/response/status-swift.property.md)
  The status of a WebSocket server response.
- [let subprotocol: String?](nwprotocolwebsocket/response/subprotocol.md)
  The selected subprotocol in a WebSocket server response.
- [let additionalHeaders: [(name: String, value: String)]?](nwprotocolwebsocket/response/additionalheaders.md)
  Any additional HTTP headers in a WebSocket server response.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [func setClientRequestHandler(DispatchQueue, handler: ([String], [(name: String, value: String)]) -> NWProtocolWebSocket.Response)](nwprotocolwebsocket/options/setclientrequesthandler(_:handler:).md)
  Sets a handler to react to as a server to inbound WebSocket client handshakes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolwebsocket/response)*