# NWProtocolWebSocket.Opcode

**Framework**: Network  
**Kind**: enum

Types of messages that you send and receive on a WebSocket connection.

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
enum Opcode
```

## Topics

### Data Types
- [NWProtocolWebSocket.Opcode.binary](nwprotocolwebsocket/opcode/binary.md)
  A binary data message.
- [NWProtocolWebSocket.Opcode.text](nwprotocolwebsocket/opcode/text.md)
  A text data message.
- [NWProtocolWebSocket.Opcode.cont](nwprotocolwebsocket/opcode/cont.md)
  A continuation message.
### Control Types
- [NWProtocolWebSocket.Opcode.ping](nwprotocolwebsocket/opcode/ping.md)
  A Ping message, which requests a Pong from the peer.
- [NWProtocolWebSocket.Opcode.pong](nwprotocolwebsocket/opcode/pong.md)
  A Pong message in response to a Ping from the peer.
- [NWProtocolWebSocket.Opcode.close](nwprotocolwebsocket/opcode/close.md)
  A message indicating a close of the connection.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [init(opcode: NWProtocolWebSocket.Opcode)](nwprotocolwebsocket/metadata/init(opcode:).md)
  Initializes a WebSocket message with a specific type code.
- [func setPongHandler(DispatchQueue, handler: (NWError?) -> Void)](nwprotocolwebsocket/metadata/setponghandler(_:handler:).md)
  Sets a handler on a Ping message to be invoked when the corresponding Pong message is received.
- [var closeCode: NWProtocolWebSocket.CloseCode](nwprotocolwebsocket/metadata/closecode.md)
  The close code on a WebSocket message.
- [NWProtocolWebSocket.CloseCode](nwprotocolwebsocket/closecode.md)
  Types of codes used upon closing a WebSocket connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolwebsocket/opcode)*