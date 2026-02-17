# NotificationsForwarding.Session

**Framework**: Accessory Notifications  
**Kind**: class

A session object that enables communication between your extension and the system.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)

## Declaration

```swift
final class Session
```

#### Overview

This type conforms to the [`Accessory Transport Extension`](https://developer.apple.com/documentation/AccessoryTransportExtension) framework’s [`AccessoryFeatureSession`](https://developer.apple.com/documentation/AccessoryTransportExtension/AccessoryFeatureSession) protocol.

## Relationships

### Conforms To
- [AccessoryFeatureSession](../AccessoryTransportExtension/AccessoryFeatureSession.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class NotificationsForwarding](notificationsforwarding.md)
  A class for handling notification forwarding in your accessory’s data provider extension.
- [NotificationsForwarding.AccessoryNotificationsHandler](notificationsforwarding/accessorynotificationshandler.md)
  A protocol that defines methods for handling notification lifecycle events in your extension.
- [NotificationsForwarding.HandlerFactory](notificationsforwarding/handlerfactory.md)
  A type alias for a factory that creates notification handlers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/notificationsforwarding/session)*