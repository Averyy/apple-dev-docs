# responseBodyV1

**Framework**: App Store Server Notifications  
**Kind**: dictionary

The response body containing JSON data that the App Store sends in a version 1 server notification.

**Availability**:
- App Store Server Notifications 1.0+

## Declaration

```swift
object responseBodyV1
```

## Mentions

- [App Store Server Notifications changelog](app-store-server-notifications-changelog.md)
- [Receiving App Store Server Notifications](receiving-app-store-server-notifications.md)

#### Discussion

Use the information in the response body to react quickly to changes in your users’ subscription states. The fields available in a notification sent to your server depend on the [`notification_type`](responsebodyv1/notification_type.md), which indicates the event that triggered the notification.

## Topics

### Unified receipt object
- [object unified_receipt](unified_receipt.md)
  An object that contains information about the most recent in-app purchase transactions for the app.

## See Also

- [App Store Server Notifications V1](app-store-server-notifications-v1.md)
  Specify your secure server’s URL in App Store Connect to receive version 1 notifications.
- [type notification_type](notification_type.md)
  The type that describes the in-app purchase event for which the App Store sends the version 1 notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreservernotifications/responsebodyv1)*