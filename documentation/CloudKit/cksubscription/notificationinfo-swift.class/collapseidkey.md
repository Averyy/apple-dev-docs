# collapseIDKey

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (copy, nullable) NSString * collapseIDKey;
```

## Discussion

When CloudKit generates a push notification, it sets the notification’s `apns-collapse-id` header to this property’s value. The system uses this header to coalesce unseen notifications.

See [Sending notification requests to APNs](../../../UserNotifications/sending-notification-requests-to-apns.md) for more information about sending notifications using the Apple Push Notification service.

## See Also

### Grouping Notifications
- [var category: String?](./category.md)
  The name of the action group that corresponds to this notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksubscription/notificationinfo-swift.class/collapseidkey)*