# nw_protocol_definition_t

**Framework**: Network  
**Kind**: typealias  
**Role**: Type Alias

The abstract superclass for identifying a network protocol.

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
typealias nw_protocol_definition_t = any OS_nw_protocol_definition
```

```c
typedef NSObject<OS_nw_protocol_definition> * nw_protocol_definition_t;
```

## Topics

### Comparing Protocols
- [func nw_protocol_definition_is_equal(nw_protocol_definition_t, nw_protocol_definition_t) -> Bool](./nw_protocol_definition_is_equal%28_,_%29.md)
  Compares two protocol definitions, and returns true if they represent the same protocol implementation.

## See Also

### Modifying Protocol Stacks
- [func nw_parameters_copy_default_protocol_stack(nw_parameters_t) -> nw_protocol_stack_t](./nw_parameters_copy_default_protocol_stack%28_%29.md)
  Accesses the protocol stack used by connections and listeners.
- [typealias nw_protocol_stack_t](./nw_protocol_stack_t.md)
  An ordered set of protocol options that define the protocols that connections and listeners use.
- [typealias nw_protocol_options_t](./nw_protocol_options_t.md)
  The abstract superclass for configuring the options of a network protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_protocol_definition_t)*