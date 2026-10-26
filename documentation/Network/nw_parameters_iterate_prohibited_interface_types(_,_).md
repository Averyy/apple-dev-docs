# nw_parameters_iterate_prohibited_interface_types(_:_:)

**Framework**: Network  
**Kind**: func  
**Role**: Function

Examines the list of prohibited interface types.

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
func nw_parameters_iterate_prohibited_interface_types(_ parameters: nw_parameters_t, _ iterate_block: (nw_interface_type_t) -> Bool)
```

```c
void nw_parameters_iterate_prohibited_interface_types(nw_parameters_t parameters, nw_parameters_iterate_interface_types_block_t iterate_block);
```

## See Also

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
- [typealias nw_parameters_iterate_interface_types_block_t](./nw_parameters_iterate_interface_types_block_t.md)
  A block that allows inspection of a list of interface types.
- [func nw_parameters_prohibit_interface(nw_parameters_t, nw_interface_t)](./nw_parameters_prohibit_interface%28_,_%29.md)
  Prevents connections and listeners from using a specific interface.
- [func nw_parameters_clear_prohibited_interfaces(nw_parameters_t)](./nw_parameters_clear_prohibited_interfaces%28_%29.md)
  Removes all prohibited interface types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_parameters_iterate_prohibited_interface_types(_:_:))*