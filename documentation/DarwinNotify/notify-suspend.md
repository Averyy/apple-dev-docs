# notify_suspend

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
extern uint32_t notify_suspend(int token);
```

#### Return Value

Returns status.

#### Discussion

Suspend delivery of notifications for a token. Notifications for this token will be pended and coalesced, then delivered following a matching call to notify_resume. Calls to notify_suspend may be nested. Notifications remain suspended until an equal number of calls have been made to notify_resume.

## Parameters

- `token`: (Input) notification token

## See Also

- [notify_cancel](notify_cancel.md)
- [notify_check](notify_check.md)
- [notify_get_state](notify_get_state.md)
- [notify_post](notify_post.md)
- [notify_register_check](notify_register_check.md)
- [notify_register_dispatch](notify_register_dispatch.md)
  Request notification delivery to a dispatch queue.
- [notify_register_mach_port](notify_register_mach_port.md)
- [notify_register_signal](notify_register_signal.md)
- [notify_resume](notify_resume.md)
- [notify_set_state](notify_set_state.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/darwinnotify/notify_suspend)*