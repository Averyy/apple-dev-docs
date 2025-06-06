# additionalActivationAction

**Framework**: Foundation  
**Kind**: property

An additional action selected by the user.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@NSCopying
var additionalActivationAction: NSUserNotificationAction? { get }
```

#### Discussion

This property specifies an additional action selected by the user when the user notification is sent to to the [`NSUserNotificationCenterDelegate`](nsusernotificationcenterdelegate.md) method [`userNotificationCenter(_:didActivate:)`](nsusernotificationcenterdelegate/usernotificationcenter(_:didactivate:).md). The supported values are described in [`NSUserNotification.ActivationType`](nsusernotification/activationtype-swift.enum.md).

## See Also

- [var activationType: NSUserNotification.ActivationType](nsusernotification/activationtype-swift.property.md)
  Specifies what caused a user notification to occur.
- [var additionalActions: [NSUserNotificationAction]?](nsusernotification/additionalactions.md)
  The actions that can be taken on a notification in addition to the default action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsusernotification/additionalactivationaction)*