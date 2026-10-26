# nw_protocol_stack_iterate_protocols_block_t

**Framework**: Network  
**Kind**: typealias  
**Role**: Type Alias

A block that allows you to inspect or modify a single protocol’s options.

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
typealias nw_protocol_stack_iterate_protocols_block_t = (nw_protocol_options_t) -> Void
```

```c
typedef void (^)(NSObject<OS_nw_protocol_options> *) nw_protocol_stack_iterate_protocols_block_t;
```

## See Also

### Modifying Application Protocols
- [func nw_protocol_stack_prepend_application_protocol(nw_protocol_stack_t, nw_protocol_options_t)](./nw_protocol_stack_prepend_application_protocol%28_,_%29.md)
  Adds a protocol onto the top of the protocol stack.
- [func nw_protocol_stack_clear_application_protocols(nw_protocol_stack_t)](./nw_protocol_stack_clear_application_protocols%28_%29.md)
  Removes all application protocols from the protocol stack.
- [func nw_protocol_stack_iterate_application_protocols(nw_protocol_stack_t, (nw_protocol_options_t) -> Void)](./nw_protocol_stack_iterate_application_protocols%28_,_%29.md)
  Iterates through the array of application protocol options that will be used by connections and listeners.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_protocol_stack_iterate_protocols_block_t)*