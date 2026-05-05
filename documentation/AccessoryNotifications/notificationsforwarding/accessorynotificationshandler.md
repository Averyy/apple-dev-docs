# NotificationsForwarding.AccessoryNotificationsHandler

**Framework**: Accessory Notifications  
**Kind**: protocol

A protocol that defines methods for handling notification lifecycle events in your extension.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+

## Declaration

```swift
protocol AccessoryNotificationsHandler : Sendable
```

#### Overview

Implement this protocol in your app’s [`AccessoryDataProvider`](https://developer.apple.com/documentation/AccessoryTransportExtension/AccessoryDataProvider) extension to receive, update, and remove notifications forwarded to your accessory.

## Topics

### Receiving notifications
- [func addNotification(AccessoryNotification, alertingContext: AlertingContext) async throws -> Bool](notificationsforwarding/accessorynotificationshandler/addnotification(_:alertingcontext:).md)
  Provides a new notification for display on your accessory.
### Updating notifications
- [func updateNotification(AccessoryNotification)](notificationsforwarding/accessorynotificationshandler/updatenotification(_:).md)
  Updates a notification with new content.
### Removing notifications
- [func removeNotification(identifier: AccessoryNotification.Identifier)](notificationsforwarding/accessorynotificationshandler/removenotification(identifier:).md)
  Removes a previously-posted notification from your accessory.
- [func removeAllNotifications()](notificationsforwarding/accessorynotificationshandler/removeallnotifications.md)
  Removes all notifications from the user interface.
### Receiving accessory messages
- [func messageHandler(TransportMessage)](notificationsforwarding/accessorynotificationshandler/messagehandler(_:).md)
  Handles decrypted messages received from the paired accessory.
### Instance Methods
- [func didActivate(for: NotificationsForwarding.Session)](notificationsforwarding/accessorynotificationshandler/didactivate(for:).md)
  Called when a notification session has been established.
- [func didInvalidate()](notificationsforwarding/accessorynotificationshandler/didinvalidate.md)
  Called when the notification session has ended.

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class NotificationsForwarding](notificationsforwarding.md)
  A class for handling notification forwarding in your accessory’s data provider extension.
- [NotificationsForwarding.Session](notificationsforwarding/session.md)
  A session object that enables communication between the system and your extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/notificationsforwarding/accessorynotificationshandler)*