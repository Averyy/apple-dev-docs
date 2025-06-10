# NWProtocolQUIC.Metadata

**Framework**: Network  
**Kind**: class

A handle you can use to inspect a connection’s QUIC state.

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
class Metadata
```

## Topics

### Inspecting Connection State
- [var negotiatedALPN: String?](nwprotocolquic/metadata/negotiatedalpn.md)
  The Application-Layer Protocol Negotiation value used when establishing the connection.
- [var localMaxStreamsBidirectional: Int](nwprotocolquic/metadata/localmaxstreamsbidirectional.md)
  The maximum number of bidirectional streams that the peer can create on a QUIC connection.
- [var localMaxStreamsUnidirectional: Int](nwprotocolquic/metadata/localmaxstreamsunidirectional.md)
  The maximum number of unidirectional streams that the peer can create on a QUIC connection.
- [var remoteMaxStreamsBidirectional: Int](nwprotocolquic/metadata/remotemaxstreamsbidirectional.md)
  The maximum number of bidirectional streams advertised by peer that the connection is allowed to create.
- [var remoteMaxStreamsUnidirectional: Int](nwprotocolquic/metadata/remotemaxstreamsunidirectional.md)
  The maximum number of unidirectional streams advertised by peer that the connection is allowed to create.
- [var remoteIdleTimeout: Int](nwprotocolquic/metadata/remoteidletimeout.md)
  The idle timeout value from the peer’s transport parameters, in milliseconds.
- [var securityProtocolMetadata: sec_protocol_metadata_t](nwprotocolquic/metadata/securityprotocolmetadata.md)
  The result of the QUIC handshake.
### Inspecting Stream State
- [var streamIdentifier: UInt64](nwprotocolquic/metadata/streamidentifier.md)
  The QUIC stream identifier.
- [var usableDatagramFrameSize: Int](nwprotocolquic/metadata/usabledatagramframesize.md)
  The maximum usable size of a datagram frame on a QUIC datagram flow.
### Handling Errors
- [var applicationError: NWProtocolQUIC.ApplicationError](nwprotocolquic/metadata/applicationerror.md)
  The QUIC application error code to send for the connection, or received from the peer.
- [NWProtocolQUIC.ApplicationError](nwprotocolquic/applicationerror.md)
  A QUIC application error code.
- [var streamApplicationErrorCode: UInt64](nwprotocolquic/metadata/streamapplicationerrorcode.md)
  The QUIC application error code to send for the stream, or received from the peer.
### Configuring Keepalives
- [var keepAlive: NWProtocolQUIC.Metadata.KeepAliveBehavior](nwprotocolquic/metadata/keepalive.md)
  The QUIC connection keepalive behavior.
- [NWProtocolQUIC.Metadata.KeepAliveBehavior](nwprotocolquic/metadata/keepalivebehavior.md)
  A QUIC connection keepalive behavior.

## Relationships

### Inherits From
- [NWProtocolMetadata](nwprotocolmetadata.md)
### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolquic/metadata)*