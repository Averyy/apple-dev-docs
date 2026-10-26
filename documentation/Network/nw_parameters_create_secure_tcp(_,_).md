# nw_parameters_create_secure_tcp(_:_:)

**Framework**: Network  
**Kind**: func  
**Role**: Function

Initializes parameters for TLS or TCP connections and listeners.

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
func nw_parameters_create_secure_tcp(_ configure_tls: @escaping nw_parameters_configure_protocol_block_t, _ configure_tcp: @escaping nw_parameters_configure_protocol_block_t) -> nw_parameters_t
```

```c
nw_parameters_tnw_parameters_create_secure_tcp(nw_parameters_configure_protocol_block_t configure_tls, nw_parameters_configure_protocol_block_t configure_tcp);
```

#### Discussion

This function allows you to either use the default configurations for TLS and TCP, or use customized protocol options. If you want to use the default configuration, pass NW_PARAMETERS_DEFAULT_CONFIGURATION. If you want to customize the options for a protocol, pass a block to modify the options.

If you need to disable TLS, pass NW_PARAMETERS_DISABLE_PROTOCOL.

## See Also

### Creating Parameters
- [func nw_parameters_create_secure_udp(nw_parameters_configure_protocol_block_t, nw_parameters_configure_protocol_block_t) -> nw_parameters_t](./nw_parameters_create_secure_udp%28_,_%29.md)
  Initializes parameters for DTLS or UDP connections and listeners.
- [func nw_parameters_create_quic(nw_parameters_configure_protocol_block_t) -> nw_parameters_t](./nw_parameters_create_quic%28_%29.md)
  Initializes parameters for QUIC connections and listeners.
- [typealias nw_parameters_configure_protocol_block_t](./nw_parameters_configure_protocol_block_t.md)
  A block to configure protocol options during the creation of a parameters object.
- [func nw_parameters_create() -> nw_parameters_t](./nw_parameters_create%28%29.md)
  Initializes parameters for connections, listeners, and browsers with no protocols specified.
- [func nw_parameters_create_custom_ip(UInt8, nw_parameters_configure_protocol_block_t) -> nw_parameters_t](./nw_parameters_create_custom_ip%28_,_%29.md)
  Initializes parameters for connections and listeners using a custom IP protocol.
- [func nw_parameters_copy(nw_parameters_t) -> nw_parameters_t](./nw_parameters_copy%28_%29.md)
  Peforms a deep copy of a parameters object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_parameters_create_secure_tcp(_:_:))*