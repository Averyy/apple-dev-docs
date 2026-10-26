# QUIC Options

**Framework**: Network  
**Role**: API Collection

Configure options for connections that use the QUIC transport protocol.

## Topics

### Creating QUIC Connections
- [func nw_protocol_copy_quic_definition() -> nw_protocol_definition_t](./nw_protocol_copy_quic_definition%28%29.md)
  Accesses the system definition of the QUIC transport protocol.
- [func nw_quic_create_options() -> nw_protocol_options_t](./nw_quic_create_options%28%29.md)
  Initializes a default set of QUIC connection options.
- [func nw_protocol_options_is_quic(nw_protocol_options_t) -> Bool](./nw_protocol_options_is_quic%28_%29.md)
  Checks whether an options object uses the QUIC protocol.
### Customizing Connection Options
- [func nw_quic_add_tls_application_protocol(nw_protocol_options_t, UnsafePointer<CChar>)](./nw_quic_add_tls_application_protocol%28_,_%29.md)
  Adds a supported Application-Layer Protocol Negotiation value.
- [func nw_quic_set_idle_timeout(nw_protocol_options_t, UInt32)](./nw_quic_set_idle_timeout%28_,_%29.md)
  Sets the idle timeout for the QUIC connection, in milliseconds.
- [func nw_quic_get_idle_timeout(nw_protocol_options_t) -> UInt32](./nw_quic_get_idle_timeout%28_%29.md)
  Accesses the idle timeout for the QUIC connection, in milliseconds.
- [func nw_quic_set_initial_max_data(nw_protocol_options_t, UInt64)](./nw_quic_set_initial_max_data%28_,_%29.md)
  Sets a QUIC connection’s initial maximum data transport parameter.
- [func nw_quic_get_initial_max_data(nw_protocol_options_t) -> UInt64](./nw_quic_get_initial_max_data%28_%29.md)
  Accesses a QUIC connection’s initial maximum data transport parameter.
- [func nw_quic_set_initial_max_stream_data_bidirectional_local(nw_protocol_options_t, UInt64)](./nw_quic_set_initial_max_stream_data_bidirectional_local%28_,_%29.md)
  Sets a QUIC connection’s initial maximum stream data limit for locally-initiated bidirectional streams.
- [func nw_quic_get_initial_max_stream_data_bidirectional_local(nw_protocol_options_t) -> UInt64](./nw_quic_get_initial_max_stream_data_bidirectional_local%28_%29.md)
  Accesses a QUIC connection’s initial maximum stream data limit for locally-initiated bidirectional streams.
- [func nw_quic_set_initial_max_stream_data_bidirectional_remote(nw_protocol_options_t, UInt64)](./nw_quic_set_initial_max_stream_data_bidirectional_remote%28_,_%29.md)
  Sets a QUIC connection’s initial maximum stream data limit for remote-initiated bidirectional streams.
- [func nw_quic_get_initial_max_stream_data_bidirectional_remote(nw_protocol_options_t) -> UInt64](./nw_quic_get_initial_max_stream_data_bidirectional_remote%28_%29.md)
  Accesses a QUIC connection’s initial maximum stream data limit for remote-initiated bidirectional streams.
- [func nw_quic_set_initial_max_stream_data_unidirectional(nw_protocol_options_t, UInt64)](./nw_quic_set_initial_max_stream_data_unidirectional%28_,_%29.md)
  Sets a QUIC connection’s initial maximum stream data limit for unidirectional streams.
- [func nw_quic_get_initial_max_stream_data_unidirectional(nw_protocol_options_t) -> UInt64](./nw_quic_get_initial_max_stream_data_unidirectional%28_%29.md)
  Accesses a QUIC connection’s initial maximum stream data limit for unidirectional streams.
- [func nw_quic_set_initial_max_streams_bidirectional(nw_protocol_options_t, UInt64)](./nw_quic_set_initial_max_streams_bidirectional%28_,_%29.md)
  Sets a QUIC connection’s initial maximum number of bidirectional streams.
