# acceptor_addrtype

**Framework**: GSS  
**Kind**: property

The type of address contained in the [`acceptor_address`](gss_channel_bindings_struct/acceptor_address.md) field.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
var acceptor_addrtype: OM_uint32
```

#### Discussion

The field takes one of the constants listed in `Address Families`.

## See Also

- [var initiator_addrtype: OM_uint32](gss_channel_bindings_struct/initiator_addrtype.md)
  The type of address contained in the [`initiator_address`](gss_channel_bindings_struct/initiator_address.md) field.
- [var initiator_address: gss_buffer_desc](gss_channel_bindings_struct/initiator_address.md)
  The network address of the acceptor, in the form specified by [`initiator_addrtype`](gss_channel_bindings_struct/initiator_addrtype.md).
- [var acceptor_address: gss_buffer_desc](gss_channel_bindings_struct/acceptor_address.md)
  The network address of the acceptor, in the form specified by [`acceptor_addrtype`](gss_channel_bindings_struct/acceptor_addrtype.md).
- [var application_data: gss_buffer_desc](gss_channel_bindings_struct/application_data.md)
  Application specific data for use in communicating a channel binding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_channel_bindings_struct/acceptor_addrtype)*