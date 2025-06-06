# willCloseNotification

**Framework**: AppKit  
**Kind**: property

Sent before the popover is closed.

**Availability**:
- macOS 10.7+

## Declaration

```swift
class let willCloseNotification: NSNotification.Name
```

#### Discussion

The `userInfo` key [`closeReasonUserInfoKey`](nspopover/closereasonuserinfokey.md) specifies the reason for closing. It can currently be either [`standard`](nspopover/closereason/standard.md) or [`detachToWindow`](nspopover/closereason/detachtowindow.md), although more reasons for closing may be added in the future.

## See Also

- [class let willShowNotification: NSNotification.Name](nspopover/willshownotification.md)
  Sent before the popover is shown.
- [class let didShowNotification: NSNotification.Name](nspopover/didshownotification.md)
  Sent after the popover has finished animating onscreen.
- [class let didCloseNotification: NSNotification.Name](nspopover/didclosenotification.md)
  Sent after the popover has finished animating offscreen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopover/willclosenotification)*