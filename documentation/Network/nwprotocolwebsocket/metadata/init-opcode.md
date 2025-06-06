# init(opcode:)

**Framework**: Network  
**Kind**: init

Initializes a WebSocket message with a specific type code.

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
init(opcode: NWProtocolWebSocket.Opcode)
```

## See Also

- [NWProtocolWebSocket.Opcode](nwprotocolwebsocket/opcode.md)
  Types of messages that you send and receive on a WebSocket connection.
- [func setPongHandler(DispatchQueue, handler: (NWError?) -> Void)](nwprotocolwebsocket/metadata/setponghandler(_:handler:).md)
  Sets a handler on a Ping message to be invoked when the corresponding Pong message is received.
- [var closeCode: NWProtocolWebSocket.CloseCode](nwprotocolwebsocket/metadata/closecode.md)
  The close code on a WebSocket message.
- [NWProtocolWebSocket.CloseCode](nwprotocolwebsocket/closecode.md)
  Types of codes used upon closing a WebSocket connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolwebsocket/metadata/init(opcode:))*