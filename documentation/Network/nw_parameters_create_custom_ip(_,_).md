# nw_parameters_create_custom_ip(_:_:)

**Framework**: Network  
**Kind**: func  
**Role**: Function

Initializes parameters for connections and listeners using a custom IP protocol.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func nw_parameters_create_custom_ip(_ custom_ip_protocol_number: UInt8, _ configure_ip: @escaping nw_parameters_configure_protocol_block_t) -> nw_parameters_t
```

```c
nw_parameters_tnw_parameters_create_custom_ip(uint8_t custom_ip_protocol_number, nw_parameters_configure_protocol_block_t configure_ip);
```

## Discussion

Creating custom IP protocol connections requires the “com.apple.developer.networking.custom-protocol” entitlement.

## See Also

### Creating Parameters
- [func nw_parameters_create_secure_tcp(nw_parameters_configure_protocol_block_t, nw_parameters_configure_protocol_block_t) -> nw_parameters_t](./nw_parameters_create_secure_tcp%28_,_%29.md)
  Initializes parameters for TLS or TCP connections and listeners.
- [func nw_parameters_create_secure_udp(nw_parameters_configure_protocol_block_t, nw_parameters_configure_protocol_block_t) -> nw_parameters_t](./nw_parameters_create_secure_udp%28_,_%29.md)
  Initializes parameters for DTLS or UDP connections and listeners.
- [func nw_parameters_create_quic(nw_parameters_configure_protocol_block_t) -> nw_parameters_t](./nw_parameters_create_quic%28_%29.md)
  Initializes parameters for QUIC connections and listeners.
- [typealias nw_parameters_configure_protocol_block_t](./nw_parameters_configure_protocol_block_t.md)
  A block to configure protocol options during the creation of a parameters object.
- [func nw_parameters_create() -> nw_parameters_t](./nw_parameters_create%28%29.md)
  Initializes parameters for connections, listeners, and browsers with no protocols specified.
- [func nw_parameters_copy(nw_parameters_t) -> nw_parameters_t](./nw_parameters_copy%28_%29.md)
  Peforms a deep copy of a parameters object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_parameters_create_custom_ip(_:_:))*