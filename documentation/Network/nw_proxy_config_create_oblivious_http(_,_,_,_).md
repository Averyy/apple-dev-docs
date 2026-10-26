# nw_proxy_config_create_oblivious_http(_:_:_:_:)

**Framework**: Network  
**Kind**: func  
**Role**: Function

Initializes an Oblivious HTTP proxy configuration using a relay and a gateway.

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
func nw_proxy_config_create_oblivious_http(_ relay: nw_relay_hop_t, _ relay_resource_path: UnsafePointer<CChar>, _ gateway_key_config: UnsafePointer<UInt8>, _ gateway_key_config_length: Int) -> nw_proxy_config_t
```

```c
nw_proxy_config_tnw_proxy_config_create_oblivious_http(nw_relay_hop_t relay, const char *relay_resource_path, const uint8_t *gateway_key_config, size_t gateway_key_config_length);
```

#### Return Value

An initialized proxy configuration object.

#### Discussion

[Oblivious HTTP](https://www.ietf.org/archive/id/draft-ietf-ohai-ohttp-08.html) provides per-message encryption to a gateway through a relay.

## Parameters

- `relay`: The Oblivious HTTP relay hop.
- `relay_resource_path`: The HTTP path to use for requests to the Oblivious HTTP relay that will forward requests to the gateway.
- `gateway_key_config`: The [key configuration](https://www.ietf.org/archive/id/draft-ietf-ohai-ohttp-08.html#name-key-configuration-encoding) for the Oblivious HTTP gateway.
- `gateway_key_config_length`: The length of the key configuration buffer in `gateway_key_config.`

## See Also

### Creating Proxy Configurations
- [func nw_proxy_config_create_relay(nw_relay_hop_t, nw_relay_hop_t?) -> nw_proxy_config_t](./nw_proxy_config_create_relay%28_,_%29.md)
  Initializes a proxy configuration with one or two relay hops.
- [typealias nw_relay_hop_t](./nw_relay_hop_t.md)
  A single relay server you can chain together with other servers.
- [func nw_proxy_config_create_http_connect(nw_endpoint_t, nw_protocol_options_t?) -> nw_proxy_config_t](./nw_proxy_config_create_http_connect%28_,_%29.md)
  Initializes a legacy HTTP CONNECT configuration for a proxy server accessible using HTTP/1.1.
- [func nw_proxy_config_create_socksv5(nw_endpoint_t) -> nw_proxy_config_t](./nw_proxy_config_create_socksv5%28_%29.md)
  Initializes a SOCKSv5 proxy configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_proxy_config_create_oblivious_http(_:_:_:_:))*