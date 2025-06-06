# additionalActions

**Framework**: Foundation  
**Kind**: property

The actions that can be taken on a notification in addition to the default action.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var additionalActions: [NSUserNotificationAction]? { get set }
```

#### Discussion

This array contains `NSUserNotificationAction` objects that describe the different actions for a notification in addition to the default action described by [`actionButtonTitle`](nsusernotification/actionbuttontitle.md).

## See Also

- [var otherButtonTitle: String](nsusernotification/otherbuttontitle.md)
  Specifies a custom title for the close button in an alert-style notification.
- [var actionButtonTitle: String](nsusernotification/actionbuttontitle.md)
  Specifies the title of the action button displayed in the notification.
- [var activationType: NSUserNotification.ActivationType](nsusernotification/activationtype-swift.property.md)
  Specifies what caused a user notification to occur.
- [var additionalActivationAction: NSUserNotificationAction?](nsusernotification/additionalactivationaction.md)
  An additional action selected by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsusernotification/additionalactions)*