# otherButtonTitle

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Specifies a custom title for the close button in an alert-style notification.

**Availability**:
- macOS 10.8+ - Deprecated in 11.0

> **Deprecated**: All NSUserNotifications API should be replaced with UserNotifications.frameworks API

## Declaration

```swift
var otherButtonTitle: String { get set }
```

```objc
@property (copy) NSString * otherButtonTitle;
```

#### Discussion

This value should be localized as it is presented to the user. The string is truncated to a length appropriate for display and the property is modified to reflect the truncation.

An empty string will cause the default localized text to be used. A `nil` value is invalid.

## See Also

### Displayed Notification Buttons
- [var hasActionButton: Bool](./hasactionbutton.md)
  A Boolean value that specifies whether the notification displays an action button.
- [var actionButtonTitle: String](./actionbuttontitle.md)
  Specifies the title of the action button displayed in the notification.
- [var hasReplyButton: Bool](./hasreplybutton.md)
  A Boolean value that specifies whether the notification displays a reply button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsusernotification/otherbuttontitle)*