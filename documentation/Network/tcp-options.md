# TCP Options

**Framework**: Network  
**Role**: API Collection

Configure options for connections that use the Transmission Control Protocol.

## Topics

### Creating TCP Connections
- [func nw_protocol_copy_tcp_definition() -> nw_protocol_definition_t](./nw_protocol_copy_tcp_definition%28%29.md)
  Accesses the system definition of the Transport Control Protocol.
- [func nw_tcp_create_options() -> nw_protocol_options_t](./nw_tcp_create_options%28%29.md)
  Initializes a default set of TCP connection options.
### Customizing TCP Options
- [func nw_tcp_options_set_enable_fast_open(nw_protocol_options_t, Bool)](./nw_tcp_options_set_enable_fast_open%28_,_%29.md)
  Enables TCP Fast Open on a connection.
- [func nw_tcp_options_set_maximum_segment_size(nw_protocol_options_t, UInt32)](./nw_tcp_options_set_maximum_segment_size%28_,_%29.md)
  Sets TCP’s maximum segment size in bytes.
- [func nw_tcp_options_set_no_delay(nw_protocol_options_t, Bool)](./nw_tcp_options_set_no_delay%28_,_%29.md)
  Disables Nagle’s algorithm for TCP.
- [func nw_tcp_options_set_no_options(nw_protocol_options_t, Bool)](./nw_tcp_options_set_no_options%28_,_%29.md)
  Sets TCP into no-options mode.
- [func nw_tcp_options_set_no_push(nw_protocol_options_t, Bool)](./nw_tcp_options_set_no_push%28_,_%29.md)
  Sets TCP into no-push mode.
- [func nw_tcp_options_set_retransmit_fin_drop(nw_protocol_options_t, Bool)](./nw_tcp_options_set_retransmit_fin_drop%28_,_%29.md)
  Causes TCP to drop its connection after not receiving an ACK after a FIN.
- [func nw_tcp_options_set_disable_ack_stretching(nw_protocol_options_t, Bool)](./nw_tcp_options_set_disable_ack_stretching%28_,_%29.md)
  Disables TCP acknowledgment stretching.
- [func nw_tcp_options_set_disable_ecn(nw_protocol_options_t, Bool)](./nw_tcp_options_set_disable_ecn%28_,_%29.md)
  Disables negotiation of Explicit Congestion Notification markings.
### Configuring Keepalives
- [func nw_tcp_options_set_enable_keepalive(nw_protocol_options_t, Bool)](./nw_tcp_options_set_enable_keepalive%28_,_%29.md)
  Enables TCP keepalives.
- [func nw_tcp_options_set_keepalive_idle_time(nw_protocol_options_t, UInt32)](./nw_tcp_options_set_keepalive_idle_time%28_,_%29.md)
  Sets the number of seconds of idleness that TCP waits before sending keepalive probes.
- [func nw_tcp_options_set_keepalive_count(nw_protocol_options_t, UInt32)](./nw_tcp_options_set_keepalive_count%28_,_%29.md)
  Sets the number of keepalive probes that TCP sends before terminating the connection.
- [func nw_tcp_options_set_keepalive_interval(nw_protocol_options_t, UInt32)](./nw_tcp_options_set_keepalive_interval%28_,_%29.md)
  Sets the number of seconds that TCP waits between sending keepalive probes.
### Setting Timeouts
- [func nw_tcp_options_set_connection_timeout(nw_protocol_options_t, UInt32)](./nw_tcp_options_set_connection_timeout%28_,_%29.md)
  Sets the number of seconds that TCP waits before timing out its handshake.
- [func nw_tcp_options_set_retransmit_connection_drop_time(nw_protocol_options_t, UInt32)](./nw_tcp_options_set_retransmit_connection_drop_time%28_,_%29.md)
  Sets the number of seconds that TCP waits between retransmission attempts.
- [func nw_tcp_options_set_persist_timeout(nw_protocol_options_t, UInt32)](./nw_tcp_options_set_persist_timeout%28_,_%29.md)
  Sets the TCP persist timeout in seconds, as defined by RFC 6429.
### Inspecting TCP State
- [func nw_protocol_metadata_is_tcp(nw_protocol_metadata_t) -> Bool](./nw_protocol_metadata_is_tcp%28_%29.md)
  Checks whether a metadata object contains TCP connection state.
- [func nw_tcp_get_available_send_buffer(nw_protocol_metadata_t) -> UInt32](./nw_tcp_get_available_send_buffer%28_%29.md)
  Accesses the number of available bytes in the TCP send buffer.
- [func nw_tcp_get_available_receive_buffer(nw_protocol_metadata_t) -> UInt32](./nw_tcp_get_available_receive_buffer%28_%29.md)
  Accesses the number of available bytes in the TCP receive buffer.

## See Also

### Network Protocols
- [TLS Options](./tls-options.md)
  Configure options for connections that use Transport Layer Security.
- [QUIC Options](./quic-options.md)
  Configure options for connections that use the QUIC transport protocol.
- [UDP Options](./udp-options.md)
  Configure options for connections that use the User Datagram Protocol.
- [IP Options](./ip-options.md)
  Configure Internet Protocol options on connections.
- [WebSocket Options](./websocket-options.md)
  Configure options for connections that use WebSocket.
- [Framer Protocol Options](./framer-protocol-options.md)
  Create custom protocols to frame applications messages over a connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/tcp-options)*