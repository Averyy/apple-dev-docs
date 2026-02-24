# NWProtocolFramer

**Framework**: Network  
**Kind**: class

A customizable network protocol for defining application message parsers.

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
class NWProtocolFramer
```

## Topics

### Implementing Framer Protocols
- [protocol NWProtocolFramerImplementation](nwprotocolframerimplementation.md)
  A protocol to which your classes can conform in order to implement a custom framing protocol.
- [NWProtocolFramer.Instance](nwprotocolframer/instance.md)
  An object that represents a single instance of your custom protocol running in a connection.
### Using Framers with Connections
- [NWProtocolFramer.Definition](nwprotocolframer/definition.md)
  A custom protocol definition you use to associate messages with protocol options.
- [NWProtocolFramer.Options](nwprotocolframer/options.md)
  A container you use to add your custom protocol to a connection’s protocol stack.
- [NWProtocolFramer.Message](nwprotocolframer/message.md)
  A message for a custom protocol, in which you can store arbitrary key-value pairs.
### Enumerations
- [NWProtocolFramer.StartResult](nwprotocolframer/startresult.md)
  Results that you send to indicate the disposition of your protocol after receiving the call to start.

## Relationships

### Inherits From
- [NWProtocol](nwprotocol.md)
### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Building a custom peer-to-peer protocol](building-a-custom-peer-to-peer-protocol.md)
  Use networking frameworks to create a custom protocol for playing a game across iOS, iPadOS, watchOS, and tvOS devices.
- [class NWProtocolTCP](nwprotocoltcp.md)
  A network protocol for connections that use the Transmission Control Protocol.
- [class NWProtocolTLS](nwprotocoltls.md)
  A network protocol for connections that use Transport Layer Security.
- [class NWProtocolQUIC](nwprotocolquic.md)
  A network protocol for connections that use the QUIC transport protocol.
- [class NWProtocolUDP](nwprotocoludp.md)
  A network protocol for connections that use the User Datagram Protocol.
- [class NWProtocolIP](nwprotocolip.md)
  A network protocol for configuring the Internet Protocol on connections.
- [class NWProtocolWebSocket](nwprotocolwebsocket.md)
  A network protocol for connections that use WebSocket.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolframer)*