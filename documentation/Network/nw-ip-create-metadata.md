# nw_ip_create_metadata()

**Framework**: Network  
**Kind**: func

Initializes an IP packet configuration with default settings.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
func nw_ip_create_metadata() -> nw_protocol_metadata_t
```

## See Also

- [func nw_protocol_metadata_is_ip(nw_protocol_metadata_t) -> Bool](nw_protocol_metadata_is_ip(_:).md)
  Checks whether a metadata object represents an IP packet.
- [func nw_ip_metadata_set_ecn_flag(nw_protocol_metadata_t, nw_ip_ecn_flag_t)](nw_ip_metadata_set_ecn_flag(_:_:).md)
  Sets a specific Explicit Congestion Notification flag value to set on an IP packet.
- [func nw_ip_metadata_get_ecn_flag(nw_protocol_metadata_t) -> nw_ip_ecn_flag_t](nw_ip_metadata_get_ecn_flag(_:).md)
  Checks the Explicit Congestion Notification flag value received on an IP packet.
- [struct nw_ip_ecn_flag_t](nw_ip_ecn_flag_t.md)
  Flag values for Explicit Congestion Notifications in IP packets.
- [func nw_ip_metadata_set_service_class(nw_protocol_metadata_t, nw_service_class_t)](nw_ip_metadata_set_service_class(_:_:).md)
  Sets a specific service class to mark on an IP packet.
- [func nw_ip_metadata_get_service_class(nw_protocol_metadata_t) -> nw_service_class_t](nw_ip_metadata_get_service_class(_:).md)
  Accesses a specific service class to mark on an IP packet.
- [func nw_ip_metadata_get_receive_time(nw_protocol_metadata_t) -> UInt64](nw_ip_metadata_get_receive_time(_:).md)
  Access the time at which a packet was received, in nanoseconds, based on `CLOCK_MONOTONIC_RAW`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_ip_create_metadata())*