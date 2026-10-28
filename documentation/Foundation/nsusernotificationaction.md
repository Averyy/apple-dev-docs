# NSUserNotificationAction

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

An action that the user can take in response to receiving a notification.

**Availability**:
- macOS 10.10+ - Deprecated in 11.0

> **Deprecated**: Use the [User Notifications](../UserNotifications/UserNotifications.md) framework instead.

## Declaration

```swift
class NSUserNotificationAction
```

```objc
@interface NSUserNotificationAction : NSObject
```

## Overview

User notifications can specify one or more actions to show to the user by using the [`additionalActivationAction`](./nsusernotification/additionalactivationaction.md) or [`additionalActions`](./nsusernotification/additionalactions.md) properties. [`NSUserNotificationAction`](./nsusernotificationaction.md) objects contain the localized title shown to the user and an identifier used to differentiate between presented actions.

## Topics

### Creating User Notification Actions
- [convenience init(identifier: String?, title: String?)](./nsusernotificationaction/init%28identifier,title%29.md)
  Creates a user notification action with a specified identifier and title.
### Getting the Identifier and Title
- [var identifier: String?](./nsusernotificationaction/identifier.md)
  The identifier for the user notification action.
- [var title: String?](./nsusernotificationaction/title.md)
  The localized title shown to the user.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](./nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### User Notifications
- [class NSUserNotification](./nsusernotification.md)
  A notification that can be scheduled for display in the notification center.
- [class NSUserNotificationCenter](./nsusernotificationcenter.md)
  An object that delivers notifications from apps to the user.
- [protocol NSUserNotificationCenterDelegate](./nsusernotificationcenterdelegate.md)
  An interface that enables customizing the behavior of the default notification center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsusernotificationaction)*