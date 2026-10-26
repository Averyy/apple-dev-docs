# WebSocket Options

**Framework**: Network  
**Role**: API Collection

Configure options for connections that use WebSocket.

## Topics

### Creating WebSocket Connections
- [func nw_protocol_copy_ws_definition() -> nw_protocol_definition_t](./nw_protocol_copy_ws_definition%28%29.md)
  Accesses the system definition of the WebSocket protocol.
- [func nw_ws_create_options(nw_ws_version_t) -> nw_protocol_options_t](./nw_ws_create_options%28_%29.md)
  Initializes a default set of WebSocket connection options.
- [struct nw_ws_version_t](./nw_ws_version_t.md)
  Supported versions of the WebSocket protocol.
- [func nw_ws_options_set_auto_reply_ping(nw_protocol_options_t, Bool)](./nw_ws_options_set_auto_reply_ping%28_,_%29.md)
  Configures the connection to automatically reply to Ping messages instead of delivering them to you.
- [func nw_ws_options_set_maximum_message_size(nw_protocol_options_t, Int)](./nw_ws_options_set_maximum_message_size%28_,_%29.md)
  Sets the maximum allowed message size, in bytes, to be received by the WebSocket connection.
### Configuring Client Handshakes
- [func nw_ws_options_add_additional_header(nw_protocol_options_t, UnsafePointer<CChar>, UnsafePointer<CChar>)](./nw_ws_options_add_additional_header%28_,_,_%29.md)
  Adds additional HTTP header fields to be sent by the client during the WebSocket handshake.
- [func nw_ws_options_add_subprotocol(nw_protocol_options_t, UnsafePointer<CChar>)](./nw_ws_options_add_subprotocol%28_,_%29.md)
  Adds to the list of supported application protocols that will be presented to a WebSocket server during connection establishment.
- [func nw_ws_options_set_skip_handshake(nw_protocol_options_t, Bool)](./nw_ws_options_set_skip_handshake%28_,_%29.md)
  Specifies whether the WebSocket protocol skips its handshake and begins framing data once the underlying connection is established.
### Handling WebSocket Messages
- [func nw_protocol_metadata_is_ws(nw_protocol_metadata_t) -> Bool](./nw_protocol_metadata_is_ws%28_%29.md)
  Checks whether a metadata object represents a WebSocket message.
- [func nw_ws_create_metadata(nw_ws_opcode_t) -> nw_protocol_metadata_t](./nw_ws_create_metadata%28_%29.md)
  Initializes a WebSocket message with a specific type code.
- [func nw_ws_metadata_get_opcode(nw_protocol_metadata_t) -> nw_ws_opcode_t](./nw_ws_metadata_get_opcode%28_%29.md)
  Checks the type code on a WebSocket message.
- [struct nw_ws_opcode_t](./nw_ws_opcode_t.md)
  Types of messages that you send and receive on a WebSocket connection.
- [func nw_ws_metadata_set_close_code(nw_protocol_metadata_t, nw_ws_close_code_t)](./nw_ws_metadata_set_close_code%28_,_%29.md)
  Sets a close code on a WebSocket message.
- [func nw_ws_metadata_get_close_code(nw_protocol_metadata_t) -> nw_ws_close_code_t](./nw_ws_metadata_get_close_code%28_%29.md)
  Accesses the close code on a WebSocket message.
- [struct nw_ws_close_code_t](./nw_ws_close_code_t.md)
  Types of codes used upon closing a WebSocket connection.
- [func nw_ws_metadata_set_pong_handler(nw_protocol_metadata_t, dispatch_queue_t, nw_ws_pong_handler_t)](./nw_ws_metadata_set_pong_handler%28_,_,_%29.md)
  Sets a handler on a Ping message to be invoked when the corresponding Pong message is received.
- [typealias nw_ws_pong_handler_t](./nw_ws_pong_handler_t.md)
  A handler that indicates that a Pong message has been received for a previously sent Ping message, or that an error was encountered.
