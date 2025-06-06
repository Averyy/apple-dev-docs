# nw_browse_descriptor_t

**Framework**: Network  
**Kind**: typealias

A service description used to discover Bonjour services.

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
typealias nw_browse_descriptor_t = any OS_nw_browse_descriptor
```

## Topics

### Creating Browse Descriptors
- [func nw_browse_descriptor_create_bonjour_service(UnsafePointer<CChar>, UnsafePointer<CChar>?) -> nw_browse_descriptor_t](nw_browse_descriptor_create_bonjour_service(_:_:).md)
  Initializes a service descriptor used to discover a Bonjour service.
- [func nw_browse_descriptor_set_include_txt_record(nw_browse_descriptor_t, Bool)](nw_browse_descriptor_set_include_txt_record(_:_:).md)
  Requires including associated TXT records with all results generated for this service descriptor.
### Inspecting Browse Descriptors
- [func nw_browse_descriptor_get_bonjour_service_type(nw_browse_descriptor_t) -> UnsafePointer<CChar>](nw_browse_descriptor_get_bonjour_service_type(_:).md)
  Accesses the Bonjour service type set on a browse descriptor.
- [func nw_browse_descriptor_get_bonjour_service_domain(nw_browse_descriptor_t) -> UnsafePointer<CChar>?](nw_browse_descriptor_get_bonjour_service_domain(_:).md)
  Accesses the Bonjour service domain set on a browse descriptor.
- [func nw_browse_descriptor_get_include_txt_record(nw_browse_descriptor_t) -> Bool](nw_browse_descriptor_get_include_txt_record(_:).md)
  Checks if the browse descriptor requires including associated TXT records with all results.

## See Also

- [typealias nw_advertise_descriptor_t](nw_advertise_descriptor_t.md)
  A description used to advertise the Bonjour service that a listener provides.
- [typealias nw_browse_result_change_t](nw_browse_result_change_t.md)
  Flags describing ways in which discovered services can change between specific results.
- [typealias nw_browse_result_enumerate_interface_t](nw_browse_result_enumerate_interface_t.md)
  A handler that enumerates the interfaces associated with a discovered service.
- [typealias nw_browse_result_t](nw_browse_result_t.md)
  A discovered service and metadata about the service.
- [typealias nw_browser_browse_results_changed_handler_t](nw_browser_browse_results_changed_handler_t.md)
  A handler that delivers updates about discovered services.
- [typealias nw_browser_state_changed_handler_t](nw_browser_state_changed_handler_t.md)
  A handler that delivers browser state updates with associated errors.
- [typealias nw_browser_t](nw_browser_t.md)
  An object you use to browse for available network services.
- [typealias nw_connection_boolean_event_handler_t](nw_connection_boolean_event_handler_t.md)
  A handler that receives Boolean state updates from a connection, such as viability and better path state.
- [typealias nw_connection_group_new_connection_handler_t](nw_connection_group_new_connection_handler_t.md)
- [typealias nw_connection_group_receive_handler_t](nw_connection_group_receive_handler_t.md)
  A handler that receives inbound messages from members of the group.
- [typealias nw_connection_group_send_completion_t](nw_connection_group_send_completion_t.md)
  A completion to notify you when data has been processed and sent.
- [typealias nw_connection_group_state_changed_handler_t](nw_connection_group_state_changed_handler_t.md)
  A handler that receives connection group state updates.
- [typealias nw_connection_group_t](nw_connection_group_t.md)
  An object you use to communicate with a group of endpoints, such as an IP multicast group on a local network.
- [typealias nw_connection_path_event_handler_t](nw_connection_path_event_handler_t.md)
  A handler that delivers network path updates.
- [typealias nw_connection_receive_completion_t](nw_connection_receive_completion_t.md)
  A completion handler that indicates when content has been received by the connection, or that an error was encountered.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_browse_descriptor_t)*