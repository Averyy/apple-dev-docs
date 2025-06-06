# NSUserNotificationAction

**Framework**: Foundation  
**Kind**: class

An action that the user can take in response to receiving a notification.

**Availability**:
- macOS 10.10+

## Declaration

```swift
class NSUserNotificationAction
```

#### Overview

User notifications can specify one or more actions to show to the user by using the [`additionalActivationAction`](nsusernotification/additionalactivationaction.md) or [`additionalActions`](nsusernotification/additionalactions.md) properties. [`NSUserNotificationAction`](nsusernotificationaction.md) objects contain the localized title shown to the user and an identifier used to differentiate between presented actions.

## Topics

### Creating User Notification Actions
- [convenience init(identifier: String?, title: String?)](nsusernotificationaction/init(identifier:title:).md)
  Creates a user notification action with a specified identifier and title.
### Getting the Identifier and Title
- [var identifier: String?](nsusernotificationaction/identifier.md)
  The identifier for the user notification action.
- [var title: String?](nsusernotificationaction/title.md)
  The localized title shown to the user.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](nscopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSUserNotification](nsusernotification.md)
  A notification that can be scheduled for display in the notification center.
- [class NSUserNotificationCenter](nsusernotificationcenter.md)
  An object that delivers notifications from apps to the user.
- [protocol NSUserNotificationCenterDelegate](nsusernotificationcenterdelegate.md)
  An interface that enables customizing the behavior of the default notification center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsusernotificationaction)*