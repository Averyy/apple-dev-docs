# NotificationsForwarding

**Framework**: Accessory Notifications  
**Kind**: class  
**Role**: Class

A class for handling notification forwarding in your accessory’s data provider extension.

**Availability**:
- iOS 26.5+

## Declaration

```swift
final class NotificationsForwarding
```

## Overview

Implement the [`NotificationsForwarding.AccessoryNotificationsHandler`](./notificationsforwarding/accessorynotificationshandler.md) protocol in your [`AccessoryDataProvider`](../AccessoryTransportExtension/accessorydataprovider.md) extension to receive and manage system notifications that iOS forwards to your accessory.

## Topics

### Creating a notifications forwarding object
- [init(() -> any NotificationsForwarding.AccessoryNotificationsHandler)](./notificationsforwarding/init%28_%29.md)
  Initializes a notifications-forwarding capability with a handler factory.
### Managing notification sessions
- [NotificationsForwarding.Session](./notificationsforwarding/session.md)
  A session object that facilitates bidirectional communication between the system and your extension.
- [NotificationsForwarding.AccessoryNotificationsSession](./notificationsforwarding/accessorynotificationssession.md)
  A protocol that enables bidirectional communication between your extension and the system.
### Handling notification events
- [NotificationsForwarding.AccessoryNotificationsHandler](./notificationsforwarding/accessorynotificationshandler.md)
  A protocol that defines methods for handling notification life cycle events in your extension.

## Relationships

### Conforms To
- [AccessoryFeature](../AccessoryTransportExtension/accessoryfeature.md)
- [AppExtensionPoint.Capability](../ExtensionFoundation/appextensionpoint/capability.md)
- [Identifiable](../Swift/identifiable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Notification receipt
- [Receiving iOS notifications on an accessory](../AccessoryTransportExtension/receiving-ios-notifications-on-an-accessory.md)
  Create custom app extensions that manage iOS system notifications for your accessory.
- [NotificationsForwarding.AccessoryNotificationsHandler](./notificationsforwarding/accessorynotificationshandler.md)
  A protocol that defines methods for handling notification life cycle events in your extension.
- [NotificationsForwarding.Session](./notificationsforwarding/session.md)
  A session object that facilitates bidirectional communication between the system and your extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/notificationsforwarding)*