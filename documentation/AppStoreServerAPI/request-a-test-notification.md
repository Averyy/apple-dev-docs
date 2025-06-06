# Request a Test Notification

**Framework**: App Store Server API  
**Kind**: httpRequest

Ask App Store Server Notifications to send a test notification to your server.

**Availability**:
- App Store Server API 1.5+

## Mentions

- [App Store Server API changelog](app-store-server-api-changelog.md)
- [Identifying rate limits](identifying-rate-limits.md)

#### Discussion

Use this endpoint to test if your server is receiving [`App Store Server Notifications`](https://developer.apple.com/documentation/AppStoreServerNotifications) at the URLs that you configured in App Store Connect. The [`Request a Test Notification`](request-a-test-notification.md) endpoint prompts the App Store server to send your server a notification with the `TEST` [`notificationType`](notificationtype.md). The App Store server sends the `TEST` notification to your production URL if you call this endpoint’s production URL; it sends it to your sandbox URL if you call this endpoint’s sandbox URL.

Although `TEST` is a version 2 notification, you can call this endpoint regardless of whether you configured your App Store Server Notifications URL in App Store Connect for version 1 or version 2. For more information about the configuration and enabling notifications, see [`Enter a URL for App Store server notifications`](https://developer.apple.comhttps://help.apple.com/app-store-connect/#/dev0067a330b) and [`Enabling App Store Server Notifications`](https://developer.apple.com/documentation/AppStoreServerNotifications/enabling-app-store-server-notifications).

This endpoint responds with a `testNotificationToken` in [`SendTestNotificationResponse`](sendtestnotificationresponse.md). To learn the result that the App Store server recorded when it attempted to send your server the `TEST` notification, call the [`Get Test Notification Status`](get-test-notification-status.md) endpoint with the `testNotificationToken`. Use the status information to troubleshoot your server if it’s unable to receive the `TEST` notification.

## See Also

- [Get Test Notification Status](get-test-notification-status.md)
  Check the status of the test App Store server notification sent to your server.
- [object SendTestNotificationResponse](sendtestnotificationresponse.md)
  A response that contains the test notification token.
- [object CheckTestNotificationResponse](checktestnotificationresponse.md)
  A response that contains the contents of the App Store server’s test notification and the result from your server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/request-a-test-notification)*