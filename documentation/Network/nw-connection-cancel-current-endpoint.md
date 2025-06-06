# nw_connection_cancel_current_endpoint(_:)

**Framework**: Network  
**Kind**: func

Causes the current endpoint to be rejected, allowing the connection to try another resolved address.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
func nw_connection_cancel_current_endpoint(_ connection: nw_connection_t)
```

#### Discussion

Protocols that do not have handshakes, such as UDP, do not allow connections to validate connectivity on their own. Cancelling an endpoint allows you to indicate that a certain endpoint should be rejected due to a lack of valid response. If other addresses were resolved for the remote endpoint, those will be attempted next.

## See Also

- [func nw_advertise_descriptor_copy_txt_record_object(nw_advertise_descriptor_t) -> nw_txt_record_t?](nw_advertise_descriptor_copy_txt_record_object(_:).md)
  Accesses the TXT record to advertise with the service.
- [func nw_advertise_descriptor_create_application_service(UnsafePointer<CChar>) -> nw_advertise_descriptor_t](nw_advertise_descriptor_create_application_service(_:).md)
- [func nw_advertise_descriptor_create_bonjour_service(UnsafePointer<CChar>?, UnsafePointer<CChar>, UnsafePointer<CChar>?) -> nw_advertise_descriptor_t?](nw_advertise_descriptor_create_bonjour_service(_:_:_:).md)
  Initializes a Bonjour service to advertise.
- [func nw_advertise_descriptor_get_application_service_name(nw_advertise_descriptor_t) -> UnsafePointer<CChar>?](nw_advertise_descriptor_get_application_service_name(_:).md)
- [func nw_advertise_descriptor_get_no_auto_rename(nw_advertise_descriptor_t) -> Bool](nw_advertise_descriptor_get_no_auto_rename(_:).md)
  Checks whether the service prohibits automatic renaming in the event of a name conflict.
- [func nw_advertise_descriptor_set_no_auto_rename(nw_advertise_descriptor_t, Bool)](nw_advertise_descriptor_set_no_auto_rename(_:_:).md)
  Sets a Boolean to indicate whether the service prohibits automatic renaming in the event of a name conflict.
- [func nw_advertise_descriptor_set_txt_record(nw_advertise_descriptor_t, UnsafeRawPointer?, Int)](nw_advertise_descriptor_set_txt_record(_:_:_:).md)
  Sets the TXT record as a raw buffer to advertise with the service.
- [func nw_advertise_descriptor_set_txt_record_object(nw_advertise_descriptor_t, nw_txt_record_t?)](nw_advertise_descriptor_set_txt_record_object(_:_:).md)
  Sets the TXT record to advertise with the service.
- [func nw_browse_descriptor_create_application_service(UnsafePointer<CChar>) -> nw_browse_descriptor_t](nw_browse_descriptor_create_application_service(_:).md)
- [func nw_browse_descriptor_create_bonjour_service(UnsafePointer<CChar>, UnsafePointer<CChar>?) -> nw_browse_descriptor_t](nw_browse_descriptor_create_bonjour_service(_:_:).md)
  Initializes a service descriptor used to discover a Bonjour service.
- [func nw_browse_descriptor_get_application_service_name(nw_browse_descriptor_t) -> UnsafePointer<CChar>?](nw_browse_descriptor_get_application_service_name(_:).md)
- [func nw_browse_descriptor_get_bonjour_service_domain(nw_browse_descriptor_t) -> UnsafePointer<CChar>?](nw_browse_descriptor_get_bonjour_service_domain(_:).md)
  Accesses the Bonjour service domain set on a browse descriptor.
- [func nw_browse_descriptor_get_bonjour_service_type(nw_browse_descriptor_t) -> UnsafePointer<CChar>](nw_browse_descriptor_get_bonjour_service_type(_:).md)
  Accesses the Bonjour service type set on a browse descriptor.
- [func nw_browse_descriptor_get_include_txt_record(nw_browse_descriptor_t) -> Bool](nw_browse_descriptor_get_include_txt_record(_:).md)
  Checks if the browse descriptor requires including associated TXT records with all results.
- [func nw_browse_descriptor_set_include_txt_record(nw_browse_descriptor_t, Bool)](nw_browse_descriptor_set_include_txt_record(_:_:).md)
  Requires including associated TXT records with all results generated for this service descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_connection_cancel_current_endpoint(_:))*