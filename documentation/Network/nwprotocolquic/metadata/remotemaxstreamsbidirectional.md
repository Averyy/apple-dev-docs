# remoteMaxStreamsBidirectional

**Framework**: Network  
**Kind**: property

The maximum number of bidirectional streams advertised by peer that the connection is allowed to create.

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
var remoteMaxStreamsBidirectional: Int { get }
```

## See Also

- [var negotiatedALPN: String?](nwprotocolquic/metadata/negotiatedalpn.md)
  The Application-Layer Protocol Negotiation value used when establishing the connection.
- [var localMaxStreamsBidirectional: Int](nwprotocolquic/metadata/localmaxstreamsbidirectional.md)
  The maximum number of bidirectional streams that the peer can create on a QUIC connection.
- [var localMaxStreamsUnidirectional: Int](nwprotocolquic/metadata/localmaxstreamsunidirectional.md)
  The maximum number of unidirectional streams that the peer can create on a QUIC connection.
- [var remoteMaxStreamsUnidirectional: Int](nwprotocolquic/metadata/remotemaxstreamsunidirectional.md)
  The maximum number of unidirectional streams advertised by peer that the connection is allowed to create.
- [var remoteIdleTimeout: Int](nwprotocolquic/metadata/remoteidletimeout.md)
  The idle timeout value from the peer’s transport parameters, in milliseconds.
- [var securityProtocolMetadata: sec_protocol_metadata_t](nwprotocolquic/metadata/securityprotocolmetadata.md)
  The result of the QUIC handshake.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolquic/metadata/remotemaxstreamsbidirectional)*