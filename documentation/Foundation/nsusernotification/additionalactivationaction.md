# additionalActivationAction

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

An additional action selected by the user.

**Availability**:
- macOS 10.10+ - Deprecated in 11.0

## Declaration

```swift
@NSCopying
var additionalActivationAction: NSUserNotificationAction? { get }
```

```objc
@property (copy, readonly, nullable) NSUserNotificationAction * additionalActivationAction;
```

#### Discussion

This property specifies an additional action selected by the user when the user notification is sent to to the [`NSUserNotificationCenterDelegate`](../nsusernotificationcenterdelegate.md) method [`userNotificationCenter(_:didActivate:)`](../nsusernotificationcenterdelegate/usernotificationcenter%28_,didactivate%29.md). The supported values are described in [`NSUserNotification.ActivationType`](./activationtype-swift.enum.md).

## See Also

### User Notification Activation Method
- [var activationType: NSUserNotification.ActivationType](./activationtype-swift.property.md)
  Specifies what caused a user notification to occur.
- [var additionalActions: [NSUserNotificationAction]?](./additionalactions.md)
  The actions that can be taken on a notification in addition to the default action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsusernotification/additionalactivationaction)*