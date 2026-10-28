# actionButtonTitle

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Specifies the title of the action button displayed in the notification.

**Availability**:
- macOS 10.8+ - Deprecated in 11.0

> **Deprecated**: All NSUserNotifications API should be replaced with UserNotifications.frameworks API

## Declaration

```swift
var actionButtonTitle: String { get set }
```

```objc
@property (copy) NSString * actionButtonTitle;
```

## Discussion

This value should be localized as it is presented to the user. The string is truncated to a length appropriate for display and the property is modified to reflect the truncation.

## See Also

### Displayed Notification Buttons
- [var hasActionButton: Bool](./hasactionbutton.md)
  A Boolean value that specifies whether the notification displays an action button.
- [var otherButtonTitle: String](./otherbuttontitle.md)
  Specifies a custom title for the close button in an alert-style notification.
- [var hasReplyButton: Bool](./hasreplybutton.md)
  A Boolean value that specifies whether the notification displays a reply button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsusernotification/actionbuttontitle)*