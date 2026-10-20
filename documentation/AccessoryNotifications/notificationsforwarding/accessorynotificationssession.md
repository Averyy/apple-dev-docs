# NotificationsForwarding.AccessoryNotificationsSession

**Framework**: Accessory Notifications  
**Kind**: protocol  
**Role**: Protocol

A protocol that enables bidirectional communication between your extension and the system.

**Availability**:
- iOS 26.5+

## Declaration

```swift
protocol AccessoryNotificationsSession : Sendable
```

#### Overview

Use the session object provided to [`didActivate(for:)`](./accessorynotificationshandler/didactivate%28for%29.md) to send messages to your accessory and communicate notification responses back to the system.

## Topics

### Sending messages to accessory
- [func send(message: AccessoryMessage) async throws](./accessorynotificationssession/send%28message%29.md)
  Sends a message to the paired accessory.
### Communicating responses
- [func sendResponse(NotificationResponse) async throws](./accessorynotificationssession/sendresponse%28_%29.md)
  Sends a notification response from the accessory to the system.
### Removing notifications
- [func removeNotifications(identifiers: [AccessoryNotification.Identifier]) async throws](./accessorynotificationssession/removenotifications%28identifiers%29.md)
  Removes the identified notifications.
- [func removeNotifications(withIdentifiers: [String], sourceIdentifier: String) async throws](./accessorynotificationssession/removenotifications%28withidentifiers,sourceidentifier%29.md)
  Removes notifications using primitive identifier components.

## Relationships

### Inherits From
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
### Conforming Types
- [NotificationsForwarding.Session](./session.md)

## See Also

### Managing notification sessions
- [NotificationsForwarding.Session](./session.md)
  A session object that facilitates bidirectional communication between the system and your extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/notificationsforwarding/accessorynotificationssession)*