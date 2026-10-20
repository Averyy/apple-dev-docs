# init(status:subprotocol:additionalHeaders:)

**Framework**: Network  
**Kind**: init  
**Role**: Initializer

Initializes a WebSocket server response with a status, selected subprotocol, and additional HTTP headers.

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
init(status: NWProtocolWebSocket.Response.Status, subprotocol: String?, additionalHeaders: [(name: String, value: String)]? = nil)
```

## See Also

### Sending Handshake Responses
- [NWProtocolWebSocket.Response.Status](./status-swift.enum.md)
  Status values that are sent with a WebSocket server response.
- [let status: NWProtocolWebSocket.Response.Status](./status-swift.property.md)
  The status of a WebSocket server response.
- [let subprotocol: String?](./subprotocol.md)
  The selected subprotocol in a WebSocket server response.
- [let additionalHeaders: [(name: String, value: String)]?](./additionalheaders.md)
  Any additional HTTP headers in a WebSocket server response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolwebsocket/response/init(status:subprotocol:additionalheaders:))*