# nw_ethernet_channel_create_with_parameters(_:_:_:)

**Framework**: Network  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 13.0+

## Declaration

```swift
func nw_ethernet_channel_create_with_parameters(_ ether_type: UInt16, _ interface: nw_interface_t, _ parameters: nw_parameters_t) -> nw_ethernet_channel_t
```

```c
nw_ethernet_channel_tnw_ethernet_channel_create_with_parameters(uint16_t ether_type, nw_interface_t interface, nw_parameters_t parameters);
```

## See Also

### Functions
- [func nw_advertise_descriptor_copy_txt_record_object(nw_advertise_descriptor_t) -> nw_txt_record_t?](./nw_advertise_descriptor_copy_txt_record_object%28_%29.md)
  Accesses the TXT record to advertise with the service.
- [func nw_advertise_descriptor_create_application_service(UnsafePointer<CChar>) -> nw_advertise_descriptor_t](./nw_advertise_descriptor_create_application_service%28_%29.md)
- [func nw_advertise_descriptor_create_bonjour_service(UnsafePointer<CChar>?, UnsafePointer<CChar>, UnsafePointer<CChar>?) -> nw_advertise_descriptor_t?](./nw_advertise_descriptor_create_bonjour_service%28_,_,_%29.md)
  Initializes a Bonjour service to advertise.
- [func nw_advertise_descriptor_get_application_service_name(nw_advertise_descriptor_t) -> UnsafePointer<CChar>?](./nw_advertise_descriptor_get_application_service_name%28_%29.md)
- [func nw_advertise_descriptor_get_no_auto_rename(nw_advertise_descriptor_t) -> Bool](./nw_advertise_descriptor_get_no_auto_rename%28_%29.md)
  Checks whether the service prohibits automatic renaming in the event of a name conflict.
- [func nw_advertise_descriptor_set_no_auto_rename(nw_advertise_descriptor_t, Bool)](./nw_advertise_descriptor_set_no_auto_rename%28_,_%29.md)
  Sets a Boolean to indicate whether the service prohibits automatic renaming in the event of a name conflict.
- [func nw_advertise_descriptor_set_txt_record(nw_advertise_descriptor_t, UnsafeRawPointer?, Int)](./nw_advertise_descriptor_set_txt_record%28_,_,_%29.md)
  Sets the TXT record as a raw buffer to advertise with the service.
- [func nw_advertise_descriptor_set_txt_record_object(nw_advertise_descriptor_t, nw_txt_record_t?)](./nw_advertise_descriptor_set_txt_record_object%28_,_%29.md)
  Sets the TXT record to advertise with the service.
- [func nw_browse_descriptor_create_application_service(UnsafePointer<CChar>) -> nw_browse_descriptor_t](./nw_browse_descriptor_create_application_service%28_%29.md)
- [func nw_browse_descriptor_create_bonjour_service(UnsafePointer<CChar>, UnsafePointer<CChar>?) -> nw_browse_descriptor_t](./nw_browse_descriptor_create_bonjour_service%28_,_%29.md)
  Initializes a service descriptor used to discover a Bonjour service.
- [func nw_browse_descriptor_get_application_service_name(nw_browse_descriptor_t) -> UnsafePointer<CChar>?](./nw_browse_descriptor_get_application_service_name%28_%29.md)
- [func nw_browse_descriptor_get_bonjour_service_domain(nw_browse_descriptor_t) -> UnsafePointer<CChar>?](./nw_browse_descriptor_get_bonjour_service_domain%28_%29.md)
  Accesses the Bonjour service domain set on a browse descriptor.
- [func nw_browse_descriptor_get_bonjour_service_type(nw_browse_descriptor_t) -> UnsafePointer<CChar>](./nw_browse_descriptor_get_bonjour_service_type%28_%29.md)
  Accesses the Bonjour service type set on a browse descriptor.
- [func nw_browse_descriptor_get_include_txt_record(nw_browse_descriptor_t) -> Bool](./nw_browse_descriptor_get_include_txt_record%28_%29.md)
  Checks if the browse descriptor requires including associated TXT records with all results.
- [func nw_browse_descriptor_set_include_txt_record(nw_browse_descriptor_t, Bool)](./nw_browse_descriptor_set_include_txt_record%28_,_%29.md)
  Requires including associated TXT records with all results generated for this service descriptor.
- [nw_connection_group_copy_protocol_metadata](./nw_connection_group_copy_protocol_metadata%28_,_%29.md)
- [nw_connection_group_copy_protocol_metadata_for_message](./nw_connection_group_copy_protocol_metadata_for_message%28_,_,_%29.md)
- [nw_connection_group_extract_connection](./nw_connection_group_extract_connection%28_,_,_%29.md)
- [nw_connection_group_reinsert_extracted_connection](./nw_connection_group_reinsert_extracted_connection%28_,_%29.md)
- [nw_connection_group_set_new_connection_handler](./nw_connection_group_set_new_connection_handler%28_,_%29.md)
- [nw_data_transfer_report_get_path_radio_type](./nw_data_transfer_report_get_path_radio_type%28_,_%29.md)
- [nw_endpoint_copy_txt_record](./nw_endpoint_copy_txt_record%28_%29.md)
- [nw_endpoint_get_signature](./nw_endpoint_get_signature%28_,_%29.md)
- [nw_ethernet_channel_get_maximum_payload_size](./nw_ethernet_channel_get_maximum_payload_size%28_%29.md)
- [nw_framer_copy_options](./nw_framer_copy_options%28_%29.md)
- [nw_framer_options_copy_object_value](./nw_framer_options_copy_object_value%28_,_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_ethernet_channel_create_with_parameters(_:_:_:))*