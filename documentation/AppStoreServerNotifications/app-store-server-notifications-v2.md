# App Store Server Notifications V2

**Framework**: App Store Server Notifications  
**Kind**: httpRequest

Specify your secure server’s URL in App Store Connect to receive version 2 notifications.

**Availability**:
- App Store Server Notifications 2.0+

## Mentions

- [App Store Server Notifications changelog](app-store-server-notifications-changelog.md)
- [Enabling App Store Server Notifications](enabling-app-store-server-notifications.md)
- [Receiving App Store Server Notifications](receiving-app-store-server-notifications.md)
- [Responding to App Store Server Notifications](responding-to-app-store-server-notifications.md)

#### Discussion

To receive server notifications from the App Store, provide your secure server’s HTTPS URL in App Store Connect. For more information, see [`Enabling App Store Server Notifications`](enabling-app-store-server-notifications.md). To secure your server and receive notifications, your server must support the Transport Layer Security (TLS) protocol version 1.2 or later.

Upon receiving a server notification, respond to the App Store with an HTTP status code of `200-206` if the post was successful. If the post was unsuccessful, send HTTP `50x` or `40x` to have the App Store retry the notification. For more information, see [`Responding to App Store Server Notifications`](responding-to-app-store-server-notifications.md).

## See Also

- [object responseBodyV2](responsebodyv2.md)
  The response body the App Store sends in a version 2 server notification.
- [object responseBodyV2DecodedPayload](responsebodyv2decodedpayload.md)
  A decoded payload that contains the version 2 notification data.
- [type notificationType](notificationtype.md)
  The type that describes the In-App Purchase or external purchase event for which the App Store sends the version 2 notification.
- [type subtype](subtype.md)
  A string that provides details about select notification types in version 2.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreservernotifications/app-store-server-notifications-v2)*