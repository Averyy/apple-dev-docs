# subtype

**Framework**: App Store Server Notifications  
**Kind**: typealias

A string that provides details about select notification types in version 2.

**Availability**:
- App Store Server Notifications 2.0+

## Declaration

```swift
string subtype
```

## Mentions

- [App Store Server Notifications changelog](app-store-server-notifications-changelog.md)

#### Discussion

This `subtype` field is part of the [`responseBodyV2DecodedPayload`](responsebodyv2decodedpayload.md), and further describes an event of type [`notificationType`](notificationtype.md). It’s present only for specific version 2 notifications.

## See Also

- [App Store Server Notifications V2](app-store-server-notifications-v2.md)
  Specify your secure server’s URL in App Store Connect to receive version 2 notifications.
- [object responseBodyV2](responsebodyv2.md)
  The response body the App Store sends in a version 2 server notification.
- [object responseBodyV2DecodedPayload](responsebodyv2decodedpayload.md)
  A decoded payload that contains the version 2 notification data.
- [type notificationType](notificationtype.md)
  The type that describes the in-app purchase or external purchase event for which the App Store sends the version 2 notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreservernotifications/subtype)*