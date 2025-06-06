# didCloseNotification

**Framework**: AppKit  
**Kind**: property

Sent after the popover has finished animating offscreen.

**Availability**:
- macOS 10.7+

## Declaration

```swift
class let didCloseNotification: NSNotification.Name
```

#### Discussion

The value of the `userInfo` key [`closeReasonUserInfoKey`](nspopover/closereasonuserinfokey.md) specifies the reason for closing. It can currently be either [`standard`](nspopover/closereason/standard.md) or [`detachToWindow`](nspopover/closereason/detachtowindow.md), although more reasons for closing may be added in the future.

## See Also

- [class let willShowNotification: NSNotification.Name](nspopover/willshownotification.md)
  Sent before the popover is shown.
- [class let didShowNotification: NSNotification.Name](nspopover/didshownotification.md)
  Sent after the popover has finished animating onscreen.
- [class let willCloseNotification: NSNotification.Name](nspopover/willclosenotification.md)
  Sent before the popover is closed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopover/didclosenotification)*