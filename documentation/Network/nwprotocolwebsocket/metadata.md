# NWProtocolWebSocket.Metadata

**Framework**: Network  
**Kind**: class

A WebSocket message you configure when sending and receiving packets.

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
class Metadata
```

## Topics

### Sending Messages
- [init(opcode: NWProtocolWebSocket.Opcode)](nwprotocolwebsocket/metadata/init(opcode:).md)
  Initializes a WebSocket message with a specific type code.
- [NWProtocolWebSocket.Opcode](nwprotocolwebsocket/opcode.md)
  Types of messages that you send and receive on a WebSocket connection.
- [func setPongHandler(DispatchQueue, handler: (NWError?) -> Void)](nwprotocolwebsocket/metadata/setponghandler(_:handler:).md)
  Sets a handler on a Ping message to be invoked when the corresponding Pong message is received.
- [var closeCode: NWProtocolWebSocket.CloseCode](nwprotocolwebsocket/metadata/closecode.md)
  The close code on a WebSocket message.
- [NWProtocolWebSocket.CloseCode](nwprotocolwebsocket/closecode.md)
  Types of codes used upon closing a WebSocket connection.
### Receiving Messages
- [let opcode: NWProtocolWebSocket.Opcode](nwprotocolwebsocket/metadata/opcode.md)
  The type code of a WebSocket message.
- [var closeCode: NWProtocolWebSocket.CloseCode](nwprotocolwebsocket/metadata/closecode.md)
  The close code on a WebSocket message.
- [NWProtocolWebSocket.CloseCode](nwprotocolwebsocket/closecode.md)
  Types of codes used upon closing a WebSocket connection.
### Inspecting Handshake Results
- [var selectedSubprotocol: String?](nwprotocolwebsocket/metadata/selectedsubprotocol.md)
  The subprotocol selected by the server during the WebSocket handshake.
- [var additionalServerHeaders: [(String, String)]?](nwprotocolwebsocket/metadata/additionalserverheaders.md)
  Additional HTTP headers sent by the server during the WebSocket handshake.

## Relationships

### Inherits From
- [NWProtocolMetadata](nwprotocolmetadata.md)
### Conforms To
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolwebsocket/metadata)*