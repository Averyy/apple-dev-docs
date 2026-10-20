# CKNotification.NotificationType

**Framework**: CloudKit  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate the type of event that generates the push notification.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
enum NotificationType
```

```c
enum CKNotificationType : NSInteger;
```

## Topics

### Notification Types
- [CKNotification.NotificationType.query](./notificationtype-swift.enum/query.md)
  A notification that CloudKit generates from a query subscription’s predicate.
- [CKNotification.NotificationType.database](./notificationtype-swift.enum/database.md)
  A notification that CloudKit generates when the contents of a database change.
- [CKNotification.NotificationType.recordZone](./notificationtype-swift.enum/recordzone.md)
  A notification that CloudKit generates when the contents of a record zone change.
- [CKNotification.NotificationType.readNotification](./notificationtype-swift.enum/readnotification.md)
  A notification that your app marks as read.
### Initializers
- [init?(rawValue: Int)](./notificationtype-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Identifying the Notification
- [var notificationID: CKNotification.ID?](./notificationid.md)
  The notification’s ID.
- [CKNotification.ID](./id.md)
  An object that uniquely identifies a push notification that a container sends.
- [var notificationType: CKNotification.NotificationType](./notificationtype-swift.property.md)
  The type of event that generates the notification.
- [var containerIdentifier: String?](./containeridentifier.md)
  The ID of the container with the content that triggers the notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cknotification/notificationtype-swift.enum)*