# notify_register_check(_:_:)

**Framework**: Darwin Notify  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func notify_register_check(_ name: UnsafePointer<CChar>!, _ out_token: UnsafeMutablePointer<Int32>!) -> UInt32
```

```c
extern uint32_t notify_register_check(const char *name, int *out_token);
```

## Return Value

Returns status.

## Discussion

Creates a registration token be used with notify_check(), but no active notifications will be delivered.

## Parameters

- `name`: (Input) notification name
- `out_token`: (Output) registration token

## See Also

### Miscellaneous
- [func notify_cancel(Int32) -> UInt32](./notify_cancel%28_%29.md)
- [func notify_check(Int32, UnsafeMutablePointer<Int32>!) -> UInt32](./notify_check%28_,_%29.md)
- [func notify_get_state(Int32, UnsafeMutablePointer<UInt64>!) -> UInt32](./notify_get_state%28_,_%29.md)
- [func notify_post(UnsafePointer<CChar>!) -> UInt32](./notify_post%28_%29.md)
- [func notify_register_dispatch(UnsafePointer<CChar>!, UnsafeMutablePointer<Int32>!, dispatch_queue_t!, notify_handler_t!) -> UInt32](./notify_register_dispatch%28_,_,_,_%29.md)
  Request notification delivery to a dispatch queue.
- [func notify_register_mach_port(UnsafePointer<CChar>!, UnsafeMutablePointer<mach_port_t>!, Int32, UnsafeMutablePointer<Int32>!) -> UInt32](./notify_register_mach_port%28_,_,_,_%29.md)
- [func notify_register_signal(UnsafePointer<CChar>!, Int32, UnsafeMutablePointer<Int32>!) -> UInt32](./notify_register_signal%28_,_,_%29.md)
- [func notify_resume(Int32) -> UInt32](./notify_resume%28_%29.md)
- [func notify_set_state(Int32, UInt64) -> UInt32](./notify_set_state%28_,_%29.md)
- [func notify_suspend(Int32) -> UInt32](./notify_suspend%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/darwinnotify/notify_register_check(_:_:))*