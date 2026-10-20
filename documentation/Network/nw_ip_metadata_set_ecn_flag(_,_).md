# nw_ip_metadata_set_ecn_flag(_:_:)

**Framework**: Network  
**Kind**: func  
**Role**: Function

Sets a specific Explicit Congestion Notification flag value to set on an IP packet.

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
func nw_ip_metadata_set_ecn_flag(_ metadata: nw_protocol_metadata_t, _ ecn_flag: nw_ip_ecn_flag_t)
```

```c
void nw_ip_metadata_set_ecn_flag(nw_protocol_metadata_t metadata, nw_ip_ecn_flag_t ecn_flag);
```

## See Also

### Handling IP Packets
- [func nw_ip_create_metadata() -> nw_protocol_metadata_t](./nw_ip_create_metadata%28%29.md)
  Initializes an IP packet configuration with default settings.
- [func nw_protocol_metadata_is_ip(nw_protocol_metadata_t) -> Bool](./nw_protocol_metadata_is_ip%28_%29.md)
  Checks whether a metadata object represents an IP packet.
- [func nw_ip_metadata_get_ecn_flag(nw_protocol_metadata_t) -> nw_ip_ecn_flag_t](./nw_ip_metadata_get_ecn_flag%28_%29.md)
  Checks the Explicit Congestion Notification flag value received on an IP packet.
- [struct nw_ip_ecn_flag_t](./nw_ip_ecn_flag_t.md)
  Flag values for Explicit Congestion Notifications in IP packets.
- [func nw_ip_metadata_set_service_class(nw_protocol_metadata_t, nw_service_class_t)](./nw_ip_metadata_set_service_class%28_,_%29.md)
  Sets a specific service class to mark on an IP packet.
- [func nw_ip_metadata_get_service_class(nw_protocol_metadata_t) -> nw_service_class_t](./nw_ip_metadata_get_service_class%28_%29.md)
  Accesses a specific service class to mark on an IP packet.
- [func nw_ip_metadata_get_receive_time(nw_protocol_metadata_t) -> UInt64](./nw_ip_metadata_get_receive_time%28_%29.md)
  Access the time at which a packet was received, in nanoseconds, based on `CLOCK_MONOTONIC_RAW`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_ip_metadata_set_ecn_flag(_:_:))*