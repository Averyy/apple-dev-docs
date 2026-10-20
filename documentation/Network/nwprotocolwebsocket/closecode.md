# NWProtocolWebSocket.CloseCode

**Framework**: Network  
**Kind**: enum  
**Role**: Enumeration

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
- [init(rawValue: UInt16) throws](./closecode/init%28rawvalue%29.md)
  Initializes a close code with a raw value.
- [case protocolCode(NWProtocolWebSocket.CloseCode.Defined)](./closecode/protocolcode%28_%29.md)
  A well-known close code reserved by the protocol (values 1000-2999).
- [NWProtocolWebSocket.CloseCode.Defined](./closecode/defined.md)
  Well-known close code values.
- [NWProtocolWebSocket.CloseCode.applicationCode(_:)](./closecode/applicationcode%28_%29.md)
  A close code in the range reserved for applications and frameworks (3000-3999).
- [NWProtocolWebSocket.CloseCode.privateCode(_:)](./closecode/privatecode%28_%29.md)
  A close code in the private-use range (4000-4999).

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Sending Messages
- [init(opcode: NWProtocolWebSocket.Opcode)](./metadata/init%28opcode%29.md)
  Initializes a WebSocket message with a specific type code.
- [NWProtocolWebSocket.Opcode](./opcode.md)
  Types of messages that you send and receive on a WebSocket connection.
- [func setPongHandler(DispatchQueue, handler: (NWError?) -> Void)](./metadata/setponghandler%28_,handler%29.md)
  Sets a handler on a Ping message to be invoked when the corresponding Pong message is received.
- [var closeCode: NWProtocolWebSocket.CloseCode](./metadata/closecode.md)
  The close code on a WebSocket message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolwebsocket/closecode)*