- [func nw_quic_get_initial_max_streams_bidirectional(nw_protocol_options_t) -> UInt64](./nw_quic_get_initial_max_streams_bidirectional%28_%29.md)
  Accesses a QUIC connection’s initial maximum number of bidirectional streams.
- [func nw_quic_set_initial_max_streams_unidirectional(nw_protocol_options_t, UInt64)](./nw_quic_set_initial_max_streams_unidirectional%28_,_%29.md)
  Sets a QUIC connection’s initial maximum number of unidirectional streams.
- [func nw_quic_get_initial_max_streams_unidirectional(nw_protocol_options_t) -> UInt64](./nw_quic_get_initial_max_streams_unidirectional%28_%29.md)
  Accesses a QUIC connection’s initial maximum number of unidirectional streams.
- [func nw_quic_set_max_datagram_frame_size(nw_protocol_options_t, UInt16)](./nw_quic_set_max_datagram_frame_size%28_,_%29.md)
  Sets a QUIC connection’s maximum DATAGRAM frame size.
- [func nw_quic_get_max_datagram_frame_size(nw_protocol_options_t) -> UInt16](./nw_quic_get_max_datagram_frame_size%28_%29.md)
  Accesses a QUIC connection’s maximum DATAGRAM frame size.
- [func nw_quic_set_max_udp_payload_size(nw_protocol_options_t, UInt16)](./nw_quic_set_max_udp_payload_size%28_,_%29.md)
  Sets the maximum length of a QUIC packet that can be received on a connection, in bytes.
- [func nw_quic_get_max_udp_payload_size(nw_protocol_options_t) -> UInt16](./nw_quic_get_max_udp_payload_size%28_%29.md)
  Accesses the maximum length of a QUIC packet that can be received on a connection, in bytes.
- [func nw_quic_copy_sec_protocol_options(nw_protocol_options_t) -> sec_protocol_options_t](./nw_quic_copy_sec_protocol_options%28_%29.md)
  Accesses the handshake security options QUIC will use.
### Customizing Stream Options
- [func nw_quic_set_stream_is_unidirectional(nw_protocol_options_t, Bool)](./nw_quic_set_stream_is_unidirectional%28_,_%29.md)
  Configures a QUIC stream as unidirectional, instead of bidirectional.
- [func nw_quic_get_stream_is_unidirectional(nw_protocol_options_t) -> Bool](./nw_quic_get_stream_is_unidirectional%28_%29.md)
  Checks if a QUIC stream is unidirectional, instead of bidirectional.
- [func nw_quic_set_stream_is_datagram(nw_protocol_options_t, Bool)](./nw_quic_set_stream_is_datagram%28_,_%29.md)
  Configures a QUIC stream as a datagram flow, instead of a byte stream.
- [func nw_quic_get_stream_is_datagram(nw_protocol_options_t) -> Bool](./nw_quic_get_stream_is_datagram%28_%29.md)
  Checks if a QUIC stream is a datagram flow, instead of a byte stream.
### Inspecting Connection State
- [func nw_protocol_metadata_is_quic(nw_protocol_metadata_t) -> Bool](./nw_protocol_metadata_is_quic%28_%29.md)
  Checks whether a metadata object contains QUIC connection state.
- [func nw_quic_set_local_max_streams_bidirectional(nw_protocol_metadata_t, UInt64)](./nw_quic_set_local_max_streams_bidirectional%28_,_%29.md)
  Sets the maximum number of bidirectional streams that the peer can create on a QUIC connection.
- [func nw_quic_get_local_max_streams_bidirectional(nw_protocol_metadata_t) -> UInt64](./nw_quic_get_local_max_streams_bidirectional%28_%29.md)
  Accesses the maximum number of bidirectional streams that the peer can create on a QUIC connection.
- [func nw_quic_set_local_max_streams_unidirectional(nw_protocol_metadata_t, UInt64)](./nw_quic_set_local_max_streams_unidirectional%28_,_%29.md)
  Sets the maximum number of unidirectional streams that the peer can create on a QUIC connection.
- [func nw_quic_get_local_max_streams_unidirectional(nw_protocol_metadata_t) -> UInt64](./nw_quic_get_local_max_streams_unidirectional%28_%29.md)
  Accesses the maximum number of unidirectional streams that the peer can create on a QUIC connection.
