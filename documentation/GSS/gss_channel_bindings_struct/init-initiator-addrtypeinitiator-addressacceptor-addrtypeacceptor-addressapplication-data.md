# init(initiator_addrtype:initiator_address:acceptor_addrtype:acceptor_address:application_data:)

**Framework**: GSS  
**Kind**: init

Initialize a new channel bindings structure with the given configuration.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
init(initiator_addrtype: OM_uint32, initiator_address: gss_buffer_desc, acceptor_addrtype: OM_uint32, acceptor_address: gss_buffer_desc, application_data: gss_buffer_desc)
```

## Parameters

- `initiator_addrtype`: The type of address contained in the   field. Use one of the values found in  .
- `initiator_address`: The network address of the initiator, in the form specified by  .
- `acceptor_addrtype`: The type of address contained in the   field. Use one of the values found in  .
- `acceptor_address`: The network address of the acceptor, in the form specified by  .
- `application_data`: Application specific data for use in communicating a channel binding.

## See Also

- [init()](gss_channel_bindings_struct/init.md)
  Initialize a new, empty channel bindings structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_channel_bindings_struct/init(initiator_addrtype:initiator_address:acceptor_addrtype:acceptor_address:application_data:))*