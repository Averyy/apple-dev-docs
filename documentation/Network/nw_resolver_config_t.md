# nw_resolver_config_t

**Framework**: Network  
**Kind**: typealias  
**Role**: Type Alias

A DNS server configuration that uses TLS or HTTPS.

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
typealias nw_resolver_config_t = any OS_nw_resolver_config
```

```c
typedef NSObject<OS_nw_resolver_config> * nw_resolver_config_t;
```

## See Also

### Requiring Encrypted DNS
- [func nw_privacy_context_require_encrypted_name_resolution(nw_privacy_context_t, Bool, nw_resolver_config_t?)](./nw_privacy_context_require_encrypted_name_resolution%28_,_,_%29.md)
  Requires that any DNS name resolution for connections associated with this context use encrypted transports, such as TLS or HTTPS.
- [func nw_resolver_config_create_https(nw_endpoint_t) -> nw_resolver_config_t](./nw_resolver_config_create_https%28_%29.md)
  Initializes a DNS-over-HTTPS resolver configuration.
- [func nw_resolver_config_create_tls(nw_endpoint_t) -> nw_resolver_config_t](./nw_resolver_config_create_tls%28_%29.md)
  Initializes a DNS-over-TLS resolver configuration.
- [func nw_resolver_config_add_server_address(nw_resolver_config_t, nw_endpoint_t)](./nw_resolver_config_add_server_address%28_,_%29.md)
  Provides a well-known DNS server address to use instead of looking up the address dynamically.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_resolver_config_t)*