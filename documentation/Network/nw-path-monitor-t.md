# nw_path_monitor_t

**Framework**: Network  
**Kind**: typealias

An observer that you use to monitor and react to network changes.

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
typealias nw_path_monitor_t = any OS_nw_path_monitor
```

## Topics

### Creating Path Monitors
- [func nw_path_monitor_create() -> nw_path_monitor_t](nw_path_monitor_create().md)
  Initializes a path monitor to observe all available interface types.
- [func nw_path_monitor_create_with_type(nw_interface_type_t) -> nw_path_monitor_t](nw_path_monitor_create_with_type(_:).md)
  Initializes a path monitor to observe a specific interface type.
- [func nw_path_monitor_prohibit_interface_type(nw_path_monitor_t, nw_interface_type_t)](nw_path_monitor_prohibit_interface_type(_:_:).md)
  Prohibit a path monitor from using a specific interface type.
- [func nw_path_monitor_set_queue(nw_path_monitor_t, dispatch_queue_t)](nw_path_monitor_set_queue(_:_:).md)
  Sets a queue on which to deliver path events.
- [func nw_path_monitor_start(nw_path_monitor_t)](nw_path_monitor_start(_:).md)
  Starts monitoring path changes.
### Handling Path Updates
- [func nw_path_monitor_set_update_handler(nw_path_monitor_t, nw_path_monitor_update_handler_t)](nw_path_monitor_set_update_handler(_:_:).md)
  Sets a handler to receive network path updates.
- [typealias nw_path_monitor_update_handler_t](nw_path_monitor_update_handler_t.md)
  A handler that delivers network path updates.
### Canceling Path Monitors
- [func nw_path_monitor_cancel(nw_path_monitor_t)](nw_path_monitor_cancel(_:).md)
  Stops receiving network path updates.
- [func nw_path_monitor_set_cancel_handler(nw_path_monitor_t, nw_path_monitor_cancel_handler_t)](nw_path_monitor_set_cancel_handler(_:_:).md)
  Sets a handler to determine when a monitor is fully cancelled and will no longer deliver events.
- [typealias nw_path_monitor_cancel_handler_t](nw_path_monitor_cancel_handler_t.md)
  A handler that indicates when a monitor has been cancelled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_path_monitor_t)*