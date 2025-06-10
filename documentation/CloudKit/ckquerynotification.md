# CKQueryNotification

**Framework**: CloudKit  
**Kind**: class

A notification that triggers when a record that matches the subscription’s predicate changes.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class CKQueryNotification
```

#### Overview

Query subscriptions execute when a record that matches the subscription’s predicate changes, for example, when the user modifies a field’s value in the record. When CloudKit registers the change, it sends push notifications to the user’s devices to inform your app about the change. You can then fetch the changes and cache them on-device. When appropriate, CloudKit excludes the device where the change originates.

You configure a subscription’s notifications by setting it’s [`notificationInfo`](cksubscription/notificationinfo-swift.property.md) property. Do this before you save it to the server. A subscription generates either high-priority or medium-priority push notifications. CloudKit delivers medium-priority notifications to your app in the background. High-priority notifications are visual and the system displays them to the user. Visual notifications need the user’s permission. For more information, see [`Asking permission to use notifications`](https://developer.apple.com/documentation/UserNotifications/asking-permission-to-use-notifications).

A subscription uses [`CKSubscription.NotificationInfo`](cksubscription/notificationinfo-swift.class.md) to configure its notifications. For background delivery, set only its [`shouldSendContentAvailable`](cksubscription/notificationinfo-swift.class/shouldsendcontentavailable.md) property to [`true`](https://developer.apple.com/documentation/swift/true). If you set any other property, CloudKit treats the notification as high-priority.

> **Note**:  To receive silent push notifications, add the Background Modes capability to your Xcode project and select the “Background fetch” and “Remote notifications” options.

Don’t rely on push notifications for changes because the system can coalesce them. CloudKit can omit data to keep the notification’s payload size under the APNs size limit. If you use [`desiredKeys`](cksubscription/notificationinfo-swift.class/desiredkeys.md) to include extra data in the payload, the server removes that first. A notification’s [`isPruned`](cknotification/ispruned.md) property is [`true`](https://developer.apple.com/documentation/swift/true) if CloudKit omits data.

Consider notifications an indication of remote changes. Use [`databaseScope`](ckdatabasenotification/databasescope.md) to determine which database contains the changed record. To fetch the changes, configure an instance of [`CKQueryOperation`](ckqueryoperation.md) to match the subscription and then execute it in the database. CloudKit returns all records that match the predicate, including the changed record. Dispose of any records you cache on-device and use the operation’s results instead.

You don’t instantiate this class. Instead, implement [`application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`](https://developer.apple.com/documentation/UIKit/UIApplicationDelegate/application(_:didReceiveRemoteNotification:fetchCompletionHandler:)) in your app delegate. Initialize [`CKNotification`](cknotification.md) with the `userInfo` dictionary that CloudKit passes to the method. This returns an instance of the appropriate subclass. Use the [`notificationType`](cknotification/notificationtype-swift.property.md) property to determine the type. Then cast to that type to access type-specific properties and methods.

## Topics

### Getting the Database Scope
- [var databaseScope: CKDatabase.Scope](ckquerynotification/databasescope.md)
  The type of database for the record zone.
### Getting the Notification Attributes
- [var queryNotificationReason: CKQueryNotification.Reason](ckquerynotification/querynotificationreason.md)
  The event that triggers the push notification.
- [CKQueryNotification.Reason](ckquerynotification/reason.md)
  Constants that indicate the event that triggers the notification.
### Getting the Record Information
- [var recordID: CKRecord.ID?](ckquerynotification/recordid.md)
  The ID of the record that CloudKit creates, updates, or deletes.
- [var recordFields: [String : Any]?](ckquerynotification/recordfields.md)
  A dictionary of fields that have changes.

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

- [class CKQuerySubscription](ckquerysubscription.md)
  A subscription that generates push notifications when CloudKit modifies records that match a predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckquerynotification)*