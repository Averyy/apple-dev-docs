# testNotificationToken

**Framework**: App Store Server API  
**Kind**: typealias

A unique identifier for a notification test that the App Store server sends to your server.

**Availability**:
- App Store Server API 1.5+

## Declaration

```swift
string testNotificationToken
```

#### Discussion

You receive a `testNotificationToken` when you call the [`Request a Test Notification`](request-a-test-notification.md) endpoint. Use the `testNotificationToken` to learn your server’s response to the test by calling [`Get Test Notification Status`](get-test-notification-status.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/testnotificationtoken)*