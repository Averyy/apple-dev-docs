# nw_connection_state_failed

**Framework**: Network  
**Kind**: var

The connection has disconnected or encountered an error.

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
var nw_connection_state_failed: nw_connection_state_t { get }
```

## See Also

- [var nw_connection_state_invalid: nw_connection_state_t](nw_connection_state_invalid.md)
  The connection is not valid.
- [var nw_connection_state_waiting: nw_connection_state_t](nw_connection_state_waiting.md)
  The connection is waiting for a network path change.
- [var nw_connection_state_preparing: nw_connection_state_t](nw_connection_state_preparing.md)
  The connection in the process of being established.
- [var nw_connection_state_ready: nw_connection_state_t](nw_connection_state_ready.md)
  The connection is established, and ready to send and receive data.
- [var nw_connection_state_cancelled: nw_connection_state_t](nw_connection_state_cancelled.md)
  The connection has been canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_connection_state_failed)*