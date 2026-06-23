# notify_register_mach_port(_:_:_:_:)

**Framework**: Darwin Notify  
**Kind**: func

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func notify_register_mach_port(_ name: UnsafePointer<CChar>!, _ notify_port: UnsafeMutablePointer<mach_port_t>!, _ flags: Int32, _ out_token: UnsafeMutablePointer<Int32>!) -> UInt32
```

#### Return Value

Returns status.

#### Discussion

Request notification by mach message.

Notifications are delivered by an empty message sent to a mach port. By default, a new port is allocated and a pointer to it is returned as the value of “notify_port”. A mach port previously returned by a call to this routine may be used for notifications if a pointer to that port is passed in to the routine and NOTIFY_REUSE is set in the flags parameter. The notification service must be able to extract send rights to the port.

Note that the kernel limits the size of the message queue for any port. If it is important that notifications should not be lost due to queue overflow, clients should service messages quickly, and be careful about using the same port for notifications for more than one name.

A notification message has an empty message body. The msgh_id field in the mach message header will have the value of the notification token. If a port is reused for multiple notification registrations, the msgh_id value may be used to determine which name generated the notification.

## Parameters

- `name`: (Input) notification name
- `notify_port`: (Input/Output) pointer to a mach port
- `out_token`: (Output) notification token

## See Also

- [func notify_cancel(Int32) -> UInt32](notify_cancel(_:).md)
- [func notify_check(Int32, UnsafeMutablePointer<Int32>!) -> UInt32](notify_check(_:_:).md)
- [func notify_get_state(Int32, UnsafeMutablePointer<UInt64>!) -> UInt32](notify_get_state(_:_:).md)
- [func notify_post(UnsafePointer<CChar>!) -> UInt32](notify_post(_:).md)
- [func notify_register_check(UnsafePointer<CChar>!, UnsafeMutablePointer<Int32>!) -> UInt32](notify_register_check(_:_:).md)
- [func notify_register_dispatch(UnsafePointer<CChar>!, UnsafeMutablePointer<Int32>!, dispatch_queue_t!, notify_handler_t!) -> UInt32](notify_register_dispatch(_:_:_:_:).md)
  Request notification delivery to a dispatch queue.
- [func notify_register_signal(UnsafePointer<CChar>!, Int32, UnsafeMutablePointer<Int32>!) -> UInt32](notify_register_signal(_:_:_:).md)
- [func notify_resume(Int32) -> UInt32](notify_resume(_:).md)
- [func notify_set_state(Int32, UInt64) -> UInt32](notify_set_state(_:_:).md)
- [func notify_suspend(Int32) -> UInt32](notify_suspend(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/darwinnotify/notify_register_mach_port(_:_:_:_:))*