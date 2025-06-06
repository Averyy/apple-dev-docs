# activationType

**Framework**: Foundation  
**Kind**: property

Specifies what caused a user notification to occur.

**Availability**:
- macOS 10.8+

## Declaration

```swift
var activationType: NSUserNotification.ActivationType { get }
```

#### Discussion

This property specifies why the user notification was sent to to the [`NSUserNotificationCenterDelegate`](nsusernotificationcenterdelegate.md) method [`userNotificationCenter(_:didActivate:)`](nsusernotificationcenterdelegate/usernotificationcenter(_:didactivate:).md). The supported values are described in [`NSUserNotification.ActivationType`](nsusernotification/activationtype-swift.enum.md).

## See Also

- [var additionalActivationAction: NSUserNotificationAction?](nsusernotification/additionalactivationaction.md)
  An additional action selected by the user.
- [var additionalActions: [NSUserNotificationAction]?](nsusernotification/additionalactions.md)
  The actions that can be taken on a notification in addition to the default action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsusernotification/activationtype-swift.property)*