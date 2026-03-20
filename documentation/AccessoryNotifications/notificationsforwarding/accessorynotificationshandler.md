# NotificationsForwarding.AccessoryNotificationsHandler

**Framework**: Accessory Notifications  
**Kind**: protocol

A protocol that defines methods for handling notification lifecycle events in your extension.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

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
### Receiving notifications
- [func add(notification: AccessoryNotification, alertingContext: AlertingContext, alertCoordinator: any AlertCoordinating)](notificationsforwarding/accessorynotificationshandler/add(notification:alertingcontext:alertcoordinator:).md)
  Provides a new notification for display on your accessory.
### Updating notifications
- [func update(notification: AccessoryNotification)](notificationsforwarding/accessorynotificationshandler/update(notification:).md)
  Updates a notification with new content.
### Removing notifications
- [func remove(notification: AccessoryNotification)](notificationsforwarding/accessorynotificationshandler/remove(notification:).md)
  Removes a previously posted notification from your accessory.
- [func removeAllNotifications()](notificationsforwarding/accessorynotificationshandler/removeallnotifications.md)
  Removes all notifications from the user interface.

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class NotificationsForwarding](notificationsforwarding.md)
  A class for handling notification forwarding in your accessory’s data provider extension.
- [NotificationsForwarding.Session](notificationsforwarding/session.md)
  A session object that enables communication between your extension and the system.
- [NotificationsForwarding.HandlerFactory](notificationsforwarding/handlerfactory.md)
  A type alias for a factory that creates notification handlers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/notificationsforwarding/accessorynotificationshandler)*