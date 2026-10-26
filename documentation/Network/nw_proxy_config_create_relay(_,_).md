# nw_proxy_config_create_relay(_:_:)

**Framework**: Network  
**Kind**: func  
**Role**: Function

Initializes a proxy configuration with one or two relay hops.

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
func nw_proxy_config_create_relay(_ first_hop: nw_relay_hop_t, _ second_hop: nw_relay_hop_t?) -> nw_proxy_config_t
```

```c
nw_proxy_config_tnw_proxy_config_create_relay(nw_relay_hop_t first_hop, nw_relay_hop_t second_hop);
```

#### Return Value

An initialized proxy configuration object.

## Parameters

- `first_hop`: A relay hop, which is either the first of two hops, or the only hop.
- `second_hop`: An optional second relay hop.

## See Also

### Creating Proxy Configurations
- [typealias nw_relay_hop_t](./nw_relay_hop_t.md)
  A single relay server you can chain together with other servers.
- [func nw_proxy_config_create_oblivious_http(nw_relay_hop_t, UnsafePointer<CChar>, UnsafePointer<UInt8>, Int) -> nw_proxy_config_t](./nw_proxy_config_create_oblivious_http%28_,_,_,_%29.md)
  Initializes an Oblivious HTTP proxy configuration using a relay and a gateway.
- [func nw_proxy_config_create_http_connect(nw_endpoint_t, nw_protocol_options_t?) -> nw_proxy_config_t](./nw_proxy_config_create_http_connect%28_,_%29.md)
  Initializes a legacy HTTP CONNECT configuration for a proxy server accessible using HTTP/1.1.
- [func nw_proxy_config_create_socksv5(nw_endpoint_t) -> nw_proxy_config_t](./nw_proxy_config_create_socksv5%28_%29.md)
  Initializes a SOCKSv5 proxy configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_proxy_config_create_relay(_:_:))*