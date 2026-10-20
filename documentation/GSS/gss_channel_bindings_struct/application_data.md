# application_data

**Framework**: GSS  
**Kind**: property  
**Role**: Instance Property

Application specific data for use in communicating a channel binding.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
var application_data: gss_buffer_desc
```

```c
gss_buffer_desc application_data;
```

## See Also

### Instance Properties
- [var initiator_addrtype: OM_uint32](./initiator_addrtype.md)
  The type of address contained in the [`initiator_address`](./initiator_address.md) field.
- [var initiator_address: gss_buffer_desc](./initiator_address.md)
  The network address of the acceptor, in the form specified by [`initiator_addrtype`](./initiator_addrtype.md).
- [var acceptor_addrtype: OM_uint32](./acceptor_addrtype.md)
  The type of address contained in the [`acceptor_address`](./acceptor_address.md) field.
- [var acceptor_address: gss_buffer_desc](./acceptor_address.md)
  The network address of the acceptor, in the form specified by [`acceptor_addrtype`](./acceptor_addrtype.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_channel_bindings_struct/application_data)*