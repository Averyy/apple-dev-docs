# nw_connection_send(_:_:_:_:_:)

**Framework**: Network  
**Kind**: func

Sends data on a connection.

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
func nw_connection_send(_ connection: nw_connection_t, _ content: dispatch_data_t?, _ context: nw_content_context_t, _ is_complete: Bool, _ completion: @escaping nw_connection_send_completion_t)
```

## Parameters

- `connection`: A network connection instance.
- `content`: The data to send on the connection. May be nil if this send marks its context as complete, such as by sending   as the context and marking the send complete to send a write-close.
- `context`: The context associated with the content, which represents a logical message to be sent on the connection. All content sent within a single context will be sent as an in-order unit, up until the point that the context is marked complete. Once a context is marked complete, it may be re-used as a new logical message. Protocols like TCP that cannot send multiple independent messages at once (serial bytestreams) will only start processing a new context once the prior context has been marked complete. Defaults to  .
- `is_complete`: When sending using streaming protocols like TCP, this flag can be used to mark the end of a single message on the stream, of which there may be many. However, it can also indicate that the connection should send a “write close” (a TCP FIN) if the sending context is the final context on the connection. Specifically, to send a “write close”, pass   or   for the context (or create a custom context and call  ), and mark the send as complete.
- `completion`: A completion handler to notify the caller when content has been processed by the connection, or a marker that this data is idempotent ( ) and may be sent multiple times as fast open data if   was called.

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

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_connection_send(_:_:_:_:_:))*