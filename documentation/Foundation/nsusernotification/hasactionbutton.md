# hasActionButton

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that specifies whether the notification displays an action button.

**Availability**:
- macOS 10.8+ - Deprecated in 11.0

> **Deprecated**: All NSUserNotifications API should be replaced with UserNotifications.frameworks API

## Declaration

```swift
var hasActionButton: Bool { get set }
```

```objc
@property BOOL hasActionButton;
```

#### Discussion

Set to [`false`](../../Swift/false.md) if the notification has no action button. This is the case for notifications that are purely for information and have no user action. The default value is [`true`](../../Swift/true.md).

## See Also

### Displayed Notification Buttons
- [var actionButtonTitle: String](./actionbuttontitle.md)
  Specifies the title of the action button displayed in the notification.
- [var otherButtonTitle: String](./otherbuttontitle.md)
  Specifies a custom title for the close button in an alert-style notification.
- [var hasReplyButton: Bool](./hasreplybutton.md)
  A Boolean value that specifies whether the notification displays a reply button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsusernotification/hasactionbutton)*