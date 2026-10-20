# NSPopover.CloseReason

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Values that specify the reason for the [`willCloseNotification`](./willclosenotification.md) notification.

**Availability**:
- macOS

## Declaration

```swift
struct CloseReason
```

```c
typedef NSString * NSPopoverCloseReasonValue;
```

## Topics

### Constants
- [static let detachToWindow: NSPopover.CloseReason](./closereason/detachtowindow.md)
  Specifies that the popover has been closed because it is being detached to a window.
- [static let standard: NSPopover.CloseReason](./closereason/standard.md)
  Specifies that the popover has been closed in a standard way.
### Initializers
- [init(rawValue: String)](./closereason/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Constants
- [NSPopover.Behavior](./behavior-swift.enum.md)
  The appearance and disappearance behavior of a popover.
- [class let closeReasonUserInfoKey: String](./closereasonuserinfokey.md)
  The `userInfo` key containing the reason for the [`willCloseNotification`](./willclosenotification.md).
- [NSPopover.Appearance](./appearance-swift.enum.md)
  The set of predefined appearances for a popover.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopover/closereason)*