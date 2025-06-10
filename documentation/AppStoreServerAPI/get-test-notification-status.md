# Get Test Notification Status

**Framework**: App Store Server API  
**Kind**: httpRequest

Check the status of the test App Store server notification sent to your server.

**Availability**:
- App Store Server API 1.5+

## Mentions

- [App Store Server API changelog](app-store-server-api-changelog.md)
- [Identifying rate limits](identifying-rate-limits.md)

#### Discussion

Call this endpoint using the [`testNotificationToken`](get-test-notification-status/testnotificationtoken.md) you receive when you call [`Request a Test Notification`](request-a-test-notification.md). You can check the status using the [`testNotificationToken`](get-test-notification-status/testnotificationtoken.md) for up to six months. Use the information in the [`CheckTestNotificationResponse`](checktestnotificationresponse.md) to troubleshoot your server if it’s unable to receive App Store Server Notifications successfully.

## See Also

- [Request a Test Notification](request-a-test-notification.md)
  Ask App Store Server Notifications to send a test notification to your server.
- [object SendTestNotificationResponse](sendtestnotificationresponse.md)
  A response that contains the test notification token.
- [object CheckTestNotificationResponse](checktestnotificationresponse.md)
  A response that contains the contents of the App Store server’s test notification and the result from your server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/get-test-notification-status)*