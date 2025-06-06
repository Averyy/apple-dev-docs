# notificationType

**Framework**: CloudKit  
**Kind**: property

The type of event that generates the notification.

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
var notificationType: CKNotification.NotificationType { get }
```

#### Discussion

Different notification types correspond to different subclasses of `CKNotification`, so you can use the value in this property to determine how to handle the notification data.

## See Also

- [var notificationID: CKNotification.ID?](cknotification/notificationid.md)
  The notification’s ID.
- [CKNotification.ID](cknotification/id.md)
  An object that uniquely identifies a push notification that a container sends.
- [CKNotification.NotificationType](cknotification/notificationtype-swift.enum.md)
  Constants that indicate the type of event that generates the push notification.
- [var containerIdentifier: String?](cknotification/containeridentifier.md)
  The ID of the container with the content that triggers the notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cknotification/notificationtype-swift.property)*