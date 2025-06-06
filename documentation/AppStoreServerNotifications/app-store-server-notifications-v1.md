# App Store Server Notifications V1

**Framework**: Appstoreservernotifications  
**Kind**: httpRequest

Specify your secure server’s URL in App Store Connect to receive version 1 notifications.

**Availability**:
- App Store Server Notifications 1.0+

## Mentions

- [App Store Server Notifications changelog](app-store-server-notifications-changelog.md)
- [Receiving App Store Server Notifications](receiving-app-store-server-notifications.md)

#### Discussion

To receive server notifications from the App Store, provide your secure server’s HTTPS URL in App Store Connect. For more information, see [`Enabling App Store Server Notifications`](enabling-app-store-server-notifications.md). To secure your server and receive notifications, your server must support the Transport Layer Security (TLS) protocol version 1.2 or later.

Upon receiving a server notification, respond to the App Store with an HTTP status code of `200` if the post was successful. If the post was unsuccessful, send HTTP `50x` or `40x` to have the App Store retry the notification. For more information, see [`Responding to App Store Server Notifications`](responding-to-app-store-server-notifications.md).

> **Note**:  For version 2 notifications, see [`App Store Server Notifications V2`](app-store-server-notifications-v2.md).

## See Also

- [object responseBodyV1](responsebodyv1.md)
  The response body containing JSON data that the App Store sends in a version 1 server notification.
- [type notification_type](notification_type.md)
  The type that describes the in-app purchase event for which the App Store sends the version 1 notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AppStoreServerNotifications/app-store-server-notifications-v1)*