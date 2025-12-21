# NWProtocolWebSocket

**Framework**: Network  
**Kind**: class

A network protocol for connections that use WebSocket.

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
class NWProtocolWebSocket
```

## Topics

### Creating WebSocket Connections
- [NWProtocolWebSocket.Options](nwprotocolwebsocket/options.md)
  A container of options for configuring how WebSocket is used on a connection.
- [static let definition: NWProtocolDefinition](nwprotocolwebsocket/definition.md)
  The system definition of the WebSocket protocol.
### Handling WebSocket Messages
- [NWProtocolWebSocket.Metadata](nwprotocolwebsocket/metadata.md)
  A WebSocket message you configure when sending and receiving packets.
### Structures
- [NWProtocolWebSocket.Response](nwprotocolwebsocket/response.md)
  A WebSocket handshake reponse sent from a server to a client.
### Enumerations
- [NWProtocolWebSocket.CloseCode](nwprotocolwebsocket/closecode.md)
  Types of codes used upon closing a WebSocket connection.
- [NWProtocolWebSocket.Opcode](nwprotocolwebsocket/opcode.md)
  Types of messages that you send and receive on a WebSocket connection.
- [NWProtocolWebSocket.Version](nwprotocolwebsocket/version.md)
  Supported versions of the WebSocket protocol.

## Relationships

### Inherits From
- [NWProtocol](nwprotocol.md)
### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Building a custom peer-to-peer protocol](building-a-custom-peer-to-peer-protocol.md)
  Use networking frameworks to create a custom protocol for playing a game across iOS, iPadOS, watchOS, and tvOS devices.
- [Connecting iPadOS and visionOS apps over the local network](../visionOS/connecting-ipados-and-visionos-apps-over-the-local-network.md)
  Build an iPadOS companion app to control your visionOS app.
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
- [class NWProtocolFramer](nwprotocolframer.md)
  A customizable network protocol for defining application message parsers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolwebsocket)*