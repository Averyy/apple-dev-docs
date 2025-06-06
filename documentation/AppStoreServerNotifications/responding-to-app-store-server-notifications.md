# Responding to App Store Server Notifications

**Framework**: Appstoreservernotifications

Send HTTP status codes to indicate the success of a notification post.

#### Overview

When you set up the endpoints on your server to receive notifications, configure your server to send a response. Use HTTP status codes to indicate whether the App Store server notification post succeeded:

- Send HTTP `200`, or any HTTP code between `200` and `206`, if the post was successful.
- Send HTTP `50x` or `40x` to have the App Store retry the notification, if the post didn’t succeed.

The system considers all other HTTP codes an unsuccessful post. Your server isn’t required to return a data value.

If the App Store server doesn’t receive a success response from your server after the initial notification attempt, it retries as follows:

- For version 2 notifications, it retries five times, at 1, 12, 24, 48, and 72 hours after the previous attempt.
- For version 1 notifications, it retries three times, at 6, 24, and 48 hours after the previous attempt.

> **Note**:  Retry notifications are available only in the production environment. In the sandbox environment, the App Store server attempts to send the notification one time.

##### Recover From Server Outages

If your server misses notifications due to an outage, you can always get up-to-date transaction information by calling [`App Store Server API`](https://developer.apple.com/documentation/AppStoreServerAPI) endpoints including [`Get Transaction History`](https://developer.apple.com/documentation/AppStoreServerAPI/Get-Transaction-History) and [`Get All Subscription Statuses`](https://developer.apple.com/documentation/AppStoreServerAPI/Get-All-Subscription-Statuses).

If you use version 2 notifications ([`App Store Server Notifications V2`](app-store-server-notifications-v2.md)), you can recover missed notifications by calling [`Get Notification History`](https://developer.apple.com/documentation/AppStoreServerAPI/Get-Notification-History). You can also test whether your server is receiving and responding to version 2 notifications correctly by calling the [`Request a Test Notification`](https://developer.apple.com/documentation/AppStoreServerAPI/Request-a-Test-Notification) endpoint.

## See Also

- [Enabling App Store Server Notifications](enabling-app-store-server-notifications.md)
  Configure your server and provide an HTTPS URL to receive notifications about in-app purchase events and unreported external purchase tokens.
- [Receiving App Store Server Notifications](receiving-app-store-server-notifications.md)
  Implement server-side code to receive and parse notification posts.
- [App Store Server Notifications changelog](app-store-server-notifications-changelog.md)
  Learn about changes to the App Store Server Notifications service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AppStoreServerNotifications/responding-to-app-store-server-notifications)*