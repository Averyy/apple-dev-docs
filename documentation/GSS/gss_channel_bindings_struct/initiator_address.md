# initiator_address

**Framework**: GSS  
**Kind**: property

The network address of the acceptor, in the form specified by [`initiator_addrtype`](gss_channel_bindings_struct/initiator_addrtype.md).

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
var initiator_address: gss_buffer_desc
```

#### Discussion

If the specified address family has more than one format, the address itself should contain enough information to distinguish among them.

## See Also

- [var initiator_addrtype: OM_uint32](gss_channel_bindings_struct/initiator_addrtype.md)
  The type of address contained in the [`initiator_address`](gss_channel_bindings_struct/initiator_address.md) field.
- [var acceptor_addrtype: OM_uint32](gss_channel_bindings_struct/acceptor_addrtype.md)
  The type of address contained in the [`acceptor_address`](gss_channel_bindings_struct/acceptor_address.md) field.
- [var acceptor_address: gss_buffer_desc](gss_channel_bindings_struct/acceptor_address.md)
  The network address of the acceptor, in the form specified by [`acceptor_addrtype`](gss_channel_bindings_struct/acceptor_addrtype.md).
- [var application_data: gss_buffer_desc](gss_channel_bindings_struct/application_data.md)
  Application specific data for use in communicating a channel binding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_channel_bindings_struct/initiator_address)*