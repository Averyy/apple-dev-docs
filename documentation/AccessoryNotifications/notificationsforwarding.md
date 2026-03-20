# NotificationsForwarding

**Framework**: Accessory Notifications  
**Kind**: class

A class for handling notification forwarding in your accessory’s data provider extension.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
final class NotificationsForwarding
```

#### Overview

Implement the [`NotificationsForwarding.AccessoryNotificationsHandler`](notificationsforwarding/accessorynotificationshandler.md) protocol in your [`AccessoryDataProvider`](https://developer.apple.com/documentation/AccessoryTransportExtension/AccessoryDataProvider) extension to receive and manage system notifications that iOS forwards to your accessory.

## Topics

### Managing notification sessions
- [NotificationsForwarding.Session](notificationsforwarding/session.md)
  A session object that enables communication between your extension and the system.
### Handling notification events
- [NotificationsForwarding.AccessoryNotificationsHandler](notificationsforwarding/accessorynotificationshandler.md)
  A protocol that defines methods for handling notification lifecycle events in your extension.
### Creating handlers
- [NotificationsForwarding.HandlerFactory](notificationsforwarding/handlerfactory.md)
  A type alias for a factory that creates notification handlers.

## Relationships

### Conforms To
- [AccessoryFeature](../AccessoryTransportExtension/AccessoryFeature.md)
- [AppExtensionPoint.Capability](../ExtensionFoundation/AppExtensionPoint/Capability.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [NotificationsForwarding.AccessoryNotificationsHandler](notificationsforwarding/accessorynotificationshandler.md)
  A protocol that defines methods for handling notification lifecycle events in your extension.
- [NotificationsForwarding.Session](notificationsforwarding/session.md)
  A session object that enables communication between your extension and the system.
- [NotificationsForwarding.HandlerFactory](notificationsforwarding/handlerfactory.md)
  A type alias for a factory that creates notification handlers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/notificationsforwarding)*