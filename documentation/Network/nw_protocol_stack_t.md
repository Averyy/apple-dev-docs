# nw_protocol_stack_t

**Framework**: Network  
**Kind**: typealias  
**Role**: Type Alias

An ordered set of protocol options that define the protocols that connections and listeners use.

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
typealias nw_protocol_stack_t = any OS_nw_protocol_stack
```

```c
typedef NSObject<OS_nw_protocol_stack> * nw_protocol_stack_t;
```

## Topics

### Modifying Application Protocols
- [func nw_protocol_stack_prepend_application_protocol(nw_protocol_stack_t, nw_protocol_options_t)](./nw_protocol_stack_prepend_application_protocol%28_,_%29.md)
  Adds a protocol onto the top of the protocol stack.
- [func nw_protocol_stack_clear_application_protocols(nw_protocol_stack_t)](./nw_protocol_stack_clear_application_protocols%28_%29.md)
  Removes all application protocols from the protocol stack.
- [func nw_protocol_stack_iterate_application_protocols(nw_protocol_stack_t, (nw_protocol_options_t) -> Void)](./nw_protocol_stack_iterate_application_protocols%28_,_%29.md)
  Iterates through the array of application protocol options that will be used by connections and listeners.
- [typealias nw_protocol_stack_iterate_protocols_block_t](./nw_protocol_stack_iterate_protocols_block_t.md)
  A block that allows you to inspect or modify a single protocol’s options.
### Configuring Lower Protocols
- [func nw_protocol_stack_copy_transport_protocol(nw_protocol_stack_t) -> nw_protocol_options_t?](./nw_protocol_stack_copy_transport_protocol%28_%29.md)
  Accesses the options for the protocol stack’s transport protocol.
- [func nw_protocol_stack_set_transport_protocol(nw_protocol_stack_t, nw_protocol_options_t)](./nw_protocol_stack_set_transport_protocol%28_,_%29.md)
  Replaces the protocol stack’s transport protocol with a new set of options.
- [func nw_protocol_stack_copy_internet_protocol(nw_protocol_stack_t) -> nw_protocol_options_t?](./nw_protocol_stack_copy_internet_protocol%28_%29.md)
  Accesses the protocol stack’s Internet Protocol options.

## See Also

### Modifying Protocol Stacks
- [func nw_parameters_copy_default_protocol_stack(nw_parameters_t) -> nw_protocol_stack_t](./nw_parameters_copy_default_protocol_stack%28_%29.md)
  Accesses the protocol stack used by connections and listeners.
- [typealias nw_protocol_definition_t](./nw_protocol_definition_t.md)
  The abstract superclass for identifying a network protocol.
- [typealias nw_protocol_options_t](./nw_protocol_options_t.md)
  The abstract superclass for configuring the options of a network protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_protocol_stack_t)*