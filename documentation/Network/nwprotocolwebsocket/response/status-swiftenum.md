# NWProtocolWebSocket.Response.Status

**Framework**: Network  
**Kind**: enum

Status values that are sent with a WebSocket server response.

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
enum Status
```

## Topics

### Handshake Status Values
- [NWProtocolWebSocket.Response.Status.accept](nwprotocolwebsocket/response/status-swift.enum/accept.md)
  The client request is being accepted.
- [NWProtocolWebSocket.Response.Status.reject](nwprotocolwebsocket/response/status-swift.enum/reject.md)
  The client request is being rejected.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [init(status: NWProtocolWebSocket.Response.Status, subprotocol: String?, additionalHeaders: [(name: String, value: String)]?)](nwprotocolwebsocket/response/init(status:subprotocol:additionalheaders:).md)
  Initializes a WebSocket server response with a status, selected subprotocol, and additional HTTP headers.
- [let status: NWProtocolWebSocket.Response.Status](nwprotocolwebsocket/response/status-swift.property.md)
  The status of a WebSocket server response.
- [let subprotocol: String?](nwprotocolwebsocket/response/subprotocol.md)
  The selected subprotocol in a WebSocket server response.
- [let additionalHeaders: [(name: String, value: String)]?](nwprotocolwebsocket/response/additionalheaders.md)
  Any additional HTTP headers in a WebSocket server response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolwebsocket/response/status-swift.enum)*