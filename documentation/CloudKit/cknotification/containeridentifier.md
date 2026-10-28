# containerIdentifier

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The ID of the container with the content that triggers the notification.

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
var containerIdentifier: String? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSString * containerIdentifier;
```

## Discussion

Use this property to determine the location of the changed content.

## See Also

### Identifying the Notification
- [var notificationID: CKNotification.ID?](./notificationid.md)
  The notification’s ID.
- [CKNotification.ID](./id.md)
  An object that uniquely identifies a push notification that a container sends.
- [var notificationType: CKNotification.NotificationType](./notificationtype-swift.property.md)
  The type of event that generates the notification.
- [CKNotification.NotificationType](./notificationtype-swift.enum.md)
  Constants that indicate the type of event that generates the push notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cknotification/containeridentifier)*