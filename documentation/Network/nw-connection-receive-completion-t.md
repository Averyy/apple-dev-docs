# nw_connection_receive_completion_t

**Framework**: Network  
**Kind**: typealias

A completion handler that indicates when content has been received by the connection, or that an error was encountered.

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
typealias nw_connection_receive_completion_t = (dispatch_data_t?, nw_content_context_t?, Bool, nw_error_t?) -> Void
```

## Parameters

- `content`: The received content, as constrained by the minimum and maximum length. This may be nil if the message or stream is complete (without any more data to deliver), or if an error was encountered.
- `context`: Content context describing the received content. This includes protocol metadata that lets the caller introspect information about the received content (such as flags on a packet).
- `is_complete`: An indication that this context (a message or stream, for example) is now complete. For protocols such as TCP, this will be marked when the entire stream has be closed in the reading direction. For protocols such as UDP, this will be marked when the end of a datagram has been reached.
- `error`: An error will be sent if the receive was terminated before completing. There may still be content delivered along with the error, but this content may be shorter than the requested ranges. An error will be sent for any outstanding receives when the connection is cancelled.

## See Also

- [typealias nw_advertise_descriptor_t](nw_advertise_descriptor_t.md)
  A description used to advertise the Bonjour service that a listener provides.
- [typealias nw_browse_descriptor_t](nw_browse_descriptor_t.md)
  A service description used to discover Bonjour services.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_connection_receive_completion_t)*