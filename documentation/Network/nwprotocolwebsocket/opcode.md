# NWProtocolWebSocket.Opcode

**Framework**: Network  
**Kind**: enum  
**Role**: Enumeration

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
- [NWProtocolWebSocket.Opcode.binary](./opcode/binary.md)
  A binary data message.
- [NWProtocolWebSocket.Opcode.text](./opcode/text.md)
  A text data message.
- [NWProtocolWebSocket.Opcode.cont](./opcode/cont.md)
  A continuation message.
### Control Types
- [NWProtocolWebSocket.Opcode.ping](./opcode/ping.md)
  A Ping message, which requests a Pong from the peer.
- [NWProtocolWebSocket.Opcode.pong](./opcode/pong.md)
  A Pong message in response to a Ping from the peer.
- [NWProtocolWebSocket.Opcode.close](./opcode/close.md)
  A message indicating a close of the connection.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Sending Messages
- [init(opcode: NWProtocolWebSocket.Opcode)](./metadata/init%28opcode%29.md)
  Initializes a WebSocket message with a specific type code.
- [func setPongHandler(DispatchQueue, handler: (NWError?) -> Void)](./metadata/setponghandler%28_,handler%29.md)
  Sets a handler on a Ping message to be invoked when the corresponding Pong message is received.
- [var closeCode: NWProtocolWebSocket.CloseCode](./metadata/closecode.md)
  The close code on a WebSocket message.
- [NWProtocolWebSocket.CloseCode](./closecode.md)
  Types of codes used upon closing a WebSocket connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolwebsocket/opcode)*