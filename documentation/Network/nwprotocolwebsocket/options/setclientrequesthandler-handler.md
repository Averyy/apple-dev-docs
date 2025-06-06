# setClientRequestHandler(_:handler:)

**Framework**: Network  
**Kind**: method

Sets a handler to react to as a server to inbound WebSocket client handshakes.

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
@preconcurrency
func setClientRequestHandler(_ queue: DispatchQueue, handler: @escaping ([String], [(name: String, value: String)]) -> NWProtocolWebSocket.Response)
```

## See Also

- [NWProtocolWebSocket.Response](nwprotocolwebsocket/response.md)
  A WebSocket handshake reponse sent from a server to a client.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolwebsocket/options/setclientrequesthandler(_:handler:))*