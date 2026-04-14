# identifier

**Framework**: Accessory Notifications  
**Kind**: property

A structure that uniquely identifies the notification.

**Availability**:
- iOS 26.5+ (Beta)
- iPadOS 26.5+ (Beta)

## Declaration

```swift
let identifier: AccessoryNotification.Identifier
```

## Mentions

- [Receiving iOS notifications on an accessory](receiving-ios-notifications-on-an-accessory.md)

#### Discussion

This structure combines the source app’s bundle identifier ([`sourceIdentifier`](accessorynotification/identifier-swift.struct/sourceidentifier.md)) with an app-provided notification identifier ([`notificationIdentifier`](accessorynotification/identifier-swift.struct/notificationidentifier.md)).

## See Also

- [AccessoryNotification.Identifier](accessorynotification/identifier-swift.struct.md)
  A structure that uniquely identifies a notification.
- [let threadIdentifier: String?](accessorynotification/threadidentifier.md)
  An identifier that groups notifications that belong to the same thread.
- [let sourceName: String](accessorynotification/sourcename.md)
  A display name for the bundle that sent the notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/accessorynotification/identifier-swift.property)*