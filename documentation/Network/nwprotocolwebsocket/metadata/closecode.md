# closeCode

**Framework**: Network  
**Kind**: property  
**Role**: Instance Property

The close code on a WebSocket message.

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
var closeCode: NWProtocolWebSocket.CloseCode { get set }
```

## See Also

### Sending Messages
- [init(opcode: NWProtocolWebSocket.Opcode)](./init%28opcode%29.md)
  Initializes a WebSocket message with a specific type code.
- [NWProtocolWebSocket.Opcode](../opcode.md)
  Types of messages that you send and receive on a WebSocket connection.
- [func setPongHandler(DispatchQueue, handler: (NWError?) -> Void)](./setponghandler%28_,handler%29.md)
  Sets a handler on a Ping message to be invoked when the corresponding Pong message is received.
- [NWProtocolWebSocket.CloseCode](../closecode.md)
  Types of codes used upon closing a WebSocket connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolwebsocket/metadata/closecode)*