# QUIC

**Framework**: Network  
**Kind**: struct

The system definition of the QUIC protocol.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct QUIC
```

#### Overview

Conforms to MultiplexProtocol, exposing configuration for a multiplexing instance of QUIC, which in turn exposes the ability to handle multiple streams of data over QUIC.

## Topics

### Classes
- [class Datagrams](quic/datagrams.md)
- [class Stream](quic/stream.md)
### Structures
- [struct TLS](quic/tls-swift.struct.md)
  The set of TLS options available when using QUIC.
### Initializers
- [init(alpn: [String])](quic/init(alpn:).md)
  Create a QUIC protocol for use in a protocol stack.
- [init(alpn: [String], () -> UDP)](quic/init(alpn:_:).md)
### Instance Properties
- [var tls: QUIC.TLS](quic/tls-swift.property.md)
  Configure TLS when used within QUIC.
### Instance Methods
- [func idleTimeout(Int) -> QUIC](quic/idletimeout(_:).md)
  Set the idle timeout for the QUIC connection, in milliseconds.
- [func initialMaxBidirectionalStreams(Int) -> QUIC](quic/initialmaxbidirectionalstreams(_:).md)
  Set the initial_max_streams_bidi transport parameter on a QUIC connection.
- [func initialMaxData(Int) -> QUIC](quic/initialmaxdata(_:).md)
  Set the initial_max_data transport parameter on a QUIC connection.
- [func initialMaxStreamDataBidirectionalLocal(Int) -> QUIC](quic/initialmaxstreamdatabidirectionallocal(_:).md)
  Set the initial_max_stream_data_bidi_local transport parameter on a QUIC connection.
- [func initialMaxStreamDataBidirectionalRemote(Int) -> QUIC](quic/initialmaxstreamdatabidirectionalremote(_:).md)
  Set the initial_max_stream_data_bidi_remote transport parameter on a QUIC connection.
- [func initialMaxStreamDataUnidirectional(Int) -> QUIC](quic/initialmaxstreamdataunidirectional(_:).md)
  Set the initial_max_stream_data_uni transport parameter on a QUIC connection.
- [func initialMaxUnidirectionalStreams(Int) -> QUIC](quic/initialmaxunidirectionalstreams(_:).md)
  Set the initial_max_stream_data_uni transport parameter on a QUIC connection.
- [func maxDatagramFrameSize(Int) -> QUIC](quic/maxdatagramframesize(_:).md)
  Set the max_datagram_frame_size transport parameter on a QUIC connection.
- [func maxUDPPayloadSize(Int) -> QUIC](quic/maxudppayloadsize(_:).md)
  Set the maximum length of a QUIC packet that you are willing to receive on a connection, in bytes.

## Relationships

### Conforms To
- [MultiplexProtocol](multiplexprotocol.md)
- [NetworkProtocolOptions](networkprotocoloptions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/quic)*