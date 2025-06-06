# NSPopover.Behavior

**Framework**: AppKit  
**Kind**: enum

The appearance and disappearance behavior of a popover.

**Availability**:
- macOS ?+

## Declaration

```swift
enum Behavior
```

## Topics

### Constants
- [NSPopover.Behavior.applicationDefined](nspopover/behavior-swift.enum/applicationdefined.md)
  Your application assumes responsibility for closing the popover.
- [NSPopover.Behavior.transient](nspopover/behavior-swift.enum/transient.md)
  The system will close the popover when the user interacts with a user interface element outside the popover.
- [NSPopover.Behavior.semitransient](nspopover/behavior-swift.enum/semitransient.md)
  The system will close the popover when the user interacts with user interface elements in the window containing the popover’s positioning view.
### Initializers
- [init?(rawValue: Int)](nspopover/behavior-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class let closeReasonUserInfoKey: String](nspopover/closereasonuserinfokey.md)
  The `userInfo` key containing the reason for the [`willCloseNotification`](nspopover/willclosenotification.md).
- [NSPopover.CloseReason](nspopover/closereason.md)
  Values that specify the reason for the [`willCloseNotification`](nspopover/willclosenotification.md) notification.
- [NSPopover.Appearance](nspopover/appearance-swift.enum.md)
  The set of predefined appearances for a popover.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopover/behavior-swift.enum)*