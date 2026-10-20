# willCloseNotification

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Sent before the popover is closed.

**Availability**:
- macOS 10.7+

## Declaration

```swift
class let willCloseNotification: NSNotification.Name
```

```c
extern NSNotificationName const NSPopoverWillCloseNotification;
```

#### Discussion

The `userInfo` key [`closeReasonUserInfoKey`](./closereasonuserinfokey.md) specifies the reason for closing. It can currently be either [`standard`](./closereason/standard.md) or [`detachToWindow`](./closereason/detachtowindow.md), although more reasons for closing may be added in the future.

To observe this notification using Swift concurrency, use [`NSPopover.WillCloseMessage`](./willclosemessage.md).

## See Also

### Notifications
- [class let willShowNotification: NSNotification.Name](./willshownotification.md)
  Sent before the popover is shown.
- [class let didShowNotification: NSNotification.Name](./didshownotification.md)
  Sent after the popover has finished animating onscreen.
- [class let didCloseNotification: NSNotification.Name](./didclosenotification.md)
  Sent after the popover has finished animating offscreen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopover/willclosenotification)*