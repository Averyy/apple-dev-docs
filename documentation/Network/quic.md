# QUIC

**Framework**: Network  
**Kind**: struct

The QUIC type can be used to insert QUIC into a protocol stack. As it conforms to MultiplexProtocol, it exposes configuration a multiplexing instance of QUIC to be used with NetworkConnection, which will in turn expose the ability to handle multiple streams of data over QUIC.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
struct QUIC
```

## Topics

### Structures
- [struct TLS](quic/tls-swift.struct.md)
### Initializers
- [init(alpn: [String])](quic/init(alpn:).md)
- [init(alpn: [String], () -> UDP)](quic/init(alpn:_:).md)
### Instance Properties
- [let belowProtocol: UDP](quic/belowprotocol.md)
- [var tls: QUIC.TLS](quic/tls-swift.property.md)
### Instance Methods
- [func idleTimeout(Int) -> QUIC](quic/idletimeout(_:).md)
  An idle timeout for the QUIC connection, in milliseconds.
- [func initialMaxBidirectionalStreams(Int) -> QUIC](quic/initialmaxbidirectionalstreams(_:).md)
  Set the `initial_max_streams_bidi` transport parameter on a QUIC connection.
- [func initialMaxData(Int) -> QUIC](quic/initialmaxdata(_:).md)
  Set the `initial_max_data` transport parameter on a QUIC connection.
- [func initialMaxStreamDataBidirectionalLocal(Int) -> QUIC](quic/initialmaxstreamdatabidirectionallocal(_:).md)
  Set the `initial_max_stream_data_bidi_local` transport parameter on a QUIC connection.
- [func initialMaxStreamDataBidirectionalRemote(Int) -> QUIC](quic/initialmaxstreamdatabidirectionalremote(_:).md)
  Set the `initial_max_stream_data_bidi_remote` transport parameter on a QUIC connection.
- [func initialMaxStreamDataUnidirectional(Int) -> QUIC](quic/initialmaxstreamdataunidirectional(_:).md)
  Set the `initial_max_stream_data_uni` transport parameter on a QUIC connection.
- [func initialMaxUnidirectionalStreams(Int) -> QUIC](quic/initialmaxunidirectionalstreams(_:).md)
  Set the `initial_max_streams_uni` transport parameter on a QUIC connection.
- [func maxDatagramFrameSize(Int) -> QUIC](quic/maxdatagramframesize(_:).md)
  Set the `max_datagram_frame_size` transport parameter on a QUIC connection.
- [func maxUDPPayloadSize(Int) -> QUIC](quic/maxudppayloadsize(_:).md)
  Define the maximum length of a QUIC packet (UDP payload) that the client is willing to receive on a connection, in bytes.

## Relationships

### Conforms To
- [MultiplexProtocol](multiplexprotocol.md)
- [NetworkProtocolOptions](networkprotocoloptions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/quic)*