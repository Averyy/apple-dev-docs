# nw_listener_t

**Framework**: Network  
**Kind**: typealias

An object you use to listen for incoming network connections.

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
typealias nw_listener_t = any OS_nw_listener
```

## Topics

### Creating Listeners
- [func nw_listener_create(nw_parameters_t) -> nw_listener_t?](nw_listener_create(_:).md)
  Initializes a network listener, which will select a random port.
- [func nw_listener_create_with_port(UnsafePointer<CChar>, nw_parameters_t) -> nw_listener_t?](nw_listener_create_with_port(_:_:).md)
  Initializes a network listener with a specified local port.
- [func nw_listener_create_with_connection(nw_connection_t, nw_parameters_t) -> nw_listener_t?](nw_listener_create_with_connection(_:_:).md)
  Initializes a network listener to receive new streams on a multiplexed connection.
- [func nw_listener_set_queue(nw_listener_t, dispatch_queue_t)](nw_listener_set_queue(_:_:).md)
  Sets the queue on which all listener events are delivered.
- [func nw_listener_start(nw_listener_t)](nw_listener_start(_:).md)
  Registers for listening for inbound connections.
- [func nw_listener_get_port(nw_listener_t) -> UInt16](nw_listener_get_port(_:).md)
  The port on which the listener can accept connections.
- [func nw_listener_cancel(nw_listener_t)](nw_listener_cancel(_:).md)
  Stops listening for inbound connections.
### Receiving Connections
- [func nw_listener_set_new_connection_handler(nw_listener_t, nw_listener_new_connection_handler_t?)](nw_listener_set_new_connection_handler(_:_:).md)
  Sets a handler that receives inbound connections.
- [typealias nw_listener_new_connection_handler_t](nw_listener_new_connection_handler_t.md)
  A handler that delivers inbound connections.
- [func nw_listener_set_new_connection_limit(nw_listener_t, UInt32)](nw_listener_set_new_connection_limit(_:_:).md)
  Resets the number of inbound connections to deliver before rejecting connections.
- [func nw_listener_get_new_connection_limit(nw_listener_t) -> UInt32](nw_listener_get_new_connection_limit(_:).md)
  Checks the remaining number of inbound connections to deliver before rejecting connections.
- [var NW_LISTENER_INFINITE_CONNECTION_LIMIT: UInt32](nw_listener_infinite_connection_limit.md)
  A static value that indicates that inbound connections should not be limited.
### Advertising Bonjour Services
- [NSBonjourServices](../BundleResources/Information-Property-List/NSBonjourServices.md)
  Bonjour service types browsed by the app.
- [NSLocalNetworkUsageDescription](../BundleResources/Information-Property-List/NSLocalNetworkUsageDescription.md)
  A message that tells people why the app is requesting access to the local network.
- [func nw_listener_set_advertise_descriptor(nw_listener_t, nw_advertise_descriptor_t?)](nw_listener_set_advertise_descriptor(_:_:).md)
  Sets a Bonjour service that advertises the listener on the local network.
- [typealias nw_advertise_descriptor_t](nw_advertise_descriptor_t.md)
  A description used to advertise the Bonjour service that a listener provides.
- [func nw_listener_set_advertised_endpoint_changed_handler(nw_listener_t, nw_listener_advertised_endpoint_changed_handler_t?)](nw_listener_set_advertised_endpoint_changed_handler(_:_:).md)
  Sets a handler that receives updates for the service endpoint being advertised.
- [typealias nw_listener_advertised_endpoint_changed_handler_t](nw_listener_advertised_endpoint_changed_handler_t.md)
  A handler that indicates changes to the service endpoints being advertised as they are added and removed.
### Handling State Updates
- [func nw_listener_set_state_changed_handler(nw_listener_t, nw_listener_state_changed_handler_t?)](nw_listener_set_state_changed_handler(_:_:).md)
  Sets a handler to receive listener state updates.
- [typealias nw_listener_state_changed_handler_t](nw_listener_state_changed_handler_t.md)
  A handler that delivers listener state updates with associated errors.
- [struct nw_listener_state_t](nw_listener_state_t.md)
  States indicating whether a listener is able to accept incoming connections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_listener_t)*