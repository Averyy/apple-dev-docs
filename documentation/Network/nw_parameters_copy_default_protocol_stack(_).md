# nw_parameters_copy_default_protocol_stack(_:)

**Framework**: Network  
**Kind**: func  
**Role**: Function

Accesses the protocol stack used by connections and listeners.

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
func nw_parameters_copy_default_protocol_stack(_ parameters: nw_parameters_t) -> nw_protocol_stack_t
```

```c
nw_protocol_stack_tnw_parameters_copy_default_protocol_stack(nw_parameters_t parameters);
```

## See Also

### Modifying Protocol Stacks
- [typealias nw_protocol_stack_t](./nw_protocol_stack_t.md)
  An ordered set of protocol options that define the protocols that connections and listeners use.
- [typealias nw_protocol_definition_t](./nw_protocol_definition_t.md)
  The abstract superclass for identifying a network protocol.
- [typealias nw_protocol_options_t](./nw_protocol_options_t.md)
  The abstract superclass for configuring the options of a network protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_parameters_copy_default_protocol_stack(_:))*