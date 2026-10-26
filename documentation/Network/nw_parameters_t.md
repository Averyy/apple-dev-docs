# nw_parameters_t

**Framework**: Network  
**Kind**: typealias  
**Role**: Type Alias

An object that stores the protocols to use for connections, options for sending data, and network path constraints.

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
typealias nw_parameters_t = any OS_nw_parameters
```

```c
typedef NSObject<OS_nw_parameters> * nw_parameters_t;
```

## Mentions

- [Indicating the source of network activity](./indicating-the-source-of-network-activity.md)

## Topics

### Creating Parameters
- [func nw_parameters_create_secure_tcp(nw_parameters_configure_protocol_block_t, nw_parameters_configure_protocol_block_t) -> nw_parameters_t](./nw_parameters_create_secure_tcp%28_,_%29.md)
  Initializes parameters for TLS or TCP connections and listeners.
- [func nw_parameters_create_secure_udp(nw_parameters_configure_protocol_block_t, nw_parameters_configure_protocol_block_t) -> nw_parameters_t](./nw_parameters_create_secure_udp%28_,_%29.md)
  Initializes parameters for DTLS or UDP connections and listeners.
- [func nw_parameters_create_quic(nw_parameters_configure_protocol_block_t) -> nw_parameters_t](./nw_parameters_create_quic%28_%29.md)
  Initializes parameters for QUIC connections and listeners.
- [typealias nw_parameters_configure_protocol_block_t](./nw_parameters_configure_protocol_block_t.md)
  A block to configure protocol options during the creation of a parameters object.
- [func nw_parameters_create() -> nw_parameters_t](./nw_parameters_create%28%29.md)
  Initializes parameters for connections, listeners, and browsers with no protocols specified.
- [func nw_parameters_create_custom_ip(UInt8, nw_parameters_configure_protocol_block_t) -> nw_parameters_t](./nw_parameters_create_custom_ip%28_,_%29.md)
  Initializes parameters for connections and listeners using a custom IP protocol.
- [func nw_parameters_copy(nw_parameters_t) -> nw_parameters_t](./nw_parameters_copy%28_%29.md)
  Peforms a deep copy of a parameters object.
### Modifying Protocol Stacks
- [func nw_parameters_copy_default_protocol_stack(nw_parameters_t) -> nw_protocol_stack_t](./nw_parameters_copy_default_protocol_stack%28_%29.md)
  Accesses the protocol stack used by connections and listeners.
- [typealias nw_protocol_stack_t](./nw_protocol_stack_t.md)
  An ordered set of protocol options that define the protocols that connections and listeners use.
- [typealias nw_protocol_definition_t](./nw_protocol_definition_t.md)
  The abstract superclass for identifying a network protocol.
- [typealias nw_protocol_options_t](./nw_protocol_options_t.md)
  The abstract superclass for configuring the options of a network protocol.
### Selecting Paths
- [func nw_parameters_set_required_interface_type(nw_parameters_t, nw_interface_type_t)](./nw_parameters_set_required_interface_type%28_,_%29.md)
  Sets an interface type to require on connections and listeners.
- [func nw_parameters_get_required_interface_type(nw_parameters_t) -> nw_interface_type_t](./nw_parameters_get_required_interface_type%28_%29.md)
  Accesses the interface type required on connections and listeners.
- [func nw_parameters_require_interface(nw_parameters_t, nw_interface_t?)](./nw_parameters_require_interface%28_,_%29.md)
  Sets a specific interface to require on connections, listeners, and browsers.
- [func nw_parameters_copy_required_interface(nw_parameters_t) -> nw_interface_t?](./nw_parameters_copy_required_interface%28_%29.md)
  Accesses the interface required on connections, listeners, and browsers.
- [func nw_parameters_set_local_endpoint(nw_parameters_t, nw_endpoint_t?)](./nw_parameters_set_local_endpoint%28_,_%29.md)
  Sets a specific local IP address and port to use for connections and listeners.
- [func nw_parameters_copy_local_endpoint(nw_parameters_t) -> nw_endpoint_t?](./nw_parameters_copy_local_endpoint%28_%29.md)
  Accesses the local IP address and port used for connections and listeners.
- [func nw_parameters_set_prohibit_constrained(nw_parameters_t, Bool)](./nw_parameters_set_prohibit_constrained%28_,_%29.md)
  Prevents connections, listeners, and browsers from using network paths marked as constrained by Low Data Mode.
- [func nw_parameters_get_prohibit_constrained(nw_parameters_t) -> Bool](./nw_parameters_get_prohibit_constrained%28_%29.md)
  Checks if connections, listeners, and browsers are prevented from using network paths marked as constrained by Low Data Mode.
- [func nw_parameters_set_prohibit_expensive(nw_parameters_t, Bool)](./nw_parameters_set_prohibit_expensive%28_,_%29.md)
  Prevents connections, listeners, and browsers from using network paths marked as expensive.
- [func nw_parameters_get_prohibit_expensive(nw_parameters_t) -> Bool](./nw_parameters_get_prohibit_expensive%28_%29.md)
  Checks if connections, listeners, and browsers are prevented from using network paths marked as expensive.
- [func nw_parameters_prohibit_interface_type(nw_parameters_t, nw_interface_type_t)](./nw_parameters_prohibit_interface_type%28_,_%29.md)
  Prevents connections, listeners, and browsers from using a specific interface type.
- [func nw_parameters_clear_prohibited_interface_types(nw_parameters_t)](./nw_parameters_clear_prohibited_interface_types%28_%29.md)
  Removes all prohibited interface types.
- [func nw_parameters_iterate_prohibited_interface_types(nw_parameters_t, (nw_interface_type_t) -> Bool)](./nw_parameters_iterate_prohibited_interface_types%28_,_%29.md)
  Examines the list of prohibited interface types.
- [typealias nw_parameters_iterate_interface_types_block_t](./nw_parameters_iterate_interface_types_block_t.md)
  A block that allows inspection of a list of interface types.
- [func nw_parameters_prohibit_interface(nw_parameters_t, nw_interface_t)](./nw_parameters_prohibit_interface%28_,_%29.md)
  Prevents connections and listeners from using a specific interface.
- [func nw_parameters_clear_prohibited_interfaces(nw_parameters_t)](./nw_parameters_clear_prohibited_interfaces%28_%29.md)
  Removes all prohibited interface types.
- [func nw_parameters_iterate_prohibited_interfaces(nw_parameters_t, (nw_interface_t) -> Bool)](./nw_parameters_iterate_prohibited_interfaces%28_,_%29.md)
  Examines the list of prohibited interfaces.
- [typealias nw_parameters_iterate_interfaces_block_t](./nw_parameters_iterate_interfaces_block_t.md)
  A block that allows inspection of a list of interfaces.
### Customizing Connection Options
- [func nw_parameters_set_multipath_service(nw_parameters_t, nw_multipath_service_t)](./nw_parameters_set_multipath_service%28_,_%29.md)
  Enables multipath protocols to allow connections to use multiple interfaces.
- [func nw_parameters_get_multipath_service(nw_parameters_t) -> nw_multipath_service_t](./nw_parameters_get_multipath_service%28_%29.md)
  Checks if multipath is enabled on a connection.
- [struct nw_multipath_service_t](./nw_multipath_service_t.md)
  Modes in which a connection can support multipath protocols.
- [func nw_parameters_set_service_class(nw_parameters_t, nw_service_class_t)](./nw_parameters_set_service_class%28_,_%29.md)
  Sets a level of service quality to use for connections.
- [func nw_parameters_get_service_class(nw_parameters_t) -> nw_service_class_t](./nw_parameters_get_service_class%28_%29.md)
  Checks the level of service quality used for connections.
- [struct nw_service_class_t](./nw_service_class_t.md)
  Levels of service quality that can be used with a connection.
- [func nw_parameters_set_fast_open_enabled(nw_parameters_t, Bool)](./nw_parameters_set_fast_open_enabled%28_,_%29.md)
  Enables sending application data with protocol handshakes.
- [func nw_parameters_get_fast_open_enabled(nw_parameters_t) -> Bool](./nw_parameters_get_fast_open_enabled%28_%29.md)
  Checks if sending application data with protocol handshakes is enabled.
- [func nw_parameters_set_expired_dns_behavior(nw_parameters_t, nw_parameters_expired_dns_behavior_t)](./nw_parameters_set_expired_dns_behavior%28_,_%29.md)
  Sets the behavior for how expired DNS answers should be used.
- [func nw_parameters_get_expired_dns_behavior(nw_parameters_t) -> nw_parameters_expired_dns_behavior_t](./nw_parameters_get_expired_dns_behavior%28_%29.md)
  Checks the behavior for how expired DNS answers should be used.
- [struct nw_parameters_expired_dns_behavior_t](./nw_parameters_expired_dns_behavior_t.md)
  Options for configuring how expired DNS answers should be used.
- [func nw_parameters_set_requires_dnssec_validation(nw_parameters_t, Bool)](./nw_parameters_set_requires_dnssec_validation%28_,_%29.md)
  Determines whether a connection requires DNSSEC validation when resolving endpoints.
- [func nw_parameters_requires_dnssec_validation(nw_parameters_t) -> Bool](./nw_parameters_requires_dnssec_validation%28_%29.md)
  Checks whether a connection requires DNSSEC validation when resolving endpoints.
- [func nw_parameters_set_prefer_no_proxy(nw_parameters_t, Bool)](./nw_parameters_set_prefer_no_proxy%28_,_%29.md)
  Sets a Boolean that indicates that connections should ignore proxies when they are enabled on the system.
- [func nw_parameters_get_prefer_no_proxy(nw_parameters_t) -> Bool](./nw_parameters_get_prefer_no_proxy%28_%29.md)
  Checks if proxies are ignored by default.
- [func nw_parameters_set_include_peer_to_peer(nw_parameters_t, Bool)](./nw_parameters_set_include_peer_to_peer%28_,_%29.md)
  Enables peer-to-peer link technologies for connections and listeners.
- [func nw_parameters_get_include_peer_to_peer(nw_parameters_t) -> Bool](./nw_parameters_get_include_peer_to_peer%28_%29.md)
  Checks whether a connection is allowed to use peer-to-peer link technologies.
- [func nw_parameters_set_reuse_local_address(nw_parameters_t, Bool)](./nw_parameters_set_reuse_local_address%28_,_%29.md)
  Allows reusing local addresses and ports across connections.
- [func nw_parameters_get_reuse_local_address(nw_parameters_t) -> Bool](./nw_parameters_get_reuse_local_address%28_%29.md)
  Checks whether a connection allows reusing local addresses and ports.
- [func nw_parameters_set_local_only(nw_parameters_t, Bool)](./nw_parameters_set_local_only%28_,_%29.md)
  Restricts listeners to only accepting connections from the local link.
- [func nw_parameters_get_local_only(nw_parameters_t) -> Bool](./nw_parameters_get_local_only%28_%29.md)
  Checks if a listener is restricted to accepting connections from the local link.
### Configuring Privacy Settings
- [func nw_parameters_set_privacy_context(nw_parameters_t, nw_privacy_context_t)](./nw_parameters_set_privacy_context%28_,_%29.md)
  Associates a privacy context with any connections or listeners that use the parameters.
- [typealias nw_privacy_context_t](./nw_privacy_context_t.md)
  An object that defines the privacy requirements for a set of connections.

## See Also

### Essentials
- [nw_endpoint_t](./nw_endpoint_t.md)
  A local or remote endpoint in a network connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_parameters_t)*