# NotificationsForwarding.AccessoryNotificationsSession

**Framework**: Accessory Notifications  
**Kind**: protocol

**Availability**:
- iOS 26.5+ (Beta)
- iPadOS 26.5+ (Beta)

## Declaration

```swift
protocol AccessoryNotificationsSession : Sendable
```

## Topics

### Instance Methods
- [func removeNotifications(identifiers: [AccessoryNotification.Identifier]) async throws](notificationsforwarding/accessorynotificationssession/removenotifications(identifiers:).md)
  Remove notifications.
- [func removeNotifications(withIdentifiers: [String], sourceIdentifier: String) async throws](notificationsforwarding/accessorynotificationssession/removenotifications(withidentifiers:sourceidentifier:).md)
- [func send(message: AccessoryMessage) async throws](notificationsforwarding/accessorynotificationssession/send(message:).md)
  Send a message to the paired accessory.
- [func sendResponse(NotificationResponse) async throws](notificationsforwarding/accessorynotificationssession/sendresponse(_:).md)
  Send a notification response from an accessory.

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Conforming Types
- [NotificationsForwarding.Session](notificationsforwarding/session.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/notificationsforwarding/accessorynotificationssession)*