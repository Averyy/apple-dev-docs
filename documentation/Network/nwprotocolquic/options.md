# NWProtocolQUIC.Options

**Framework**: Network  
**Kind**: class

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
- [convenience init(alpn: [String])](nwprotocolquic/options/init(alpn:).md)
  Initializes a default set of QUIC options along with a set of supported Application-Layer Protocol Negotiation values.
- [init()](nwprotocolquic/options/init.md)
  Initializes a default set of QUIC options, without specifying a set of supported Application-Layer Protocol Negotiation values.
- [var alpn: [String]](nwprotocolquic/options/alpn.md)
  A set of supported Application-Layer Protocol Negotiation values.
- [var idleTimeout: Int](nwprotocolquic/options/idletimeout.md)
  The idle timeout for the QUIC connection, in milliseconds.
- [var initialMaxData: Int](nwprotocolquic/options/initialmaxdata.md)
  A QUIC connection’s initial maximum data transport parameter.
- [var initialMaxStreamDataBidirectionalLocal: Int](nwprotocolquic/options/initialmaxstreamdatabidirectionallocal.md)
  A QUIC connection’s initial maximum stream data limit for locally-initiated bidirectional streams.
- [var initialMaxStreamDataBidirectionalRemote: Int](nwprotocolquic/options/initialmaxstreamdatabidirectionalremote.md)
  A QUIC connection’s initial maximum stream data limit for remote-initiated bidirectional streams.
- [var initialMaxStreamDataUnidirectional: Int](nwprotocolquic/options/initialmaxstreamdataunidirectional.md)
  A QUIC connection’s initial maximum stream data limit for unidirectional streams.
- [var initialMaxStreamsBidirectional: Int](nwprotocolquic/options/initialmaxstreamsbidirectional.md)
  A QUIC connection’s initial maximum number of bidirectional streams.
- [var initialMaxStreamsUnidirectional: Int](nwprotocolquic/options/initialmaxstreamsunidirectional.md)
  A QUIC connection’s initial maximum number of unidirectional streams.
- [var maxDatagramFrameSize: Int](nwprotocolquic/options/maxdatagramframesize.md)
  A QUIC connection’s maximum DATAGRAM frame size.
- [var maxUDPPayloadSize: Int](nwprotocolquic/options/maxudppayloadsize.md)
  The maximum length of a QUIC packet that can be received on a connection, in bytes.
- [var securityProtocolOptions: sec_protocol_options_t](nwprotocolquic/options/securityprotocoloptions.md)
  The handshake security options QUIC uses.
### Customizing Stream Options
- [var direction: NWProtocolQUIC.Options.Direction](nwprotocolquic/options/direction-swift.property.md)
  The direction of the QUIC stream.
- [NWProtocolQUIC.Options.Direction](nwprotocolquic/options/direction-swift.enum.md)
  A directionality of a QUIC stream.
- [var isDatagram: Bool](nwprotocolquic/options/isdatagram.md)
  A Boolean that indicates that this is a QUIC datagram flow, not a stream of bytes.

## Relationships

### Inherits From
- [NWProtocolOptions](nwprotocoloptions.md)
### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [static let definition: NWProtocolDefinition](nwprotocolquic/definition.md)
  The system definition of the QUIC transport protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolquic/options)*