- [func nw_ws_metadata_copy_server_response(nw_protocol_metadata_t) -> nw_ws_response_t](./nw_ws_metadata_copy_server_response%28_%29.md)
  Accesses the WebSocket server’s response sent during the handshake.
### Handling Server Handshakes
- [func nw_ws_options_set_client_request_handler(nw_protocol_options_t, dispatch_queue_t, nw_ws_client_request_handler_t)](./nw_ws_options_set_client_request_handler%28_,_,_%29.md)
  Sets a handler to react to as a server to inbound WebSocket client handshakes.
- [typealias nw_ws_client_request_handler_t](./nw_ws_client_request_handler_t.md)
  A handler that delivers inbound client handshake requests.
- [typealias nw_ws_request_t](./nw_ws_request_t.md)
  A WebSocket handshake request sent from a client to a server.
- [func nw_ws_request_enumerate_subprotocols(nw_ws_request_t, (UnsafePointer<CChar>) -> Bool) -> Bool](./nw_ws_request_enumerate_subprotocols%28_,_%29.md)
  Enumerates the supported subprotocols in a WebSocket message.
- [typealias nw_ws_subprotocol_enumerator_t](./nw_ws_subprotocol_enumerator_t.md)
  A block that enumerates the supported subprotocols in a WebSocket client request.
- [func nw_ws_request_enumerate_additional_headers(nw_ws_request_t, (UnsafePointer<CChar>, UnsafePointer<CChar>) -> Bool) -> Bool](./nw_ws_request_enumerate_additional_headers%28_,_%29.md)
  Enumerates additional HTTP headers in a WebSocket message.
- [typealias nw_ws_additional_header_enumerator_t](./nw_ws_additional_header_enumerator_t.md)
  A block that enumerates additional HTTP headers in a WebSocket client request.
- [typealias nw_ws_response_t](./nw_ws_response_t.md)
  A WebSocket handshake reponse sent from a server to a client.
- [func nw_ws_response_create(nw_ws_response_status_t, UnsafePointer<CChar>?) -> nw_ws_response_t](./nw_ws_response_create%28_,_%29.md)
  Initializes a WebSocket server response with a status and selected subprotocol.
- [struct nw_ws_response_status_t](./nw_ws_response_status_t.md)
  Status values that are sent with a WebSocket server response.
- [func nw_ws_response_add_additional_header(nw_ws_response_t, UnsafePointer<CChar>, UnsafePointer<CChar>)](./nw_ws_response_add_additional_header%28_,_,_%29.md)
  Adds an additional HTTP header to a WebSocket server response.
- [func nw_ws_response_get_status(nw_ws_response_t?) -> nw_ws_response_status_t](./nw_ws_response_get_status%28_%29.md)
  Accesses the status of a WebSocket server response.
- [func nw_ws_response_get_selected_subprotocol(nw_ws_response_t) -> UnsafePointer<CChar>?](./nw_ws_response_get_selected_subprotocol%28_%29.md)
  Accesses the selected subprotocol in a WebSocket server response.
- [func nw_ws_response_enumerate_additional_headers(nw_ws_response_t, (UnsafePointer<CChar>, UnsafePointer<CChar>) -> Bool) -> Bool](./nw_ws_response_enumerate_additional_headers%28_,_%29.md)
  Enumerates the additional HTTP headers in a WebSocket server response.

## See Also

### Network Protocols
- [TCP Options](./tcp-options.md)
  Configure options for connections that use the Transmission Control Protocol.
- [TLS Options](./tls-options.md)
  Configure options for connections that use Transport Layer Security.
- [QUIC Options](./quic-options.md)
  Configure options for connections that use the QUIC transport protocol.
- [UDP Options](./udp-options.md)
  Configure options for connections that use the User Datagram Protocol.
- [IP Options](./ip-options.md)
  Configure Internet Protocol options on connections.
- [Framer Protocol Options](./framer-protocol-options.md)
  Create custom protocols to frame applications messages over a connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/websocket-options)*