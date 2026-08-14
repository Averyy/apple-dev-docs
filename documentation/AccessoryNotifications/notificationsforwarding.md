# NotificationsForwarding

**Framework**: Accessory Notifications  
**Kind**: class

A class for handling notification forwarding in your accessory’s data provider extension.

**Availability**:
- iOS 26.5+

## Declaration

```swift
final class NotificationsForwarding
```

#### Overview

Implement the [`NotificationsForwarding.AccessoryNotificationsHandler`](notificationsforwarding/accessorynotificationshandler.md) protocol in your [`AccessoryDataProvider`](https://developer.apple.com/documentation/accessorytransportextension/accessorydataprovider) extension to receive and manage system notifications that iOS forwards to your accessory.

## Topics

### Creating a notifications forwarding object
- [init(() -> any NotificationsForwarding.AccessoryNotificationsHandler)](notificationsforwarding/init(_:).md)
  Initializes a notifications-forwarding capability with a handler factory.
### Managing notification sessions
- [NotificationsForwarding.Session](notificationsforwarding/session.md)
  A session object that facilitates bidirectional communication between the system and your extension.
- [NotificationsForwarding.AccessoryNotificationsSession](notificationsforwarding/accessorynotificationssession.md)
  A protocol that enables bidirectional communication between your extension and the system.
### Handling notification events
- [NotificationsForwarding.AccessoryNotificationsHandler](notificationsforwarding/accessorynotificationshandler.md)
  A protocol that defines methods for handling notification life cycle events in your extension.

## Relationships

### Conforms To
- [AccessoryFeature](../accessorytransportextension/accessoryfeature.md)
- [AppExtensionPoint.Capability](../extensionfoundation/appextensionpoint/capability.md)
- [Identifiable](../swift/identifiable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [NotificationsForwarding.AccessoryNotificationsHandler](notificationsforwarding/accessorynotificationshandler.md)
  A protocol that defines methods for handling notification life cycle events in your extension.
- [NotificationsForwarding.Session](notificationsforwarding/session.md)
  A session object that facilitates bidirectional communication between the system and your extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/notificationsforwarding)*