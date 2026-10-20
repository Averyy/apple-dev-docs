# additionalActions

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The actions that can be taken on a notification in addition to the default action.

**Availability**:
- macOS 10.10+ - Deprecated in 11.0

## Declaration

```swift
var additionalActions: [NSUserNotificationAction]? { get set }
```

```objc
@property (copy, nullable) NSArray<NSUserNotificationAction *> * additionalActions;
```

#### Discussion

This array contains `NSUserNotificationAction` objects that describe the different actions for a notification in addition to the default action described by [`actionButtonTitle`](./actionbuttontitle.md).

## See Also

### Related Documentation
- [var otherButtonTitle: String](./otherbuttontitle.md)
  Specifies a custom title for the close button in an alert-style notification.
- [var actionButtonTitle: String](./actionbuttontitle.md)
  Specifies the title of the action button displayed in the notification.
### User Notification Activation Method
- [var activationType: NSUserNotification.ActivationType](./activationtype-swift.property.md)
  Specifies what caused a user notification to occur.
- [var additionalActivationAction: NSUserNotificationAction?](./additionalactivationaction.md)
  An additional action selected by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsusernotification/additionalactions)*