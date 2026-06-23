# notify_post(_:)

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
func notify_post(_ name: UnsafePointer<CChar>!) -> UInt32
```

#### Discussion

Post a notification for a name.

This is the only call that is required for a notification producer. Returns status.

## See Also

- [func notify_cancel(Int32) -> UInt32](notify_cancel(_:).md)
- [func notify_check(Int32, UnsafeMutablePointer<Int32>!) -> UInt32](notify_check(_:_:).md)
- [func notify_get_state(Int32, UnsafeMutablePointer<UInt64>!) -> UInt32](notify_get_state(_:_:).md)
- [func notify_register_check(UnsafePointer<CChar>!, UnsafeMutablePointer<Int32>!) -> UInt32](notify_register_check(_:_:).md)
- [func notify_register_dispatch(UnsafePointer<CChar>!, UnsafeMutablePointer<Int32>!, dispatch_queue_t!, notify_handler_t!) -> UInt32](notify_register_dispatch(_:_:_:_:).md)
  Request notification delivery to a dispatch queue.
- [func notify_register_mach_port(UnsafePointer<CChar>!, UnsafeMutablePointer<mach_port_t>!, Int32, UnsafeMutablePointer<Int32>!) -> UInt32](notify_register_mach_port(_:_:_:_:).md)
- [func notify_register_signal(UnsafePointer<CChar>!, Int32, UnsafeMutablePointer<Int32>!) -> UInt32](notify_register_signal(_:_:_:).md)
- [func notify_resume(Int32) -> UInt32](notify_resume(_:).md)
- [func notify_set_state(Int32, UInt64) -> UInt32](notify_set_state(_:_:).md)
- [func notify_suspend(Int32) -> UInt32](notify_suspend(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/darwinnotify/notify_post(_:))*