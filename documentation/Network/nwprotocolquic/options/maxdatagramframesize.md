# maxDatagramFrameSize

**Framework**: Network  
**Kind**: property

A QUIC connection’s maximum DATAGRAM frame size.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var maxDatagramFrameSize: Int { get set }
```

#### Discussion

This property determines the value of the `max_datagram_frame_size` transport parameter.

## See Also

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
- [var maxUDPPayloadSize: Int](nwprotocolquic/options/maxudppayloadsize.md)
  The maximum length of a QUIC packet that can be received on a connection, in bytes.
- [var securityProtocolOptions: sec_protocol_options_t](nwprotocolquic/options/securityprotocoloptions.md)
  The handshake security options QUIC uses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolquic/options/maxdatagramframesize)*