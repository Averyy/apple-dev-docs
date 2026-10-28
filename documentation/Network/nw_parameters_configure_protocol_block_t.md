# nw_parameters_configure_protocol_block_t

**Framework**: Network  
**Kind**: typealias  
**Role**: Type Alias

A block to configure protocol options during the creation of a parameters object.

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
typealias nw_parameters_configure_protocol_block_t = (nw_protocol_options_t) -> Void
```

```c
typedef void (^)(NSObject<OS_nw_protocol_options> *) nw_parameters_configure_protocol_block_t;
```

## Discussion

Passing in a block allows you to customize how a protocol will behave in a connection.

If you want to use the default configuration for a protocol, pass NW_PARAMETERS_DEFAULT_CONFIGURATION.

If you want to disable a protocol (such as TLS), pass NW_PARAMETERS_DISABLE_PROTOCOL. Not all protocols can be disabled.

## See Also

### Creating Parameters
- [func nw_parameters_create_secure_tcp(nw_parameters_configure_protocol_block_t, nw_parameters_configure_protocol_block_t) -> nw_parameters_t](./nw_parameters_create_secure_tcp%28_,_%29.md)
  Initializes parameters for TLS or TCP connections and listeners.
- [func nw_parameters_create_secure_udp(nw_parameters_configure_protocol_block_t, nw_parameters_configure_protocol_block_t) -> nw_parameters_t](./nw_parameters_create_secure_udp%28_,_%29.md)
  Initializes parameters for DTLS or UDP connections and listeners.
- [func nw_parameters_create_quic(nw_parameters_configure_protocol_block_t) -> nw_parameters_t](./nw_parameters_create_quic%28_%29.md)
  Initializes parameters for QUIC connections and listeners.
- [func nw_parameters_create() -> nw_parameters_t](./nw_parameters_create%28%29.md)
  Initializes parameters for connections, listeners, and browsers with no protocols specified.
- [func nw_parameters_create_custom_ip(UInt8, nw_parameters_configure_protocol_block_t) -> nw_parameters_t](./nw_parameters_create_custom_ip%28_,_%29.md)
  Initializes parameters for connections and listeners using a custom IP protocol.
- [func nw_parameters_copy(nw_parameters_t) -> nw_parameters_t](./nw_parameters_copy%28_%29.md)
  Peforms a deep copy of a parameters object.
### Related Documentation
- [TCP Options](./tcp-options.md)
  Configure options for connections that use the Transmission Control Protocol.
- [TLS Options](./tls-options.md)
  Configure options for connections that use Transport Layer Security.
- [UDP Options](./udp-options.md)
  Configure options for connections that use the User Datagram Protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_parameters_configure_protocol_block_t)*