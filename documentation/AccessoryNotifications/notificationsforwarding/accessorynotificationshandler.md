# NotificationsForwarding.AccessoryNotificationsHandler

**Framework**: Accessory Notifications  
**Kind**: protocol

A protocol that defines methods for handling notification lifecycle events in your extension.

**Availability**:
- iOS 26.5+ (Beta)
- iPadOS 26.5+ (Beta)

## Declaration

```swift
protocol AccessoryNotificationsHandler : Sendable
```

## Mentions

- [Receiving iOS notifications on an accessory](receiving-ios-notifications-on-an-accessory.md)

#### Overview

Implement this protocol in your app’s [`AccessoryDataProvider`](https://developer.apple.com/documentation/AccessoryTransportExtension/AccessoryDataProvider) extension to receive, update, and remove notifications forwarded to your accessory.

## Topics

### Managing the session lifecycle
- [func activate(for: NotificationsForwarding.Session)](notificationsforwarding/accessorynotificationshandler/activate(for:).md)
  Establishes a notification session for communication between the extension and the system.
### Removing notifications
- [func removeAllNotifications()](notificationsforwarding/accessorynotificationshandler/removeallnotifications.md)
  Removes all notifications from the user interface.
### Instance Methods
- [func addNotification(AccessoryNotification, alertingContext: AlertingContext) async throws -> Bool](notificationsforwarding/accessorynotificationshandler/addnotification(_:alertingcontext:).md)
  Called when a notification has been added.
- [func messageHandler(TransportMessage)](notificationsforwarding/accessorynotificationshandler/messagehandler(_:).md)
  Called when a message from the paired accessory has been received and decrypted.
- [func removeNotification(identifier: AccessoryNotification.Identifier)](notificationsforwarding/accessorynotificationshandler/removenotification(identifier:).md)
  Called to indicate that a notification that has been posted should be removed.
- [func updateNotification(AccessoryNotification)](notificationsforwarding/accessorynotificationshandler/updatenotification(_:).md)
  Called when a notification has been updated. Accessories should not alert for a updated notification.

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class NotificationsForwarding](notificationsforwarding.md)
  A class for handling notification forwarding in your accessory’s data provider extension.
- [NotificationsForwarding.Session](notificationsforwarding/session.md)
  A session object that enables communication between your extension and the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/notificationsforwarding/accessorynotificationshandler)*