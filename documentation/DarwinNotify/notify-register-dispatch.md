# notify_register_dispatch(_:_:_:_:)

**Framework**: Darwin Notify  
**Kind**: func

Request notification delivery to a dispatch queue.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func notify_register_dispatch(_ name: UnsafePointer<CChar>!, _ out_token: UnsafeMutablePointer<Int32>!, _ queue: dispatch_queue_t!, _ handler: notify_handler_t!) -> UInt32
```

#### Return Value

Returns status.

#### Discussion

When notifications are received by the process, the notify subsystem will deliver the registered Block to the target dispatch queue. Notification blocks are not re-entrant, and subsequent notification Blocks will not be delivered for the same registration until the previous Block has returned.

## Parameters

- `name`: (Input) The notification name.
- `out_token`: (Output) The registration token.
- `queue`: (Input) The dispatch queue to which the Block is submitted. The dispatch queue is retained by the notify subsystem while the notification is registered, and will be released when notification is canceled.
- `handler`: (Input) The Block to invoke on the dispatch queue in response to a notification. The notification token is passed to the Block as an argument so that the callee can modify the state of the notification or cancel the registration.

## See Also

- [func notify_cancel(Int32) -> UInt32](notify_cancel(_:).md)
- [func notify_check(Int32, UnsafeMutablePointer<Int32>!) -> UInt32](notify_check(_:_:).md)
- [func notify_get_state(Int32, UnsafeMutablePointer<UInt64>!) -> UInt32](notify_get_state(_:_:).md)
- [func notify_post(UnsafePointer<CChar>!) -> UInt32](notify_post(_:).md)
- [func notify_register_check(UnsafePointer<CChar>!, UnsafeMutablePointer<Int32>!) -> UInt32](notify_register_check(_:_:).md)
- [func notify_register_mach_port(UnsafePointer<CChar>!, UnsafeMutablePointer<mach_port_t>!, Int32, UnsafeMutablePointer<Int32>!) -> UInt32](notify_register_mach_port(_:_:_:_:).md)
- [func notify_register_signal(UnsafePointer<CChar>!, Int32, UnsafeMutablePointer<Int32>!) -> UInt32](notify_register_signal(_:_:_:).md)
- [func notify_resume(Int32) -> UInt32](notify_resume(_:).md)
- [func notify_set_state(Int32, UInt64) -> UInt32](notify_set_state(_:_:).md)
- [func notify_suspend(Int32) -> UInt32](notify_suspend(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/darwinnotify/notify_register_dispatch(_:_:_:_:))*