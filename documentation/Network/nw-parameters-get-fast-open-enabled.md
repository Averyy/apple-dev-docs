# nw_parameters_get_fast_open_enabled(_:)

**Framework**: Network  
**Kind**: func

Checks if sending application data with protocol handshakes is enabled.

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
func nw_parameters_get_fast_open_enabled(_ parameters: nw_parameters_t) -> Bool
```

## See Also

- [func nw_parameters_set_multipath_service(nw_parameters_t, nw_multipath_service_t)](nw_parameters_set_multipath_service(_:_:).md)
  Enables multipath protocols to allow connections to use multiple interfaces.
- [func nw_parameters_get_multipath_service(nw_parameters_t) -> nw_multipath_service_t](nw_parameters_get_multipath_service(_:).md)
  Checks if multipath is enabled on a connection.
- [struct nw_multipath_service_t](nw_multipath_service_t.md)
  Modes in which a connection can support multipath protocols.
- [func nw_parameters_set_service_class(nw_parameters_t, nw_service_class_t)](nw_parameters_set_service_class(_:_:).md)
  Sets a level of service quality to use for connections.
- [func nw_parameters_get_service_class(nw_parameters_t) -> nw_service_class_t](nw_parameters_get_service_class(_:).md)
  Checks the level of service quality used for connections.
- [struct nw_service_class_t](nw_service_class_t.md)
  Levels of service quality that can be used with a connection.
- [func nw_parameters_set_fast_open_enabled(nw_parameters_t, Bool)](nw_parameters_set_fast_open_enabled(_:_:).md)
  Enables sending application data with protocol handshakes.
- [func nw_parameters_set_expired_dns_behavior(nw_parameters_t, nw_parameters_expired_dns_behavior_t)](nw_parameters_set_expired_dns_behavior(_:_:).md)
  Sets the behavior for how expired DNS answers should be used.
- [func nw_parameters_get_expired_dns_behavior(nw_parameters_t) -> nw_parameters_expired_dns_behavior_t](nw_parameters_get_expired_dns_behavior(_:).md)
  Checks the behavior for how expired DNS answers should be used.
- [struct nw_parameters_expired_dns_behavior_t](nw_parameters_expired_dns_behavior_t.md)
  Options for configuring how expired DNS answers should be used.
- [func nw_parameters_set_requires_dnssec_validation(nw_parameters_t, Bool)](nw_parameters_set_requires_dnssec_validation(_:_:).md)
  Determines whether a connection requires DNSSEC validation when resolving endpoints.
- [func nw_parameters_requires_dnssec_validation(nw_parameters_t) -> Bool](nw_parameters_requires_dnssec_validation(_:).md)
  Checks whether a connection requires DNSSEC validation when resolving endpoints.
- [func nw_parameters_set_prefer_no_proxy(nw_parameters_t, Bool)](nw_parameters_set_prefer_no_proxy(_:_:).md)
  Sets a Boolean that indicates that connections should ignore proxies when they are enabled on the system.
- [func nw_parameters_get_prefer_no_proxy(nw_parameters_t) -> Bool](nw_parameters_get_prefer_no_proxy(_:).md)
  Checks if proxies are ignored by default.
- [func nw_parameters_set_include_peer_to_peer(nw_parameters_t, Bool)](nw_parameters_set_include_peer_to_peer(_:_:).md)
  Enables peer-to-peer link technologies for connections and listeners.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_parameters_get_fast_open_enabled(_:))*