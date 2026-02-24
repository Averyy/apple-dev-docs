# NWProtocolUDP

**Framework**: Network  
**Kind**: class

A network protocol for connections that use the User Datagram Protocol.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 12.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
class NWProtocolUDP
```

## Topics

### Creating UDP Connections
- [NWProtocolUDP.Options](nwprotocoludp/options.md)
  A container of options for configuring how UDP is used on a connection.
- [static let definition: NWProtocolDefinition](nwprotocoludp/definition.md)
  The system definition of the User Datagram Protocol.
### Sending UDP Messages
- [NWProtocolUDP.Metadata](nwprotocoludp/metadata.md)
  A container representing UDP when sending and receiving packets.

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
- [class NWProtocolIP](nwprotocolip.md)
  A network protocol for configuring the Internet Protocol on connections.
- [class NWProtocolWebSocket](nwprotocolwebsocket.md)
  A network protocol for connections that use WebSocket.
- [class NWProtocolFramer](nwprotocolframer.md)
  A customizable network protocol for defining application message parsers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocoludp)*