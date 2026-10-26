# nw_proxy_config_t

**Framework**: Network  
**Kind**: typealias  
**Role**: Type Alias

A proxy configuration for Relays, Oblivious HTTP, HTTP CONNECT, or SOCKSv5.

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
typealias nw_proxy_config_t = any OS_nw_proxy_config
```

```c
typedef NSObject<OS_nw_proxy_config> * nw_proxy_config_t;
```

## Topics

### Creating Proxy Configurations
- [func nw_proxy_config_create_relay(nw_relay_hop_t, nw_relay_hop_t?) -> nw_proxy_config_t](./nw_proxy_config_create_relay%28_,_%29.md)
  Initializes a proxy configuration with one or two relay hops.
- [typealias nw_relay_hop_t](./nw_relay_hop_t.md)
  A single relay server you can chain together with other servers.
- [func nw_proxy_config_create_oblivious_http(nw_relay_hop_t, UnsafePointer<CChar>, UnsafePointer<UInt8>, Int) -> nw_proxy_config_t](./nw_proxy_config_create_oblivious_http%28_,_,_,_%29.md)
  Initializes an Oblivious HTTP proxy configuration using a relay and a gateway.
- [func nw_proxy_config_create_http_connect(nw_endpoint_t, nw_protocol_options_t?) -> nw_proxy_config_t](./nw_proxy_config_create_http_connect%28_,_%29.md)
  Initializes a legacy HTTP CONNECT configuration for a proxy server accessible using HTTP/1.1.
- [func nw_proxy_config_create_socksv5(nw_endpoint_t) -> nw_proxy_config_t](./nw_proxy_config_create_socksv5%28_%29.md)
  Initializes a SOCKSv5 proxy configuration.
### Customizing Proxy Behavior
- [func nw_proxy_config_set_failover_allowed(nw_proxy_config_t, Bool)](./nw_proxy_config_set_failover_allowed%28_,_%29.md)
  Configures whether or not a proxy configuration allows failover to non-proxied connections. Failover isn’t allowed by default.
- [func nw_proxy_config_set_username_and_password(nw_proxy_config_t, UnsafePointer<CChar>, UnsafePointer<CChar>?)](./nw_proxy_config_set_username_and_password%28_,_,_%29.md)
  Sets a username and password to use as authentication for a proxy configuration.
### Inspecting Proxies
- [func nw_proxy_config_get_failover_allowed(nw_proxy_config_t) -> Bool](./nw_proxy_config_get_failover_allowed%28_%29.md)
  Checks if a proxy configuration allows failover to non-proxied connections.

## See Also

### Configuring Proxies
- [func nw_privacy_context_add_proxy(nw_privacy_context_t, nw_proxy_config_t)](./nw_privacy_context_add_proxy%28_,_%29.md)
  Applies a proxy configuration to all connections associated with this context.
- [func nw_privacy_context_clear_proxies(nw_privacy_context_t)](./nw_privacy_context_clear_proxies%28_%29.md)
  Clears out any proxies added using [`nw_privacy_context_add_proxy(_:_:)`](./nw_privacy_context_add_proxy%28_,_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_proxy_config_t)*