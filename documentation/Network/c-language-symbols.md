# C-Language Symbols

**Framework**: Network

## Topics

### C Network Structures
- [struct nw_connection_group_state_t](nw_connection_group_state_t.md)
  States that indicate whether you can use a connection group to send and receive messages.
- [struct nw_browser_state_t](nw_browser_state_t.md)
  States indicating whether a browser is able to discover services.
- [struct nw_connection_state_t](nw_connection_state_t.md)
  States indicating whether a connection can be used to send and receive data.
- [struct nw_data_transfer_report_state_t](nw_data_transfer_report_state_t.md)
  States indicating whether a data transfer report is collected yet.
- [struct nw_endpoint_type_t](nw_endpoint_type_t.md)
  The type of a network endpoint, such as a host or a service.
- [struct nw_error_domain_t](nw_error_domain_t.md)
  The error domain for errors used by the Network framework.
- [struct nw_ethernet_channel_state_t](nw_ethernet_channel_state_t.md)
  States indicating whether an Ethernet channel is able to send and receive frames.
- [struct nw_framer_start_result_t](nw_framer_start_result_t.md)
  Results that you send to indicate the disposition of your protocol after the start handler is invoked.
- [struct nw_interface_type_t](nw_interface_type_t.md)
  Types of network interfaces, based on their link layer media types.
- [struct nw_ip_ecn_flag_t](nw_ip_ecn_flag_t.md)
  Flag values for Explicit Congestion Notifications in IP packets.
- [struct nw_ip_local_address_preference_t](nw_ip_local_address_preference_t.md)
  Types of local addresses that can be selected, such as temporary or stable.
- [struct nw_ip_version_t](nw_ip_version_t.md)
  IP versions to require on connections and listeners.
- [struct nw_listener_state_t](nw_listener_state_t.md)
  States indicating whether a listener is able to accept incoming connections.
- [struct nw_multipath_service_t](nw_multipath_service_t.md)
  Modes in which a connection can support multipath protocols.
- [struct nw_parameters_expired_dns_behavior_t](nw_parameters_expired_dns_behavior_t.md)
  Options for configuring how expired DNS answers should be used.
- [struct nw_path_status_t](nw_path_status_t.md)
  Status values indicating whether a path can be used by connections.
- [struct nw_report_resolution_protocol_t](nw_report_resolution_protocol_t.md)
  A set of transport protocols connections use for DNS resolution.
- [struct nw_report_resolution_source_t](nw_report_resolution_source_t.md)
  Sources that may provide DNS responses.
- [struct nw_service_class_t](nw_service_class_t.md)
  Levels of service quality that can be used with a connection.
- [struct nw_txt_record_find_key_t](nw_txt_record_find_key_t.md)
  Status values describing what kind of value is stored in a TXT record dictionary.
- [struct nw_ws_close_code_t](nw_ws_close_code_t.md)
  Types of codes used upon closing a WebSocket connection.
- [struct nw_ws_opcode_t](nw_ws_opcode_t.md)
  Types of messages that you send and receive on a WebSocket connection.
- [struct nw_ws_response_status_t](nw_ws_response_status_t.md)
  Status values that are sent with a WebSocket server response.
- [struct nw_ws_version_t](nw_ws_version_t.md)
  Supported versions of the WebSocket protocol.
### C Network Protocols
- [protocol OS_nw_advertise_descriptor](os_nw_advertise_descriptor.md)
- [protocol OS_nw_browse_descriptor](os_nw_browse_descriptor.md)
- [protocol OS_nw_browse_result](os_nw_browse_result.md)
- [protocol OS_nw_browser](os_nw_browser.md)
- [protocol OS_nw_connection](os_nw_connection.md)
- [protocol OS_nw_connection_group](os_nw_connection_group.md)
- [protocol OS_nw_content_context](os_nw_content_context.md)
- [protocol OS_nw_data_transfer_report](os_nw_data_transfer_report.md)
- [protocol OS_nw_endpoint](os_nw_endpoint.md)
- [protocol OS_nw_error](os_nw_error.md)
- [protocol OS_nw_establishment_report](os_nw_establishment_report.md)
- [protocol OS_nw_ethernet_channel](os_nw_ethernet_channel.md)
- [protocol OS_nw_framer](os_nw_framer.md)
- [protocol OS_nw_group_descriptor](os_nw_group_descriptor.md)
- [protocol OS_nw_interface](os_nw_interface.md)
- [protocol OS_nw_listener](os_nw_listener.md)
- [protocol OS_nw_object](os_nw_object.md)
- [protocol OS_nw_parameters](os_nw_parameters.md)
- [protocol OS_nw_path](os_nw_path.md)
- [protocol OS_nw_path_monitor](os_nw_path_monitor.md)
- [protocol OS_nw_privacy_context](os_nw_privacy_context.md)
- [protocol OS_nw_protocol_definition](os_nw_protocol_definition.md)
- [protocol OS_nw_protocol_metadata](os_nw_protocol_metadata.md)
- [protocol OS_nw_protocol_options](os_nw_protocol_options.md)
- [protocol OS_nw_protocol_stack](os_nw_protocol_stack.md)
- [protocol OS_nw_proxy_config](os_nw_proxy_config.md)
- [protocol OS_nw_relay_hop](os_nw_relay_hop.md)
- [protocol OS_nw_resolution_report](os_nw_resolution_report.md)
- [protocol OS_nw_resolver_config](os_nw_resolver_config.md)
- [protocol OS_nw_txt_record](os_nw_txt_record.md)
- [protocol OS_nw_ws_request](os_nw_ws_request.md)
- [protocol OS_nw_ws_response](os_nw_ws_response.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/c-language-symbols)*