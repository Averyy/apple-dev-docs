# nw_privacy_context_t

**Framework**: Network  
**Kind**: typealias  
**Role**: Type Alias

An object that defines the privacy requirements for a set of connections.

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
typealias nw_privacy_context_t = any OS_nw_privacy_context
```

```c
typedef NSObject<OS_nw_privacy_context> * nw_privacy_context_t;
```

#### Discussion

Use *NW_DEFAULT_PRIVACY_CONTEXT* to specify the default shared privacy context that applies to all connections that do not use a custom context.

## Topics

### Configuring Custom Privacy Settings
- [func nw_privacy_context_create(UnsafePointer<CChar>) -> nw_privacy_context_t](./nw_privacy_context_create%28_%29.md)
  Initializes a privacy context with a description string.
- [func nw_privacy_context_disable_logging(nw_privacy_context_t)](./nw_privacy_context_disable_logging%28_%29.md)
  Disables system logging of connection activity.
- [func nw_privacy_context_flush_cache(nw_privacy_context_t)](./nw_privacy_context_flush_cache%28_%29.md)
  Flushes all cached data, such as TLS session state, created by connections associated with the privacy context.
### Requiring Encrypted DNS
- [func nw_privacy_context_require_encrypted_name_resolution(nw_privacy_context_t, Bool, nw_resolver_config_t?)](./nw_privacy_context_require_encrypted_name_resolution%28_,_,_%29.md)
  Requires that any DNS name resolution for connections associated with this context use encrypted transports, such as TLS or HTTPS.
- [typealias nw_resolver_config_t](./nw_resolver_config_t.md)
  A DNS server configuration that uses TLS or HTTPS.
- [func nw_resolver_config_create_https(nw_endpoint_t) -> nw_resolver_config_t](./nw_resolver_config_create_https%28_%29.md)
  Initializes a DNS-over-HTTPS resolver configuration.
- [func nw_resolver_config_create_tls(nw_endpoint_t) -> nw_resolver_config_t](./nw_resolver_config_create_tls%28_%29.md)
  Initializes a DNS-over-TLS resolver configuration.
- [func nw_resolver_config_add_server_address(nw_resolver_config_t, nw_endpoint_t)](./nw_resolver_config_add_server_address%28_,_%29.md)
  Provides a well-known DNS server address to use instead of looking up the address dynamically.
### Configuring Proxies
- [func nw_privacy_context_add_proxy(nw_privacy_context_t, nw_proxy_config_t)](./nw_privacy_context_add_proxy%28_,_%29.md)
  Applies a proxy configuration to all connections associated with this context.
- [func nw_privacy_context_clear_proxies(nw_privacy_context_t)](./nw_privacy_context_clear_proxies%28_%29.md)
  Clears out any proxies added using [`nw_privacy_context_add_proxy(_:_:)`](./nw_privacy_context_add_proxy%28_,_%29.md)
- [typealias nw_proxy_config_t](./nw_proxy_config_t.md)
  A proxy configuration for Relays, Oblivious HTTP, HTTP CONNECT, or SOCKSv5.

## See Also

### Configuring Privacy Settings
- [func nw_parameters_set_privacy_context(nw_parameters_t, nw_privacy_context_t)](./nw_parameters_set_privacy_context%28_,_%29.md)
  Associates a privacy context with any connections or listeners that use the parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_privacy_context_t)*