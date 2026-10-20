# nw_framer_mark_ready(_:)

**Framework**: Network  
**Kind**: func  
**Role**: Function

Indicates to a connection that your protocol’s handshake is complete.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func nw_framer_mark_ready(_ framer: nw_framer_t)
```

```c
void nw_framer_mark_ready(nw_framer_t framer);
```

## See Also

### Related Documentation
- [var nw_framer_start_result_will_mark_ready: nw_framer_start_result_t](./nw_framer_start_result_will_mark_ready.md)
  The protocol will perform a handshake, preventing the overall connection from becoming ready until [`nw_framer_mark_ready(_:)`](./nw_framer_mark_ready%28_%29.md) is called.
### Managing Instance Lifetime
- [func nw_framer_mark_failed_with_error(nw_framer_t, Int32)](./nw_framer_mark_failed_with_error%28_,_%29.md)
  Indicates to a connection that your protocol has encountered an error, or has gracefully closed.
- [func nw_framer_prepend_application_protocol(nw_framer_t, nw_protocol_options_t) -> Bool](./nw_framer_prepend_application_protocol%28_,_%29.md)
  Dynamically adds another protocol that will run above your protocol after your protocol calls [`nw_framer_mark_ready(_:)`](./nw_framer_mark_ready%28_%29.md).
- [func nw_framer_set_stop_handler(nw_framer_t, nw_framer_stop_handler_t)](./nw_framer_set_stop_handler%28_,_%29.md)
  Sets a block to handle when the connection is being closed.
- [typealias nw_framer_stop_handler_t](./nw_framer_stop_handler_t.md)
  A handler that requests that your protocol send any final messages to close the connection.
- [func nw_framer_set_cleanup_handler(nw_framer_t, nw_framer_cleanup_handler_t)](./nw_framer_set_cleanup_handler%28_,_%29.md)
  Sets a block to handle the final cleanup of allocations made by your protocol instance.
- [typealias nw_framer_cleanup_handler_t](./nw_framer_cleanup_handler_t.md)
  A handler that tells your protocol to clean up all allocations before being deallocated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_framer_mark_ready(_:))*