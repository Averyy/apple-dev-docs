# notify_register_dispatch

**Framework**: Darwin Notify  
**Kind**: func

Request notification delivery to a dispatch queue.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
extern uint32_t notify_register_dispatch(const char * name, int * out_token, dispatch_queue_t queue, notify_handler_thandler);
```

#### Return Value

Returns status.

#### Discussion

When notifications are received by the process, the notify subsystem will deliver the registered Block to the target dispatch queue. Notification blocks are not re-entrant, and subsequent notification Blocks will not be delivered for the same registration until the previous Block has returned.

## Parameters

- `name`: (Input) The notification name.
- `out_token`: (Output) The registration token.
- `queue`: (Input) The dispatch queue to which the Block is submitted. The dispatch queue is retained by the notify subsystem while the notification is registered, and will be released when notification is canceled.
- `handler`: (Input) The Block to invoke on the dispatch queue in response to a notification. The notification token is passed to the Block as an argument so that the callee can modify the state of the notification or cancel the registration.

## See Also

- [notify_cancel](notify_cancel.md)
- [notify_check](notify_check.md)
- [notify_get_state](notify_get_state.md)
- [notify_post](notify_post.md)
- [notify_register_check](notify_register_check.md)
- [notify_register_mach_port](notify_register_mach_port.md)
- [notify_register_signal](notify_register_signal.md)
- [notify_resume](notify_resume.md)
- [notify_set_state](notify_set_state.md)
- [notify_suspend](notify_suspend.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/darwinnotify/notify_register_dispatch)*