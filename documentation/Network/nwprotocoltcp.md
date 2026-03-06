# NWProtocolTCP

**Framework**: Network  
**Kind**: class

A network protocol for connections that use the Transmission Control Protocol.

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
class NWProtocolTCP
```

## Topics

### Creating TCP Connections
- [NWProtocolTCP.Options](nwprotocoltcp/options.md)
  A container of options for configuring how TCP is used on a connection.
- [static let definition: NWProtocolDefinition](nwprotocoltcp/definition.md)
  The system definition of the Transport Control Protocol.
### Inspecting TCP State
- [NWProtocolTCP.Metadata](nwprotocoltcp/metadata.md)
  A handle you can use to inspect a connection’s TCP state.

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
- [class NWProtocolFramer](nwprotocolframer.md)
  A customizable network protocol for defining application message parsers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocoltcp)*