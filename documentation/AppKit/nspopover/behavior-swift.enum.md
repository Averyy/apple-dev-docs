# NSPopover.Behavior

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

The appearance and disappearance behavior of a popover.

**Availability**:
- macOS

## Declaration

```swift
enum Behavior
```

```c
enum NSPopoverBehavior : NSInteger;
```

## Topics

### Constants
- [NSPopover.Behavior.applicationDefined](./behavior-swift.enum/applicationdefined.md)
  Your application assumes responsibility for closing the popover.
- [NSPopover.Behavior.transient](./behavior-swift.enum/transient.md)
  The system will close the popover when the user interacts with a user interface element outside the popover.
- [NSPopover.Behavior.semitransient](./behavior-swift.enum/semitransient.md)
  The system will close the popover when the user interacts with user interface elements in the window containing the popover’s positioning view.
### Initializers
- [init?(rawValue: Int)](./behavior-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Constants
- [class let closeReasonUserInfoKey: String](./closereasonuserinfokey.md)
  The `userInfo` key containing the reason for the [`willCloseNotification`](./willclosenotification.md).
- [NSPopover.CloseReason](./closereason.md)
  Values that specify the reason for the [`willCloseNotification`](./willclosenotification.md) notification.
- [NSPopover.Appearance](./appearance-swift.enum.md)
  The set of predefined appearances for a popover.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopover/behavior-swift.enum)*