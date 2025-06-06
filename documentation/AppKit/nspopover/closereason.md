# NSPopover.CloseReason

**Framework**: AppKit  
**Kind**: struct

Values that specify the reason for the [`willCloseNotification`](nspopover/willclosenotification.md) notification.

**Availability**:
- macOS ?+

## Declaration

```swift
struct CloseReason
```

## Topics

### Constants
- [static let detachToWindow: NSPopover.CloseReason](nspopover/closereason/detachtowindow.md)
  Specifies that the popover has been closed because it is being detached to a window.
- [static let standard: NSPopover.CloseReason](nspopover/closereason/standard.md)
  Specifies that the popover has been closed in a standard way.
### Initializers
- [init(rawValue: String)](nspopover/closereason/init(rawvalue:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [NSPopover.Behavior](nspopover/behavior-swift.enum.md)
  The appearance and disappearance behavior of a popover.
- [class let closeReasonUserInfoKey: String](nspopover/closereasonuserinfokey.md)
  The `userInfo` key containing the reason for the [`willCloseNotification`](nspopover/willclosenotification.md).
- [NSPopover.Appearance](nspopover/appearance-swift.enum.md)
  The set of predefined appearances for a popover.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopover/closereason)*