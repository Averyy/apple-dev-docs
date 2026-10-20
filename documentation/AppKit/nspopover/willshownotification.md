# willShowNotification

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Sent before the popover is shown.

**Availability**:
- macOS 10.7+

## Declaration

```swift
class let willShowNotification: NSNotification.Name
```

```c
extern NSNotificationName const NSPopoverWillShowNotification;
```

#### Discussion

To observe this notification using Swift concurrency, use [`NSPopover.WillShowMessage`](./willshowmessage.md).

## See Also

### Notifications
- [class let didShowNotification: NSNotification.Name](./didshownotification.md)
  Sent after the popover has finished animating onscreen.
- [class let willCloseNotification: NSNotification.Name](./willclosenotification.md)
  Sent before the popover is closed.
- [class let didCloseNotification: NSNotification.Name](./didclosenotification.md)
  Sent after the popover has finished animating offscreen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopover/willshownotification)*