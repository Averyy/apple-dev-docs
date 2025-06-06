# SendTestNotificationResponse

**Framework**: App Store Server API  
**Kind**: dictionary

A response that contains the test notification token.

**Availability**:
- App Store Server API 1.5+

## Declaration

```swift
object SendTestNotificationResponse
```

#### Discussion

The [`Request a Test Notification`](request-a-test-notification.md) endpoint returns this response, which includes a [`testNotificationToken`](sendtestnotificationresponse/testnotificationtoken.md) value to reference the test associated with your request. When you request a test notification, the App Store server sends a notification with the `TEST` [`notificationType`](https://developer.apple.com/documentation/AppStoreServerNotifications/notificationType) to your server. To learn the result of the App Store server’s attempt to send the `TEST` notification, call [`Get Test Notification Status`](get-test-notification-status.md) with the [`testNotificationToken`](sendtestnotificationresponse/testnotificationtoken.md).

For more information about notifications, see [`App Store Server Notifications`](https://developer.apple.com/documentation/AppStoreServerNotifications).

## Topics

### Data types
- [type testNotificationToken](testnotificationtoken.md)
  A unique identifier for a notification test that the App Store server sends to your server.

## See Also

- [Request a Test Notification](request-a-test-notification.md)
  Ask App Store Server Notifications to send a test notification to your server.
- [Get Test Notification Status](get-test-notification-status.md)
  Check the status of the test App Store server notification sent to your server.
- [object CheckTestNotificationResponse](checktestnotificationresponse.md)
  A response that contains the contents of the App Store server’s test notification and the result from your server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/sendtestnotificationresponse)*