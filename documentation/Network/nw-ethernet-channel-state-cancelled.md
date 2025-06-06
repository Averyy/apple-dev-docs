# nw_ethernet_channel_state_cancelled

**Framework**: Network  
**Kind**: var

The channel has been canceled.

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
var nw_ethernet_channel_state_cancelled: nw_ethernet_channel_state_t { get }
```

## See Also

- [var nw_ethernet_channel_state_invalid: nw_ethernet_channel_state_t](nw_ethernet_channel_state_invalid.md)
  The channel is not valid.
- [var nw_ethernet_channel_state_waiting: nw_ethernet_channel_state_t](nw_ethernet_channel_state_waiting.md)
  The channel is waiting for its interface to become available.
- [var nw_ethernet_channel_state_preparing: nw_ethernet_channel_state_t](nw_ethernet_channel_state_preparing.md)
  The channel is registering with the interface.
- [var nw_ethernet_channel_state_ready: nw_ethernet_channel_state_t](nw_ethernet_channel_state_ready.md)
  The channel is able to send and receive Ethernet frames.
- [var nw_ethernet_channel_state_failed: nw_ethernet_channel_state_t](nw_ethernet_channel_state_failed.md)
  The channel has encountered a fatal error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_ethernet_channel_state_cancelled)*