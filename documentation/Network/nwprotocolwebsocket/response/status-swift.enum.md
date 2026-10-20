# NWProtocolWebSocket.Response.Status

**Framework**: Network  
**Kind**: enum  
**Role**: Enumeration

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
- [NWProtocolWebSocket.Response.Status.accept](./status-swift.enum/accept.md)
  The client request is being accepted.
- [NWProtocolWebSocket.Response.Status.reject](./status-swift.enum/reject.md)
  The client request is being rejected.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Sending Handshake Responses
- [init(status: NWProtocolWebSocket.Response.Status, subprotocol: String?, additionalHeaders: [(name: String, value: String)]?)](./init%28status,subprotocol,additionalheaders%29.md)
  Initializes a WebSocket server response with a status, selected subprotocol, and additional HTTP headers.
- [let status: NWProtocolWebSocket.Response.Status](./status-swift.property.md)
  The status of a WebSocket server response.
- [let subprotocol: String?](./subprotocol.md)
  The selected subprotocol in a WebSocket server response.
- [let additionalHeaders: [(name: String, value: String)]?](./additionalheaders.md)
  Any additional HTTP headers in a WebSocket server response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolwebsocket/response/status-swift.enum)*