# NWProtocolQUIC

**Framework**: Network  
**Kind**: class

A network protocol for connections that use the QUIC transport protocol.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
class NWProtocolQUIC
```

## Topics

### Creating QUIC Connections
- [NWProtocolQUIC.Options](nwprotocolquic/options.md)
  A container of options that configure the use of QUIC on a connection.
- [static let definition: NWProtocolDefinition](nwprotocolquic/definition.md)
  The system definition of the QUIC transport protocol.
### Inspecting QUIC State
- [NWProtocolQUIC.Metadata](nwprotocolquic/metadata.md)
  A handle you can use to inspect a connection’s QUIC state.
### Structures
- [NWProtocolQUIC.ApplicationError](nwprotocolquic/applicationerror.md)
  A QUIC application error code.

## Relationships

### Inherits From
- [NWProtocol](nwprotocol.md)
### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [Building a custom peer-to-peer protocol](building-a-custom-peer-to-peer-protocol.md)
  Use networking frameworks to create a custom protocol for playing a game across iOS, iPadOS, watchOS, and tvOS devices.
- [class NWProtocolTCP](nwprotocoltcp.md)
  A network protocol for connections that use the Transmission Control Protocol.
- [class NWProtocolTLS](nwprotocoltls.md)
  A network protocol for connections that use Transport Layer Security.
- [class NWProtocolUDP](nwprotocoludp.md)
  A network protocol for connections that use the User Datagram Protocol.
- [class NWProtocolIP](nwprotocolip.md)
  A network protocol for configuring the Internet Protocol on connections.
- [class NWProtocolWebSocket](nwprotocolwebsocket.md)
  A network protocol for connections that use WebSocket.
- [class NWProtocolFramer](nwprotocolframer.md)
  A customizable network protocol for defining application message parsers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolquic)*