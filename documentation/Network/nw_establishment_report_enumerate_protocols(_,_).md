# nw_establishment_report_enumerate_protocols(_:_:)

**Framework**: Network  
**Kind**: func  
**Role**: Function

Iterates a list of protocol handshakes in order from first completed to last completed.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func nw_establishment_report_enumerate_protocols(_ report: nw_establishment_report_t, _ enumerate_block: (nw_protocol_definition_t, UInt64, UInt64) -> Bool)
```

```c
void nw_establishment_report_enumerate_protocols(nw_establishment_report_t report, nw_report_protocol_enumerator_t enumerate_block);
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_establishment_report_enumerate_protocols(_:_:))*