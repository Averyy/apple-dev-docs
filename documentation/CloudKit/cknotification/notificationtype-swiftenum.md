# CKNotification.NotificationType

**Framework**: CloudKit  
**Kind**: enum

Constants that indicate the type of event that generates the push notification.

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
enum NotificationType
```

## Topics

### Notification Types
- [CKNotification.NotificationType.query](cknotification/notificationtype-swift.enum/query.md)
  A notification that CloudKit generates from a query subscription’s predicate.
- [CKNotification.NotificationType.database](cknotification/notificationtype-swift.enum/database.md)
  A notification that CloudKit generates when the contents of a database change.
- [CKNotification.NotificationType.recordZone](cknotification/notificationtype-swift.enum/recordzone.md)
  A notification that CloudKit generates when the contents of a record zone change.
- [CKNotification.NotificationType.readNotification](cknotification/notificationtype-swift.enum/readnotification.md)
  A notification that your app marks as read.
### Initializers
- [init?(rawValue: Int)](cknotification/notificationtype-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var notificationID: CKNotification.ID?](cknotification/notificationid.md)
  The notification’s ID.
- [CKNotification.ID](cknotification/id.md)
  An object that uniquely identifies a push notification that a container sends.
- [var notificationType: CKNotification.NotificationType](cknotification/notificationtype-swift.property.md)
  The type of event that generates the notification.
- [var containerIdentifier: String?](cknotification/containeridentifier.md)
  The ID of the container with the content that triggers the notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cknotification/notificationtype-swift.enum)*