# NWProtocolWebSocket.Response

**Framework**: Network  
**Kind**: struct  
**Role**: Structure

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
- [init(status: NWProtocolWebSocket.Response.Status, subprotocol: String?, additionalHeaders: [(name: String, value: String)]?)](./response/init%28status,subprotocol,additionalheaders%29.md)
  Initializes a WebSocket server response with a status, selected subprotocol, and additional HTTP headers.
- [NWProtocolWebSocket.Response.Status](./response/status-swift.enum.md)
  Status values that are sent with a WebSocket server response.
- [let status: NWProtocolWebSocket.Response.Status](./response/status-swift.property.md)
  The status of a WebSocket server response.
- [let subprotocol: String?](./response/subprotocol.md)
  The selected subprotocol in a WebSocket server response.
- [let additionalHeaders: [(name: String, value: String)]?](./response/additionalheaders.md)
  Any additional HTTP headers in a WebSocket server response.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Handling Server Handshakes
- [func setClientRequestHandler(DispatchQueue, handler: ([String], [(name: String, value: String)]) -> NWProtocolWebSocket.Response)](./options/setclientrequesthandler%28_,handler%29.md)
  Sets a handler to react to as a server to inbound WebSocket client handshakes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolwebsocket/response)*