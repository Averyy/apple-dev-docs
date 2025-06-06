# nw_establishment_report_t

**Framework**: Network  
**Kind**: typealias

A report that provides metrics about how a connection was established.

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
typealias nw_establishment_report_t = any OS_nw_establishment_report
```

## Topics

### Inspecting Connection Attempts
- [func nw_establishment_report_get_duration_milliseconds(nw_establishment_report_t) -> UInt64](nw_establishment_report_get_duration_milliseconds(_:).md)
  Checks the total duration of the successful connection establishment attempt, from the preparing state to the ready state.
- [func nw_establishment_report_get_previous_attempt_count(nw_establishment_report_t) -> UInt32](nw_establishment_report_get_previous_attempt_count(_:).md)
  Checks the number of attempts made before the successful attempt, when the connection moved from the preparing state back to the waiting state.
- [func nw_establishment_report_get_attempt_started_after_milliseconds(nw_establishment_report_t) -> UInt64](nw_establishment_report_get_attempt_started_after_milliseconds(_:).md)
  Accesses the time between the call to start and the beginning of the successful connection attempt, in milliseconds.
### Inspecting Resolution
- [func nw_establishment_report_enumerate_resolution_reports(nw_establishment_report_t, (nw_resolution_report_t) -> Bool)](nw_establishment_report_enumerate_resolution_reports(_:_:).md)
- [typealias nw_report_resolution_report_enumerator_t](nw_report_resolution_report_enumerator_t.md)
  Iterates a list of resolution steps, as [`nw_resolution_report_t`](nw_resolution_report_t.md) objects, performed during connection establishment, in order from first resolved to last resolved.
- [typealias nw_resolution_report_t](nw_resolution_report_t.md)
  A description of a single DNS resolution step.
- [func nw_resolution_report_get_milliseconds(nw_resolution_report_t) -> UInt64](nw_resolution_report_get_milliseconds(_:).md)
  Accesses the duration of this resolution step, from when the query was issued to when the response was complete.
- [func nw_resolution_report_get_source(nw_resolution_report_t) -> nw_report_resolution_source_t](nw_resolution_report_get_source(_:).md)
  Accesses the source of the DNS response.
- [struct nw_report_resolution_source_t](nw_report_resolution_source_t.md)
  Sources that may provide DNS responses.
- [func nw_resolution_report_get_protocol(nw_resolution_report_t) -> nw_report_resolution_protocol_t](nw_resolution_report_get_protocol(_:).md)
  Accesses the transport protocol your connection used for DNS resolution.
- [struct nw_report_resolution_protocol_t](nw_report_resolution_protocol_t.md)
  A set of transport protocols connections use for DNS resolution.
- [func nw_resolution_report_copy_successful_endpoint(nw_resolution_report_t) -> nw_endpoint_t](nw_resolution_report_copy_successful_endpoint(_:).md)
  Accesses the resolved endpoint that led to the established connection.
- [func nw_resolution_report_copy_preferred_endpoint(nw_resolution_report_t) -> nw_endpoint_t](nw_resolution_report_copy_preferred_endpoint(_:).md)
  Accesses the resolved endpoint that the connection used for its first connection attempt.
- [func nw_resolution_report_get_endpoint_count(nw_resolution_report_t) -> UInt32](nw_resolution_report_get_endpoint_count(_:).md)
  Accesses the number of endpoints resolved in this step.
- [func nw_establishment_report_enumerate_resolutions(nw_establishment_report_t, (nw_report_resolution_source_t, UInt64, UInt32, nw_endpoint_t, nw_endpoint_t) -> Bool)](nw_establishment_report_enumerate_resolutions(_:_:).md)
  Iterates a list of resolution steps performed during connection establishment, in order from first resolved to last resolved.
- [typealias nw_report_resolution_enumerator_t](nw_report_resolution_enumerator_t.md)
  A block used to enumerate resolution steps performed during connection establishment.
### Inspecting Protocol Handshakes
- [func nw_establishment_report_enumerate_protocols(nw_establishment_report_t, (nw_protocol_definition_t, UInt64, UInt64) -> Bool)](nw_establishment_report_enumerate_protocols(_:_:).md)
  Iterates a list of protocol handshakes in order from first completed to last completed.
- [typealias nw_report_protocol_enumerator_t](nw_report_protocol_enumerator_t.md)
  A block used to enumerate protocol handshakes performed during connection establishment.
### Checking for Proxies
- [func nw_establishment_report_get_proxy_configured(nw_establishment_report_t) -> Bool](nw_establishment_report_get_proxy_configured(_:).md)
  Checks whether a proxy was configured on the connection.
- [func nw_establishment_report_get_used_proxy(nw_establishment_report_t) -> Bool](nw_establishment_report_get_used_proxy(_:).md)
  Checks whether the connection used a proxy.
- [func nw_establishment_report_copy_proxy_endpoint(nw_establishment_report_t) -> nw_endpoint_t?](nw_establishment_report_copy_proxy_endpoint(_:).md)
  Accesses the endpoint of the proxy the connection used.

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

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_establishment_report_t)*