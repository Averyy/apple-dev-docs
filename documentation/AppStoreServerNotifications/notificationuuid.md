# notificationUUID

**Framework**: App Store Server Notifications  
**Kind**: typealias

A unique identifier for the notification.

**Availability**:
- App Store Server Notifications 2.0+

## Declaration

```swift
string notificationUUID
```

#### Discussion

The App Store server assigns a unique identifer to each notification it sends. Use this value to identify, and ignore, duplicate notifications.

## See Also

- [type notificationType](notificationtype.md)
  The type that describes the In-App Purchase or external purchase event for which the App Store sends the version 2 notification.
- [type subtype](subtype.md)
  A string that provides details about select notification types in version 2.
- [type version](version.md)
  A string that indicates the notification’s App Store Server Notifications version number.
- [type signedDate](signeddate.md)
  The UNIX time, in milliseconds, that the App Store signed the JSON Web Signature data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreservernotifications/notificationuuid)*