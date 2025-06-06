# subprotocol

**Framework**: Network  
**Kind**: property

The selected subprotocol in a WebSocket server response.

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
let subprotocol: String?
```

## See Also

- [init(status: NWProtocolWebSocket.Response.Status, subprotocol: String?, additionalHeaders: [(name: String, value: String)]?)](nwprotocolwebsocket/response/init(status:subprotocol:additionalheaders:).md)
  Initializes a WebSocket server response with a status, selected subprotocol, and additional HTTP headers.
- [NWProtocolWebSocket.Response.Status](nwprotocolwebsocket/response/status-swift.enum.md)
  Status values that are sent with a WebSocket server response.
- [let status: NWProtocolWebSocket.Response.Status](nwprotocolwebsocket/response/status-swift.property.md)
  The status of a WebSocket server response.
- [let additionalHeaders: [(name: String, value: String)]?](nwprotocolwebsocket/response/additionalheaders.md)
  Any additional HTTP headers in a WebSocket server response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolwebsocket/response/subprotocol)*