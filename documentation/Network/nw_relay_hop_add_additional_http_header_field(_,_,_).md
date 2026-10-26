# nw_relay_hop_add_additional_http_header_field(_:_:_:)

**Framework**: Network  
**Kind**: func  
**Role**: Function

Adds an HTTP header name and value pair to send as part of `CONNECT` requests to the relay.

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
func nw_relay_hop_add_additional_http_header_field(_ relay_hop: nw_relay_hop_t, _ field_name: UnsafePointer<CChar>, _ field_value: UnsafePointer<CChar>)
```

```c
void nw_relay_hop_add_additional_http_header_field(nw_relay_hop_t relay_hop, const char *field_name, const char *field_value);
```

## Parameters

- `relay_hop`: The relay hop to modify.
- `field_name`: The HTTP header name.
- `field_value`: The HTTP header value.

## See Also

### Configuring Relay Hops
- [func nw_relay_hop_create(nw_endpoint_t?, nw_endpoint_t?, nw_protocol_options_t?) -> nw_relay_hop_t](./nw_relay_hop_create%28_,_,_%29.md)
  Creates a configuration for a secure relay accessible using HTTP/3, with an optional HTTP/2 fallback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_relay_hop_add_additional_http_header_field(_:_:_:))*