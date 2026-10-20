# NWProtocolQUIC.Options

**Framework**: Network  
**Kind**: class  
**Role**: Class

A container of options that configure the use of QUIC on a connection.

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
class Options
```

## Topics

### Customizing Connection Options
- [convenience init(alpn: [String])](./options/init%28alpn%29.md)
  Initializes a default set of QUIC options along with a set of supported Application-Layer Protocol Negotiation values.
- [init()](./options/init%28%29.md)
  Initializes a default set of QUIC options, without specifying a set of supported Application-Layer Protocol Negotiation values.
- [var alpn: [String]](./options/alpn.md)
  A set of supported Application-Layer Protocol Negotiation values.
- [var idleTimeout: Int](./options/idletimeout.md)
  The idle timeout for the QUIC connection, in milliseconds.
- [var initialMaxData: Int](./options/initialmaxdata.md)
  A QUIC connection’s initial maximum data transport parameter.
- [var initialMaxStreamDataBidirectionalLocal: Int](./options/initialmaxstreamdatabidirectionallocal.md)
  A QUIC connection’s initial maximum stream data limit for locally-initiated bidirectional streams.
- [var initialMaxStreamDataBidirectionalRemote: Int](./options/initialmaxstreamdatabidirectionalremote.md)
  A QUIC connection’s initial maximum stream data limit for remote-initiated bidirectional streams.
- [var initialMaxStreamDataUnidirectional: Int](./options/initialmaxstreamdataunidirectional.md)
  A QUIC connection’s initial maximum stream data limit for unidirectional streams.
- [var initialMaxStreamsBidirectional: Int](./options/initialmaxstreamsbidirectional.md)
  A QUIC connection’s initial maximum number of bidirectional streams.
- [var initialMaxStreamsUnidirectional: Int](./options/initialmaxstreamsunidirectional.md)
  A QUIC connection’s initial maximum number of unidirectional streams.
- [var maxDatagramFrameSize: Int](./options/maxdatagramframesize.md)
  A QUIC connection’s maximum DATAGRAM frame size.
- [var maxUDPPayloadSize: Int](./options/maxudppayloadsize.md)
  The maximum length of a QUIC packet that can be received on a connection, in bytes.
- [var securityProtocolOptions: sec_protocol_options_t](./options/securityprotocoloptions.md)
  The handshake security options QUIC uses.
### Customizing Stream Options
- [var direction: NWProtocolQUIC.Options.Direction](./options/direction-swift.property.md)
  The direction of the QUIC stream.
- [NWProtocolQUIC.Options.Direction](./options/direction-swift.enum.md)
  A directionality of a QUIC stream.
- [var isDatagram: Bool](./options/isdatagram.md)
  A Boolean that indicates that this is a QUIC datagram flow, not a stream of bytes.

## Relationships

### Inherits From
- [NWProtocolOptions](../nwprotocoloptions.md)
### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating QUIC Connections
- [static let definition: NWProtocolDefinition](./definition.md)
  The system definition of the QUIC transport protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolquic/options)*