# nw_browse_result_change_t

**Framework**: Network  
**Kind**: typealias

Flags describing ways in which discovered services can change between specific results.

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
typealias nw_browse_result_change_t = UInt64
```

## Topics

### Browse Result Change Flags
- [var nw_browse_result_change_invalid: Int](nw_browse_result_change_invalid.md)
  The comparison was invallid.
- [var nw_browse_result_change_identical: Int](nw_browse_result_change_identical.md)
  The compared services are identical.
- [var nw_browse_result_change_result_added: Int](nw_browse_result_change_result_added.md)
  A new service was discovered.
- [var nw_browse_result_change_result_removed: Int](nw_browse_result_change_result_removed.md)
  A previously discovered service was removed.
- [var nw_browse_result_change_txt_record_changed: Int](nw_browse_result_change_txt_record_changed.md)
  The service’s associated TXT record changed.
- [var nw_browse_result_change_interface_added: Int](nw_browse_result_change_interface_added.md)
  The service was discovered over a new interface.
- [var nw_browse_result_change_interface_removed: Int](nw_browse_result_change_interface_removed.md)
  The service was no longer discovered over a certain interface.

## See Also

- [typealias nw_advertise_descriptor_t](nw_advertise_descriptor_t.md)
  A description used to advertise the Bonjour service that a listener provides.
- [typealias nw_browse_descriptor_t](nw_browse_descriptor_t.md)
  A service description used to discover Bonjour services.
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

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_browse_result_change_t)*