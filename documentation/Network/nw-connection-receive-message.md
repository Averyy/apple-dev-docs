# nw_connection_receive_message(_:_:)

**Framework**: Network  
**Kind**: func

Schedules a single receive completion handler for a complete message, as opposed to a range of bytes.

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
func nw_connection_receive_message(_ connection: nw_connection_t, _ completion: @escaping nw_connection_receive_completion_t)
```

#### Discussion

Receiving messages allows you to deal with complete datagrams or application-layer messages without needing to reconstruct a stream.

If you are using UDP, receiving a message will deliver a single datagram.

If you request to receive a message on a protocol that is otherwise an unbounded bytestream, like TCP or TLS, note that this will not deliver any data until the stream is closed by the peer.

In order to use messages on top of a bytestream protocol, add [`WebSocket Options`](websocket-options.md) or custom [`Framer Protocol Options`](framer-protocol-options.md) to your protocol stack.

## Parameters

- `connection`: A network connection instance.
- `completion`: The completion delivers the received content, which may be nil if the message is complete or an error occurred, the message context, a flag indicating if the message is complete, and any associated error.

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

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_connection_receive_message(_:_:))*