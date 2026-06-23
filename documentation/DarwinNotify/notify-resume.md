# notify_resume(_:)

**Framework**: Darwin Notify  
**Kind**: func

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func notify_resume(_ token: Int32) -> UInt32
```

#### Return Value

Returns status.

#### Discussion

Removes one level of suspension for a token previously suspended by a call to notify_suspend. Notifications will resume when a matching call to notify_resume is made for each previous call to notify_suspend. Notifications posted while a token is suspended are coalesced into a single notification sent following a resumption.

## Parameters

- `token`: (Input) notification token

## See Also

- [func notify_cancel(Int32) -> UInt32](notify_cancel(_:).md)
- [func notify_check(Int32, UnsafeMutablePointer<Int32>!) -> UInt32](notify_check(_:_:).md)
- [func notify_get_state(Int32, UnsafeMutablePointer<UInt64>!) -> UInt32](notify_get_state(_:_:).md)
- [func notify_post(UnsafePointer<CChar>!) -> UInt32](notify_post(_:).md)
- [func notify_register_check(UnsafePointer<CChar>!, UnsafeMutablePointer<Int32>!) -> UInt32](notify_register_check(_:_:).md)
- [func notify_register_dispatch(UnsafePointer<CChar>!, UnsafeMutablePointer<Int32>!, dispatch_queue_t!, notify_handler_t!) -> UInt32](notify_register_dispatch(_:_:_:_:).md)
  Request notification delivery to a dispatch queue.
- [func notify_register_mach_port(UnsafePointer<CChar>!, UnsafeMutablePointer<mach_port_t>!, Int32, UnsafeMutablePointer<Int32>!) -> UInt32](notify_register_mach_port(_:_:_:_:).md)
- [func notify_register_signal(UnsafePointer<CChar>!, Int32, UnsafeMutablePointer<Int32>!) -> UInt32](notify_register_signal(_:_:_:).md)
- [func notify_set_state(Int32, UInt64) -> UInt32](notify_set_state(_:_:).md)
- [func notify_suspend(Int32) -> UInt32](notify_suspend(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/darwinnotify/notify_resume(_:))*