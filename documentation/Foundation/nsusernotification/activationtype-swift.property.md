# activationType

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Specifies what caused a user notification to occur.

**Availability**:
- macOS 10.8+ - Deprecated in 11.0

> **Deprecated**: All NSUserNotifications API should be replaced with UserNotifications.frameworks API

## Declaration

```swift
var activationType: NSUserNotification.ActivationType { get }
```

```objc
@property (readonly) NSUserNotificationActivationType activationType;
```

#### Discussion

This property specifies why the user notification was sent to to the [`NSUserNotificationCenterDelegate`](../nsusernotificationcenterdelegate.md) method [`userNotificationCenter(_:didActivate:)`](../nsusernotificationcenterdelegate/usernotificationcenter%28_,didactivate%29.md). The supported values are described in [`NSUserNotification.ActivationType`](./activationtype-swift.enum.md).

## See Also

### User Notification Activation Method
- [var additionalActivationAction: NSUserNotificationAction?](./additionalactivationaction.md)
  An additional action selected by the user.
- [var additionalActions: [NSUserNotificationAction]?](./additionalactions.md)
  The actions that can be taken on a notification in addition to the default action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsusernotification/activationtype-swift.property)*