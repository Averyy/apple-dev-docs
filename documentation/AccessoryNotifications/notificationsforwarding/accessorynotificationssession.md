# NotificationsForwarding.AccessoryNotificationsSession

**Framework**: Accessory Notifications  
**Kind**: protocol

A protocol that enables communication between your extension and the system.

**Availability**:
- iOS 26.5+ (Beta)
- iPadOS 26.5+ (Beta)

## Declaration

```swift
protocol AccessoryNotificationsSession : Sendable
```

#### Overview

Use the session object provided to `NotificationsForwarding/AccessoryNotificationsHandler/activate(for:)` to send messages to your accessory and communicate notification responses back to the system.

## Topics

### Sending messages to accessory
- [func send(message: AccessoryMessage) async throws](notificationsforwarding/accessorynotificationssession/send(message:).md)
  Sends a message to the paired accessory.
### Communicating responses
- [func sendResponse(NotificationResponse) async throws](notificationsforwarding/accessorynotificationssession/sendresponse(_:).md)
  Sends a notification response from the accessory to the system.
### Removing notifications
- [func removeNotifications(identifiers: [AccessoryNotification.Identifier]) async throws](notificationsforwarding/accessorynotificationssession/removenotifications(identifiers:).md)
  Removes the identified notifications.
- [func removeNotifications(withIdentifiers: [String], sourceIdentifier: String) async throws](notificationsforwarding/accessorynotificationssession/removenotifications(withidentifiers:sourceidentifier:).md)
  Removes notifications using primitive identifier components.

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Conforming Types
- [NotificationsForwarding.Session](notificationsforwarding/session.md)

## See Also

- [NotificationsForwarding.Session](notificationsforwarding/session.md)
  A session object that enables communication between the system and your extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/notificationsforwarding/accessorynotificationssession)*