# notify_get_state

**Framework**: Darwin Notify  
**Kind**: func

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
extern uint32_t notify_get_state(int token, uint64_t * state64);
```

#### Return Value

Returns status.

#### Discussion

Get the 64-bit integer state value.

## Parameters

- `token`: (Input) notification token
- `state64`: (Output) 64-bit unsigned integer value

## See Also

- [notify_cancel](notify_cancel.md)
- [notify_check](notify_check.md)
- [notify_post](notify_post.md)
- [notify_register_check](notify_register_check.md)
- [notify_register_dispatch](notify_register_dispatch.md)
  Request notification delivery to a dispatch queue.
- [notify_register_mach_port](notify_register_mach_port.md)
- [notify_register_signal](notify_register_signal.md)
- [notify_resume](notify_resume.md)
- [notify_set_state](notify_set_state.md)
- [notify_suspend](notify_suspend.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/darwinnotify/notify_get_state)*