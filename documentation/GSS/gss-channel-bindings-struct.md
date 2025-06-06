# gss_channel_bindings_struct

**Framework**: GSS  
**Kind**: struct

The structure defining a channel bindings descriptor that specifies the communications channel used to carry a context.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
struct gss_channel_bindings_struct
```

## Topics

### Instance Properties
- [var initiator_addrtype: OM_uint32](gss_channel_bindings_struct/initiator_addrtype.md)
  The type of address contained in the [`initiator_address`](gss_channel_bindings_struct/initiator_address.md) field.
- [var initiator_address: gss_buffer_desc](gss_channel_bindings_struct/initiator_address.md)
  The network address of the acceptor, in the form specified by [`initiator_addrtype`](gss_channel_bindings_struct/initiator_addrtype.md).
- [var acceptor_addrtype: OM_uint32](gss_channel_bindings_struct/acceptor_addrtype.md)
  The type of address contained in the [`acceptor_address`](gss_channel_bindings_struct/acceptor_address.md) field.
- [var acceptor_address: gss_buffer_desc](gss_channel_bindings_struct/acceptor_address.md)
  The network address of the acceptor, in the form specified by [`acceptor_addrtype`](gss_channel_bindings_struct/acceptor_addrtype.md).
- [var application_data: gss_buffer_desc](gss_channel_bindings_struct/application_data.md)
  Application specific data for use in communicating a channel binding.
### Initialization
- [init()](gss_channel_bindings_struct/init.md)
  Initialize a new, empty channel bindings structure.
- [init(initiator_addrtype: OM_uint32, initiator_address: gss_buffer_desc, acceptor_addrtype: OM_uint32, acceptor_address: gss_buffer_desc, application_data: gss_buffer_desc)](gss_channel_bindings_struct/init(initiator_addrtype:initiator_address:acceptor_addrtype:acceptor_address:application_data:).md)
  Initialize a new channel bindings structure with the given configuration.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [typealias gss_ctx_id_t](gss_ctx_id_t.md)
  A pointer to an opaque type that you use to communicate context pointers with GSS-API functions.
- [typealias gss_channel_bindings_t](gss_channel_bindings_t.md)
  A pointer to a channel bindings descriptor that specifies the communications channel used to carry a context.
- [typealias gss_const_channel_bindings_t](gss_const_channel_bindings_t.md)
  A pointer to an immutable channel bindings descriptor that you use to specify the communications channel used to carry a context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_channel_bindings_struct)*