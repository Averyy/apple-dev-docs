# notify_cancel

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
extern uint32_t notify_cancel(int token);
```

#### Return Value

Returns status.

#### Discussion

Cancel notification and free resources associated with a notification token. Mach ports and file descriptor associated with a token are released (deallocated or closed) when all registration tokens associated with the port or file descriptor have been cancelled.

## Parameters

- `token`: (Input) notification token

## See Also

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
- [notify_suspend](notify_suspend.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/darwinnotify/notify_cancel)*