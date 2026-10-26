# nw_protocol_stack_set_transport_protocol(_:_:)

**Framework**: Network  
**Kind**: func  
**Role**: Function

Replaces the protocol stack’s transport protocol with a new set of options.

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
func nw_protocol_stack_set_transport_protocol(_ stack: nw_protocol_stack_t, _ protocol: nw_protocol_options_t)
```

```c
void nw_protocol_stack_set_transport_protocol(nw_protocol_stack_t stack, nw_protocol_options_t protocol);
```

## See Also

### Configuring Lower Protocols
- [func nw_protocol_stack_copy_transport_protocol(nw_protocol_stack_t) -> nw_protocol_options_t?](./nw_protocol_stack_copy_transport_protocol%28_%29.md)
  Accesses the options for the protocol stack’s transport protocol.
- [func nw_protocol_stack_copy_internet_protocol(nw_protocol_stack_t) -> nw_protocol_options_t?](./nw_protocol_stack_copy_internet_protocol%28_%29.md)
  Accesses the protocol stack’s Internet Protocol options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_protocol_stack_set_transport_protocol(_:_:))*