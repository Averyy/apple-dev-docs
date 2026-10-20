# NotificationsForwarding.AccessoryNotificationsHandler

**Framework**: Accessory Notifications  
**Kind**: protocol  
**Role**: Protocol

A protocol that defines methods for handling notification life cycle events in your extension.

**Availability**:
- iOS 26.5+

## Declaration

```swift
protocol AccessoryNotificationsHandler : Sendable
```

#### Overview

Implement this protocol in your app’s [`didActivate(for:)`](./accessorynotificationshandler/didactivate%28for%29.md) extension to receive, update, and remove notifications forwarded to your accessory.

## Topics

### Managing the session life cycle
- [func didActivate(for: NotificationsForwarding.Session)](./accessorynotificationshandler/didactivate%28for%29.md)
  Establishes a notification session for communication with the system.
- [func didInvalidate()](./accessorynotificationshandler/didinvalidate%28%29.md)
  Handles notification session termination.
### Receiving notifications
- [func addNotification(AccessoryNotification, alertingContext: AlertingContext) async throws -> Bool](./accessorynotificationshandler/addnotification%28_,alertingcontext%29.md)
  Provides a new notification for display on your accessory.
### Updating notifications
- [func updateNotification(AccessoryNotification)](./accessorynotificationshandler/updatenotification%28_%29.md)
  Updates a notification with new content.
### Removing notifications
- [func removeNotification(identifier: AccessoryNotification.Identifier)](./accessorynotificationshandler/removenotification%28identifier%29.md)
  Removes a previously-posted notification from your accessory.
- [func removeAllNotifications()](./accessorynotificationshandler/removeallnotifications%28%29.md)
  Removes all notifications from the user interface.
### Receiving accessory messages
- [func messageHandler(TransportMessage)](./accessorynotificationshandler/messagehandler%28_%29.md)
  Handles decrypted messages received from the paired accessory.

## Relationships

### Inherits From
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Notification receipt
- [Receiving iOS notifications on an accessory](../../AccessoryTransportExtension/receiving-ios-notifications-on-an-accessory.md)
  Create custom app extensions that manage iOS system notifications for your accessory.
- [class NotificationsForwarding](../notificationsforwarding.md)
  A class for handling notification forwarding in your accessory’s data provider extension.
- [NotificationsForwarding.Session](./session.md)
  A session object that facilitates bidirectional communication between the system and your extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/notificationsforwarding/accessorynotificationshandler)*