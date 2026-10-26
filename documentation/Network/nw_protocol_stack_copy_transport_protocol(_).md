# nw_protocol_stack_copy_transport_protocol(_:)

**Framework**: Network  
**Kind**: func  
**Role**: Function

Accesses the options for the protocol stack’s transport protocol.

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
func nw_protocol_stack_copy_transport_protocol(_ stack: nw_protocol_stack_t) -> nw_protocol_options_t?
```

```c
nw_protocol_options_tnw_protocol_stack_copy_transport_protocol(nw_protocol_stack_t stack);
```

## See Also

### Configuring Lower Protocols
- [func nw_protocol_stack_set_transport_protocol(nw_protocol_stack_t, nw_protocol_options_t)](./nw_protocol_stack_set_transport_protocol%28_,_%29.md)
  Replaces the protocol stack’s transport protocol with a new set of options.
- [func nw_protocol_stack_copy_internet_protocol(nw_protocol_stack_t) -> nw_protocol_options_t?](./nw_protocol_stack_copy_internet_protocol%28_%29.md)
  Accesses the protocol stack’s Internet Protocol options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_protocol_stack_copy_transport_protocol(_:))*