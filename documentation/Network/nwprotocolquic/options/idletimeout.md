# idleTimeout

**Framework**: Network  
**Kind**: property

The idle timeout for the QUIC connection, in milliseconds.

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
var idleTimeout: Int { get set }
```

## See Also

- [convenience init(alpn: [String])](nwprotocolquic/options/init(alpn:).md)
  Initializes a default set of QUIC options along with a set of supported Application-Layer Protocol Negotiation values.
- [init()](nwprotocolquic/options/init.md)
  Initializes a default set of QUIC options, without specifying a set of supported Application-Layer Protocol Negotiation values.
- [var alpn: [String]](nwprotocolquic/options/alpn.md)
  A set of supported Application-Layer Protocol Negotiation values.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolquic/options/idletimeout)*