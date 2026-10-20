# didCloseNotification

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Sent after the popover has finished animating offscreen.

**Availability**:
- macOS 10.7+

## Declaration

```swift
class let didCloseNotification: NSNotification.Name
```

```c
extern NSNotificationName const NSPopoverDidCloseNotification;
```

#### Discussion

The value of the `userInfo` key [`closeReasonUserInfoKey`](./closereasonuserinfokey.md) specifies the reason for closing. It can currently be either [`standard`](./closereason/standard.md) or [`detachToWindow`](./closereason/detachtowindow.md), although more reasons for closing may be added in the future.

To observe this notification using Swift concurrency, use [`NSPopover.DidCloseMessage`](./didclosemessage.md).

## See Also

### Notifications
- [class let willShowNotification: NSNotification.Name](./willshownotification.md)
  Sent before the popover is shown.
- [class let didShowNotification: NSNotification.Name](./didshownotification.md)
  Sent after the popover has finished animating onscreen.
- [class let willCloseNotification: NSNotification.Name](./willclosenotification.md)
  Sent before the popover is closed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopover/didclosenotification)*