# NWProtocolWebSocket.CloseCode

**Framework**: Network  
**Kind**: enum

Types of codes used upon closing a WebSocket connection.

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
enum CloseCode
```

## Topics

### Close Code Types
- [init(rawValue: UInt16) throws](nwprotocolwebsocket/closecode/init(rawvalue:).md)
  Initializes a close code with a raw value.
- [case protocolCode(NWProtocolWebSocket.CloseCode.Defined)](nwprotocolwebsocket/closecode/protocolcode(_:).md)
  A well-known close code reserved by the protocol (values 1000-2999).
- [NWProtocolWebSocket.CloseCode.Defined](nwprotocolwebsocket/closecode/defined.md)
  Well-known close code values.
- [NWProtocolWebSocket.CloseCode.applicationCode(_:)](nwprotocolwebsocket/closecode/applicationcode(_:).md)
  A close code in the range reserved for applications and frameworks (3000-3999).
- [NWProtocolWebSocket.CloseCode.privateCode(_:)](nwprotocolwebsocket/closecode/privatecode(_:).md)
  A close code in the private-use range (4000-4999).

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [init(opcode: NWProtocolWebSocket.Opcode)](nwprotocolwebsocket/metadata/init(opcode:).md)
  Initializes a WebSocket message with a specific type code.
- [NWProtocolWebSocket.Opcode](nwprotocolwebsocket/opcode.md)
  Types of messages that you send and receive on a WebSocket connection.
- [func setPongHandler(DispatchQueue, handler: (NWError?) -> Void)](nwprotocolwebsocket/metadata/setponghandler(_:handler:).md)
  Sets a handler on a Ping message to be invoked when the corresponding Pong message is received.
- [var closeCode: NWProtocolWebSocket.CloseCode](nwprotocolwebsocket/metadata/closecode.md)
  The close code on a WebSocket message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolwebsocket/closecode)*