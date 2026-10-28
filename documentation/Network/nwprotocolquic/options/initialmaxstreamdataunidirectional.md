# initialMaxStreamDataUnidirectional

**Framework**: Network  
**Kind**: property  
**Role**: Instance Property

A QUIC connection’s initial maximum stream data limit for unidirectional streams.

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
var initialMaxStreamDataUnidirectional: Int { get set }
```

## Discussion

This property determines the value of the `initial_max_stream_data_uni` transport parameter.

## See Also

### Customizing Connection Options
- [convenience init(alpn: [String])](./init%28alpn%29.md)
  Initializes a default set of QUIC options along with a set of supported Application-Layer Protocol Negotiation values.
- [init()](./init%28%29.md)
  Initializes a default set of QUIC options, without specifying a set of supported Application-Layer Protocol Negotiation values.
- [var alpn: [String]](./alpn.md)
  A set of supported Application-Layer Protocol Negotiation values.
- [var idleTimeout: Int](./idletimeout.md)
  The idle timeout for the QUIC connection, in milliseconds.
- [var initialMaxData: Int](./initialmaxdata.md)
  A QUIC connection’s initial maximum data transport parameter.
- [var initialMaxStreamDataBidirectionalLocal: Int](./initialmaxstreamdatabidirectionallocal.md)
  A QUIC connection’s initial maximum stream data limit for locally-initiated bidirectional streams.
- [var initialMaxStreamDataBidirectionalRemote: Int](./initialmaxstreamdatabidirectionalremote.md)
  A QUIC connection’s initial maximum stream data limit for remote-initiated bidirectional streams.
- [var initialMaxStreamsBidirectional: Int](./initialmaxstreamsbidirectional.md)
  A QUIC connection’s initial maximum number of bidirectional streams.
- [var initialMaxStreamsUnidirectional: Int](./initialmaxstreamsunidirectional.md)
  A QUIC connection’s initial maximum number of unidirectional streams.
- [var maxDatagramFrameSize: Int](./maxdatagramframesize.md)
  A QUIC connection’s maximum DATAGRAM frame size.
- [var maxUDPPayloadSize: Int](./maxudppayloadsize.md)
  The maximum length of a QUIC packet that can be received on a connection, in bytes.
- [var securityProtocolOptions: sec_protocol_options_t](./securityprotocoloptions.md)
  The handshake security options QUIC uses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolquic/options/initialmaxstreamdataunidirectional)*