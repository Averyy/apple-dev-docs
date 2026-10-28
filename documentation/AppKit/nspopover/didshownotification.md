# didShowNotification

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Sent after the popover has finished animating onscreen.

**Availability**:
- macOS 10.7+

## Declaration

```swift
class let didShowNotification: NSNotification.Name
```

```c
extern NSNotificationName const NSPopoverDidShowNotification;
```

## Discussion

To observe this notification using Swift concurrency, use [`NSPopover.DidShowMessage`](./didshowmessage.md).

## See Also

### Notifications
- [class let willShowNotification: NSNotification.Name](./willshownotification.md)
  Sent before the popover is shown.
- [class let willCloseNotification: NSNotification.Name](./willclosenotification.md)
  Sent before the popover is closed.
- [class let didCloseNotification: NSNotification.Name](./didclosenotification.md)
  Sent after the popover has finished animating offscreen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopover/didshownotification)*