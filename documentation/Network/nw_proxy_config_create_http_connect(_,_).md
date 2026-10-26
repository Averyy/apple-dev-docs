# nw_proxy_config_create_http_connect(_:_:)

**Framework**: Network  
**Kind**: func  
**Role**: Function

Initializes a legacy HTTP CONNECT configuration for a proxy server accessible using HTTP/1.1.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
func nw_proxy_config_create_http_connect(_ proxy_endpoint: nw_endpoint_t, _ proxy_tls_options: nw_protocol_options_t?) -> nw_proxy_config_t
```

```c
nw_proxy_config_tnw_proxy_config_create_http_connect(nw_endpoint_t proxy_endpoint, nw_protocol_options_t proxy_tls_options);
```

#### Return Value

An initialized proxy configuration object.

## Parameters

- `proxy_endpoint`: A host endpoint identifying the proxy server accessible using HTTP/1.1.
- `proxy_tls_options`: Optional TLS options to use for a TLS handshake to the relay. If no TLS options are provided, the proxy will be accessed using cleartext HTTP.

## See Also

### Creating Proxy Configurations
- [func nw_proxy_config_create_relay(nw_relay_hop_t, nw_relay_hop_t?) -> nw_proxy_config_t](./nw_proxy_config_create_relay%28_,_%29.md)
  Initializes a proxy configuration with one or two relay hops.
- [typealias nw_relay_hop_t](./nw_relay_hop_t.md)
  A single relay server you can chain together with other servers.
- [func nw_proxy_config_create_oblivious_http(nw_relay_hop_t, UnsafePointer<CChar>, UnsafePointer<UInt8>, Int) -> nw_proxy_config_t](./nw_proxy_config_create_oblivious_http%28_,_,_,_%29.md)
  Initializes an Oblivious HTTP proxy configuration using a relay and a gateway.
- [func nw_proxy_config_create_socksv5(nw_endpoint_t) -> nw_proxy_config_t](./nw_proxy_config_create_socksv5%28_%29.md)
  Initializes a SOCKSv5 proxy configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_proxy_config_create_http_connect(_:_:))*