# identifier

**Framework**: Accessory Notifications  
**Kind**: property  
**Role**: Instance Property

A structure that uniquely identifies the notification.

**Availability**:
- iOS 26.5+

## Declaration

```swift
let identifier: AccessoryNotification.Identifier
```

#### Discussion

This structure combines the source app’s bundle identifier ([`sourceIdentifier`](./identifier-swift.struct/sourceidentifier.md)) with an app-provided notification identifier ([`notificationIdentifier`](./identifier-swift.struct/notificationidentifier.md)).

## See Also

### Identifying and grouping notifications
- [AccessoryNotification.Identifier](./identifier-swift.struct.md)
  A structure that uniquely identifies a notification.
- [let threadIdentifier: String?](./threadidentifier.md)
  An identifier that groups notifications that belong to the same thread.
- [let sourceName: String](./sourcename.md)
  A display name for the bundle that sent the notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/accessorynotification/identifier-swift.property)*