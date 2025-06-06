# nw_txt_record_find_key_t

**Framework**: Network  
**Kind**: struct

Status values describing what kind of value is stored in a TXT record dictionary.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
struct nw_txt_record_find_key_t
```

## Topics

### Key Value Status
- [var nw_txt_record_find_key_invalid: nw_txt_record_find_key_t](nw_txt_record_find_key_invalid.md)
  The key is not valid.
- [var nw_txt_record_find_key_not_present: nw_txt_record_find_key_t](nw_txt_record_find_key_not_present.md)
  The key is not present in the dictionary.
- [var nw_txt_record_find_key_no_value: nw_txt_record_find_key_t](nw_txt_record_find_key_no_value.md)
  The key is present but has no associated value.
- [var nw_txt_record_find_key_empty_value: nw_txt_record_find_key_t](nw_txt_record_find_key_empty_value.md)
  The key is present and has an empty associated value.
- [var nw_txt_record_find_key_non_empty_value: nw_txt_record_find_key_t](nw_txt_record_find_key_non_empty_value.md)
  The key has an associated value.
### Initializers
- [init(UInt32)](nw_txt_record_find_key_t/init(_:).md)
- [init(rawValue: UInt32)](nw_txt_record_find_key_t/init(rawvalue:).md)
### Instance Properties
- [var rawValue: UInt32](nw_txt_record_find_key_t/rawvalue.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_txt_record_find_key_t)*