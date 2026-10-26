# nw_privacy_context_require_encrypted_name_resolution(_:_:_:)

**Framework**: Network  
**Kind**: func  
**Role**: Function

Requires that any DNS name resolution for connections associated with this context use encrypted transports, such as TLS or HTTPS.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
func nw_privacy_context_require_encrypted_name_resolution(_ privacy_context: nw_privacy_context_t, _ require_encrypted_name_resolution: Bool, _ fallback_resolver_config: nw_resolver_config_t?)
```

```c
void nw_privacy_context_require_encrypted_name_resolution(nw_privacy_context_t privacy_context, bool require_encrypted_name_resolution, nw_resolver_config_t fallback_resolver_config);
```

## See Also

### Requiring Encrypted DNS
- [typealias nw_resolver_config_t](./nw_resolver_config_t.md)
  A DNS server configuration that uses TLS or HTTPS.
- [func nw_resolver_config_create_https(nw_endpoint_t) -> nw_resolver_config_t](./nw_resolver_config_create_https%28_%29.md)
  Initializes a DNS-over-HTTPS resolver configuration.
- [func nw_resolver_config_create_tls(nw_endpoint_t) -> nw_resolver_config_t](./nw_resolver_config_create_tls%28_%29.md)
  Initializes a DNS-over-TLS resolver configuration.
- [func nw_resolver_config_add_server_address(nw_resolver_config_t, nw_endpoint_t)](./nw_resolver_config_add_server_address%28_,_%29.md)
  Provides a well-known DNS server address to use instead of looking up the address dynamically.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_privacy_context_require_encrypted_name_resolution(_:_:_:))*