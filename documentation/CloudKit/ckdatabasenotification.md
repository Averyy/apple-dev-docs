# CKDatabaseNotification

**Framework**: CloudKit  
**Kind**: class

A notification that triggers when the contents of a database change.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class CKDatabaseNotification
```

#### Overview

Database subscriptions execute when changes happen in any of a database’s record zones, for example, when CloudKit saves a new record. When the subscription registers a change, it sends push notifications to the user’s devices to inform your app about the change. You can then fetch the changes and cache them on-device. When appropriate, CloudKit excludes the device where the change originates.

You configure a subscription’s notifications by setting it’s [`notificationInfo`](cksubscription/notificationinfo-swift.property.md) property. Do this before you save it to the server. A subscription generates either high-priority or medium-priority push notifications. CloudKit delivers medium-priority notifications to your app in the background. High-priority notifications are visual and the system displays them to the user. Visual notifications need the user’s permission. For more information, see [`Asking permission to use notifications`](https://developer.apple.com/documentation/UserNotifications/asking-permission-to-use-notifications).

A subscription uses [`CKSubscription.NotificationInfo`](cksubscription/notificationinfo-swift.class.md) to configure its notifications. For background delivery, set only its [`shouldSendContentAvailable`](cksubscription/notificationinfo-swift.class/shouldsendcontentavailable.md) property to [`true`](https://developer.apple.com/documentation/Swift/true). If you set any other property, CloudKit treats the notification as high-priority.

> **Note**:  To receive silent push notifications, add the Background Modes capability to your Xcode project and select the “Background fetch” and “Remote notifications” options.

Don’t rely on push notifications for specific changes because the system can coalesce them. CloudKit can omit data to keep the notification’s payload size under the APNs size limit. Consider notifications an indication of remote changes. Use [`databaseScope`](ckdatabasenotification/databasescope.md) to determine which database has changes, and then [`CKFetchDatabaseChangesOperation`](ckfetchdatabasechangesoperation.md) to fetch those changes. A notification’s [`isPruned`](cknotification/ispruned.md) property is [`true`](https://developer.apple.com/documentation/Swift/true) if CloudKit omits data.

You don’t instantiate this class. Instead, implement [`application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`](https://developer.apple.com/documentation/UIKit/UIApplicationDelegate/application(_:didReceiveRemoteNotification:fetchCompletionHandler:)) in your app delegate. Initialize [`CKNotification`](cknotification.md) with the `userInfo` dictionary that CloudKit passes to the method. This returns an instance of the appropriate subclass. Use the [`notificationType`](cknotification/notificationtype-swift.property.md) property to determine the type. Then cast to that type to access type-specific properties and methods.

## Topics

### Getting the Database Scope
- [var databaseScope: CKDatabase.Scope](ckdatabasenotification/databasescope.md)
  The type of database.

## Relationships

### Inherits From
- [CKNotification](cknotification.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class CKDatabaseSubscription](ckdatabasesubscription.md)
  A subscription that generates push notifications when CloudKit modifies records in a database.
- [class CKFetchDatabaseChangesOperation](ckfetchdatabasechangesoperation.md)
  An operation that fetches database changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabasenotification)*