# notificationID

**Framework**: CloudKit  
**Kind**: property

The notification’s ID.

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
@NSCopying
var notificationID: CKNotification.ID? { get }
```

#### Discussion

Use this property to differentiate notifications.

## See Also

- [CKNotification.ID](cknotification/id.md)
  An object that uniquely identifies a push notification that a container sends.
- [var notificationType: CKNotification.NotificationType](cknotification/notificationtype-swift.property.md)
  The type of event that generates the notification.
- [CKNotification.NotificationType](cknotification/notificationtype-swift.enum.md)
  Constants that indicate the type of event that generates the push notification.
- [var containerIdentifier: String?](cknotification/containeridentifier.md)
  The ID of the container with the content that triggers the notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cknotification/notificationid)*