- [func nw_quic_get_remote_max_streams_bidirectional(nw_protocol_metadata_t) -> UInt64](./nw_quic_get_remote_max_streams_bidirectional%28_%29.md)
  Accesses the maximum number of bidirectional streams advertised by peer that the connection is allowed to create.
- [func nw_quic_get_remote_max_streams_unidirectional(nw_protocol_metadata_t) -> UInt64](./nw_quic_get_remote_max_streams_unidirectional%28_%29.md)
  Accesses the maximum number of unidirectional streams advertised by peer that the connection is allowed to create.
- [func nw_quic_get_remote_idle_timeout(nw_protocol_metadata_t) -> UInt64](./nw_quic_get_remote_idle_timeout%28_%29.md)
  Accesses the idle timeout value from the peer’s transport parameters, in milliseconds.
- [func nw_quic_copy_sec_protocol_metadata(nw_protocol_metadata_t) -> sec_protocol_metadata_t](./nw_quic_copy_sec_protocol_metadata%28_%29.md)
  Accesses the result of the QUIC handshake.
### Inspecting Stream State
- [func nw_quic_get_stream_id(nw_protocol_metadata_t) -> UInt64](./nw_quic_get_stream_id%28_%29.md)
  Accesses the QUIC stream identifier.
- [func nw_quic_get_stream_type(nw_protocol_metadata_t) -> UInt8](./nw_quic_get_stream_type%28_%29.md)
  Accesses the stream type of the QUIC stream.
- [func nw_quic_get_stream_usable_datagram_frame_size(nw_protocol_metadata_t) -> UInt16](./nw_quic_get_stream_usable_datagram_frame_size%28_%29.md)
  Accesses the maximum usable size of a datagram frame on a QUIC datagram flow.
### Handling Errors
- [func nw_quic_set_application_error(nw_protocol_metadata_t, UInt64, UnsafePointer<CChar>?)](./nw_quic_set_application_error%28_,_,_%29.md)
  Sets the QUIC application error code to send for the connection.
- [func nw_quic_get_application_error(nw_protocol_metadata_t) -> UInt64](./nw_quic_get_application_error%28_%29.md)
  Accesses the QUIC application error code received from the peer.
- [func nw_quic_get_application_error_reason(nw_protocol_metadata_t) -> UnsafePointer<CChar>?](./nw_quic_get_application_error_reason%28_%29.md)
  Accesses the QUIC application error reason received from the peer.
- [func nw_quic_set_stream_application_error(nw_protocol_metadata_t, UInt64)](./nw_quic_set_stream_application_error%28_,_%29.md)
  Sets the QUIC application error code to send for the stream.
- [func nw_quic_get_stream_application_error(nw_protocol_metadata_t) -> UInt64](./nw_quic_get_stream_application_error%28_%29.md)
  Accesses the QUIC application error code received from the peer for the stream.
### Configuring Keepalives
- [func nw_quic_set_keepalive_interval(nw_protocol_metadata_t, UInt16)](./nw_quic_set_keepalive_interval%28_,_%29.md)
  Sets the keepalive interval for the QUIC connection, in seconds.
- [func nw_quic_get_keepalive_interval(nw_protocol_metadata_t) -> UInt16](./nw_quic_get_keepalive_interval%28_%29.md)
  Accesses the keepalive interval for the QUIC connection, in seconds.

## See Also

### Network Protocols
- [TCP Options](./tcp-options.md)
  Configure options for connections that use the Transmission Control Protocol.
- [TLS Options](./tls-options.md)
  Configure options for connections that use Transport Layer Security.
- [UDP Options](./udp-options.md)
  Configure options for connections that use the User Datagram Protocol.
- [IP Options](./ip-options.md)
  Configure Internet Protocol options on connections.
- [WebSocket Options](./websocket-options.md)
  Configure options for connections that use WebSocket.
- [Framer Protocol Options](./framer-protocol-options.md)
  Create custom protocols to frame applications messages over a connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/quic-options)*