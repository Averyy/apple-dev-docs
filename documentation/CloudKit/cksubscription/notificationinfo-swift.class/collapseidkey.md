# collapseIDKey

**Framework**: CloudKit  
**Kind**: property

A value that the system uses to coalesce unseen push notifications.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var collapseIDKey: String? { get set }
```

#### Discussion

When CloudKit generates a push notification, it sets the notification’s `apns-collapse-id` header to this property’s value. The system uses this header to coalesce unseen notifications.

See [`Sending notification requests to APNs`](https://developer.apple.com/documentation/UserNotifications/sending-notification-requests-to-apns) for more information about sending notifications using the Apple Push Notification service.

## See Also

- [var category: String?](cksubscription/notificationinfo-swift.class/category.md)
  The name of the action group that corresponds to this notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksubscription/notificationinfo-swift.class/collapseidkey)*