# notify_get_state(_:_:)

**Framework**: Darwin Notify  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func notify_get_state(_ token: Int32, _ state64: UnsafeMutablePointer<UInt64>!) -> UInt32
```

```c
extern uint32_t notify_get_state(int token, uint64_t *state64);
```

#### Return Value

Returns status.

#### Discussion

Get the 64-bit integer state value.

## Parameters

- `token`: (Input) notification token
- `state64`: (Output) 64-bit unsigned integer value

## See Also

### Miscellaneous
- [func notify_cancel(Int32) -> UInt32](./notify_cancel%28_%29.md)
- [func notify_check(Int32, UnsafeMutablePointer<Int32>!) -> UInt32](./notify_check%28_,_%29.md)
- [func notify_post(UnsafePointer<CChar>!) -> UInt32](./notify_post%28_%29.md)
- [func notify_register_check(UnsafePointer<CChar>!, UnsafeMutablePointer<Int32>!) -> UInt32](./notify_register_check%28_,_%29.md)
- [func notify_register_dispatch(UnsafePointer<CChar>!, UnsafeMutablePointer<Int32>!, dispatch_queue_t!, notify_handler_t!) -> UInt32](./notify_register_dispatch%28_,_,_,_%29.md)
  Request notification delivery to a dispatch queue.
- [func notify_register_mach_port(UnsafePointer<CChar>!, UnsafeMutablePointer<mach_port_t>!, Int32, UnsafeMutablePointer<Int32>!) -> UInt32](./notify_register_mach_port%28_,_,_,_%29.md)
- [func notify_register_signal(UnsafePointer<CChar>!, Int32, UnsafeMutablePointer<Int32>!) -> UInt32](./notify_register_signal%28_,_,_%29.md)
- [func notify_resume(Int32) -> UInt32](./notify_resume%28_%29.md)
- [func notify_set_state(Int32, UInt64) -> UInt32](./notify_set_state%28_,_%29.md)
- [func notify_suspend(Int32) -> UInt32](./notify_suspend%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/darwinnotify/notify_get_state(_:_:))*