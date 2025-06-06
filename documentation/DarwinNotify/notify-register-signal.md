# notify_register_signal

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
extern uint32_t notify_register_signal(const char * name, int sig, int * out_token);
```

#### Return Value

Returns status.

#### Discussion

Request notification delivery by UNIX signal.

A client may request signal notification for multiple names. After a signal is delivered, the notify_check() routine may be called with each notification token to determine which name (if any) generated the signal notification.

## Parameters

- `name`: (Input) notification name
- `sig`: (Input) signal number (see signal(3))
- `out_token`: (Output) notification token

## See Also

- [notify_cancel](notify_cancel.md)
- [notify_check](notify_check.md)
- [notify_get_state](notify_get_state.md)
- [notify_post](notify_post.md)
- [notify_register_check](notify_register_check.md)
- [notify_register_dispatch](notify_register_dispatch.md)
  Request notification delivery to a dispatch queue.
- [notify_register_mach_port](notify_register_mach_port.md)
- [notify_resume](notify_resume.md)
- [notify_set_state](notify_set_state.md)
- [notify_suspend](notify_suspend.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/darwinnotify/notify_register_signal)*