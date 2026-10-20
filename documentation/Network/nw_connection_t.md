# nw_connection_t

**Framework**: Network  
**Kind**: typealias  
**Role**: Type Alias

A bidirectional data connection between a local endpoint and a remote endpoint.

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
typealias nw_connection_t = any OS_nw_connection
```

```c
typedef NSObject<OS_nw_connection> * nw_connection_t;
```

## Topics

### Creating Connections
- [func nw_connection_create(nw_endpoint_t, nw_parameters_t) -> nw_connection_t](./nw_connection_create%28_,_%29.md)
  Initializes a new connection to a remote endpoint.
- [func nw_connection_set_queue(nw_connection_t, dispatch_queue_t)](./nw_connection_set_queue%28_,_%29.md)
  Sets the queue on which all connection events are delivered.
- [func nw_connection_start(nw_connection_t)](./nw_connection_start%28_%29.md)
  Starts establishing a connection.
- [func nw_connection_restart(nw_connection_t)](./nw_connection_restart%28_%29.md)
  Restarts a connection that is in the waiting state.
### Handling State Updates
- [struct nw_connection_state_t](./nw_connection_state_t.md)
  States indicating whether a connection can be used to send and receive data.
- [func nw_connection_set_state_changed_handler(nw_connection_t, nw_connection_state_changed_handler_t?)](./nw_connection_set_state_changed_handler%28_,_%29.md)
  Sets a handler to receive connection state updates.
- [typealias nw_connection_state_changed_handler_t](./nw_connection_state_changed_handler_t.md)
  A handler that delivers connection state updates with associated errors.
### Sending and Receiving Data
- [func nw_connection_send(nw_connection_t, dispatch_data_t?, nw_content_context_t, Bool, nw_connection_send_completion_t)](./nw_connection_send%28_,_,_,_,_%29.md)
  Sends data on a connection.
- [typealias nw_connection_send_completion_t](./nw_connection_send_completion_t.md)
  A completion handler that indicates when the connection has finished processing sent content.
- [typealias nw_content_context_t](./nw_content_context_t.md)
  A representation of a message to send or receive, containing protocol metadata and send properties.
- [func nw_connection_receive(nw_connection_t, UInt32, UInt32, nw_connection_receive_completion_t)](./nw_connection_receive%28_,_,_,_%29.md)
  Schedules a single receive completion handler, with a range indicating how many bytes the handler can receive at one time.
- [typealias nw_connection_receive_completion_t](./nw_connection_receive_completion_t.md)
  A completion handler that indicates when content has been received by the connection, or that an error was encountered.
- [func nw_connection_receive_message(nw_connection_t, nw_connection_receive_completion_t)](./nw_connection_receive_message%28_,_%29.md)
  Schedules a single receive completion handler for a complete message, as opposed to a range of bytes.
- [func nw_connection_batch(nw_connection_t, () -> Void)](./nw_connection_batch%28_,_%29.md)
  Defines a block in which calls to send and receive are processed as a batch to improve performance.
- [func nw_connection_get_maximum_datagram_size(nw_connection_t) -> UInt32](./nw_connection_get_maximum_datagram_size%28_%29.md)
  Accesses the maximum size of a datagram message that can be sent on a connection.
### Canceling Connections
- [func nw_connection_cancel(nw_connection_t)](./nw_connection_cancel%28_%29.md)
  Cancels the connection and gracefully disconnects any established network protocols.
- [func nw_connection_force_cancel(nw_connection_t)](./nw_connection_force_cancel%28_%29.md)
  Cancels the connection and immediately disconnects any established network protocols.
- [func nw_connection_cancel_current_endpoint(nw_connection_t)](./nw_connection_cancel_current_endpoint%28_%29.md)
  Causes the current endpoint to be rejected, allowing the connection to try another resolved address.
### Handling Path Updates
- [func nw_connection_copy_current_path(nw_connection_t) -> nw_path_t?](./nw_connection_copy_current_path%28_%29.md)
  Accesses the network path the connection is using.
- [func nw_connection_set_path_changed_handler(nw_connection_t, nw_connection_path_event_handler_t?)](./nw_connection_set_path_changed_handler%28_,_%29.md)
  Sets a handler that receives network path updates.
- [typealias nw_connection_path_event_handler_t](./nw_connection_path_event_handler_t.md)
  A handler that delivers network path updates.
- [func nw_connection_set_viability_changed_handler(nw_connection_t, nw_connection_boolean_event_handler_t?)](./nw_connection_set_viability_changed_handler%28_,_%29.md)
  Sets a handler that receives updates when data can be sent and received.
- [func nw_connection_set_better_path_available_handler(nw_connection_t, nw_connection_boolean_event_handler_t?)](./nw_connection_set_better_path_available_handler%28_,_%29.md)
  Sets a handler that receives updates when an alternative network path is preferred over the current path.
- [typealias nw_connection_boolean_event_handler_t](./nw_connection_boolean_event_handler_t.md)
  A handler that receives Boolean state updates from a connection, such as viability and better path state.
### Collecting Connection Metrics
- [typealias nw_establishment_report_t](./nw_establishment_report_t.md)
  A report that provides metrics about how a connection was established.
- [func nw_connection_access_establishment_report(nw_connection_t, dispatch_queue_t, nw_establishment_report_access_block_t)](./nw_connection_access_establishment_report%28_,_,_%29.md)
  Requests a copy of the connection’s establishment report once the connection is in the ready state.
- [typealias nw_establishment_report_access_block_t](./nw_establishment_report_access_block_t.md)
  A block that delivers a connection’s establishment report when it’s in the ready state.
- [typealias nw_data_transfer_report_t](./nw_data_transfer_report_t.md)
  A report that provides metrics about data being sent and received on a connection.
- [func nw_connection_create_new_data_transfer_report(nw_connection_t) -> nw_data_transfer_report_t](./nw_connection_create_new_data_transfer_report%28_%29.md)
  Begins a new data transfer report, which can later be collected.
### Copying Connection State
- [func nw_connection_copy_protocol_metadata(nw_connection_t, nw_protocol_definition_t) -> nw_protocol_metadata_t?](./nw_connection_copy_protocol_metadata%28_,_%29.md)
  Retrieves the connection-wide metadata for a specific protocol.
- [func nw_connection_copy_endpoint(nw_connection_t) -> nw_endpoint_t](./nw_connection_copy_endpoint%28_%29.md)
  Accesses the endpoint with which the connection was created.
- [func nw_connection_copy_parameters(nw_connection_t) -> nw_parameters_t](./nw_connection_copy_parameters%28_%29.md)
  Accesses the parameters with which the connection was created.
- [func nw_connection_copy_description(nw_connection_t) -> UnsafeMutablePointer<CChar>](./nw_connection_copy_description%28_%29.md)
  Copies the description of the connection as a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_connection_t)*