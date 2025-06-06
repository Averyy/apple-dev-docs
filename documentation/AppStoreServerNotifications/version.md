# version

**Framework**: App Store Server Notifications  
**Kind**: typealias

A string that indicates the notification’s App Store Server Notifications version number.

**Availability**:
- App Store Server Notifications 2.5+

## Declaration

```swift
string version
```

#### Discussion

The version string is `“2.0”`. It’s present in [`responseBodyV2DecodedPayload`](responsebodyv2decodedpayload.md) for version 2 notifications.

For more information about App Store Server Notification changes, see [`App Store Server Notifications changelog`](app-store-server-notifications-changelog.md).

## See Also

- [type notificationType](notificationtype.md)
  The type that describes the in-app purchase or external purchase event for which the App Store sends the version 2 notification.
- [type subtype](subtype.md)
  A string that provides details about select notification types in version 2.
- [type signedDate](signeddate.md)
  The UNIX time, in milliseconds, that the App Store signed the JSON Web Signature data.
- [type notificationUUID](notificationuuid.md)
  A unique identifier for the notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreservernotifications/version)*