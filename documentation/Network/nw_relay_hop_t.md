# nw_relay_hop_t

**Framework**: Network  
**Kind**: typealias  
**Role**: Type Alias

A single relay server you can chain together with other servers.

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
typealias nw_relay_hop_t = any OS_nw_relay_hop
```

```c
typedef NSObject<OS_nw_relay_hop> * nw_relay_hop_t;
```

#### Discussion

Relay servers are secure HTTP proxies that allow proxying TCP traffic using the `CONNECT` method and UDP traffic using the `connect-udp` protocol defined in [RFC 9298](https://www.rfc-editor.org/rfc/rfc9298.html).

## Topics

### Configuring Relay Hops
- [func nw_relay_hop_create(nw_endpoint_t?, nw_endpoint_t?, nw_protocol_options_t?) -> nw_relay_hop_t](./nw_relay_hop_create%28_,_,_%29.md)
  Creates a configuration for a secure relay accessible using HTTP/3, with an optional HTTP/2 fallback.
- [func nw_relay_hop_add_additional_http_header_field(nw_relay_hop_t, UnsafePointer<CChar>, UnsafePointer<CChar>)](./nw_relay_hop_add_additional_http_header_field%28_,_,_%29.md)
  Adds an HTTP header name and value pair to send as part of `CONNECT` requests to the relay.

## See Also

### Creating Proxy Configurations
- [func nw_proxy_config_create_relay(nw_relay_hop_t, nw_relay_hop_t?) -> nw_proxy_config_t](./nw_proxy_config_create_relay%28_,_%29.md)
  Initializes a proxy configuration with one or two relay hops.
- [func nw_proxy_config_create_oblivious_http(nw_relay_hop_t, UnsafePointer<CChar>, UnsafePointer<UInt8>, Int) -> nw_proxy_config_t](./nw_proxy_config_create_oblivious_http%28_,_,_,_%29.md)
  Initializes an Oblivious HTTP proxy configuration using a relay and a gateway.
- [func nw_proxy_config_create_http_connect(nw_endpoint_t, nw_protocol_options_t?) -> nw_proxy_config_t](./nw_proxy_config_create_http_connect%28_,_%29.md)
  Initializes a legacy HTTP CONNECT configuration for a proxy server accessible using HTTP/1.1.
- [func nw_proxy_config_create_socksv5(nw_endpoint_t) -> nw_proxy_config_t](./nw_proxy_config_create_socksv5%28_%29.md)
  Initializes a SOCKSv5 proxy configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_relay_hop_t)*