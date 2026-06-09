# didShowNotification

**Framework**: AppKit  
**Kind**: property

Sent after the popover has finished animating onscreen.

**Availability**:
- macOS 10.7+

## Declaration

```swift
class let didShowNotification: NSNotification.Name
```

#### Discussion

To observe this notification using Swift concurrency, use [`NSPopover.DidShowMessage`](nspopover/didshowmessage.md).

## See Also

- [class let willShowNotification: NSNotification.Name](nspopover/willshownotification.md)
  Sent before the popover is shown.
- [class let willCloseNotification: NSNotification.Name](nspopover/willclosenotification.md)
  Sent before the popover is closed.
- [class let didCloseNotification: NSNotification.Name](nspopover/didclosenotification.md)
  Sent after the popover has finished animating offscreen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopover/didshownotification)*