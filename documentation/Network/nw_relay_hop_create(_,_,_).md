# nw_relay_hop_create(_:_:_:)

**Framework**: Network  
**Kind**: func  
**Role**: Function

Creates a configuration for a secure relay accessible using HTTP/3, with an optional HTTP/2 fallback.

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
func nw_relay_hop_create(_ http3_relay_endpoint: nw_endpoint_t?, _ http2_relay_endpoint: nw_endpoint_t?, _ relay_tls_options: nw_protocol_options_t?) -> nw_relay_hop_t
```

```c
nw_relay_hop_tnw_relay_hop_create(nw_endpoint_t http3_relay_endpoint, nw_endpoint_t http2_relay_endpoint, nw_protocol_options_t relay_tls_options);
```

#### Return Value

An initialized relay hop object.

## Parameters

- `http3_relay_endpoint`: A URL or host endpoint identifying the relay server accessible using HTTP/3.
- `http2_relay_endpoint`: An optional URL or host endpoint identifying the relay server accessible using HTTP/2. This can be the same endpoint as `http3_relay_endpoint`.
- `relay_tls_options`: The TLS options to use for the TLS handshake to the relay.

## See Also

### Configuring Relay Hops
- [func nw_relay_hop_add_additional_http_header_field(nw_relay_hop_t, UnsafePointer<CChar>, UnsafePointer<CChar>)](./nw_relay_hop_add_additional_http_header_field%28_,_,_%29.md)
  Adds an HTTP header name and value pair to send as part of `CONNECT` requests to the relay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_relay_hop_create(_:_:_:))*