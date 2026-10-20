# nw_path_monitor_t

**Framework**: Network  
**Kind**: typealias  
**Role**: Type Alias

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

```c
typedef NSObject<OS_nw_path_monitor> * nw_path_monitor_t;
```

## Topics

### Creating Path Monitors
- [func nw_path_monitor_create() -> nw_path_monitor_t](./nw_path_monitor_create%28%29.md)
  Initializes a path monitor to observe all available interface types.
- [func nw_path_monitor_create_with_type(nw_interface_type_t) -> nw_path_monitor_t](./nw_path_monitor_create_with_type%28_%29.md)
  Initializes a path monitor to observe a specific interface type.
- [func nw_path_monitor_prohibit_interface_type(nw_path_monitor_t, nw_interface_type_t)](./nw_path_monitor_prohibit_interface_type%28_,_%29.md)
  Prohibit a path monitor from using a specific interface type.
- [func nw_path_monitor_set_queue(nw_path_monitor_t, dispatch_queue_t)](./nw_path_monitor_set_queue%28_,_%29.md)
  Sets a queue on which to deliver path events.
- [func nw_path_monitor_start(nw_path_monitor_t)](./nw_path_monitor_start%28_%29.md)
  Starts monitoring path changes.
### Handling Path Updates
- [func nw_path_monitor_set_update_handler(nw_path_monitor_t, nw_path_monitor_update_handler_t)](./nw_path_monitor_set_update_handler%28_,_%29.md)
  Sets a handler to receive network path updates.
- [typealias nw_path_monitor_update_handler_t](./nw_path_monitor_update_handler_t.md)
  A handler that delivers network path updates.
### Canceling Path Monitors
- [func nw_path_monitor_cancel(nw_path_monitor_t)](./nw_path_monitor_cancel%28_%29.md)
  Stops receiving network path updates.
- [func nw_path_monitor_set_cancel_handler(nw_path_monitor_t, nw_path_monitor_cancel_handler_t)](./nw_path_monitor_set_cancel_handler%28_,_%29.md)
  Sets a handler to determine when a monitor is fully cancelled and will no longer deliver events.
- [typealias nw_path_monitor_cancel_handler_t](./nw_path_monitor_cancel_handler_t.md)
  A handler that indicates when a monitor has been cancelled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_path_monitor_t)*