# notify_check

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
extern uint32_t notify_check(int token, int * check);
```

#### Return Value

Returns status.

#### Discussion

Check if any notifications have been posted.

Output parameter check is set to 0 for false, 1 for true. Returns status. check is set to true the first time notify_check is called for a token. Subsequent calls set check to true when notifications have been posted for the name associated with the notification token. This routine is independent of notify_post(). That is, check will be true if an application calls notify_post() for a name and then calls notify_check() for a token associated with that name.

## Parameters

- `token`: (Input) notification token
- `check`: (Output) true/false indication

## See Also

- [notify_cancel](notify_cancel.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/darwinnotify/notify_check)*