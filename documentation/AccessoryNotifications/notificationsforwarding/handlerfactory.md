# NotificationsForwarding.HandlerFactory

**Framework**: Accessory Notifications  
**Kind**: typealias

A type alias for a factory that creates notification handlers.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)

## Declaration

```swift
typealias HandlerFactory = @Sendable () -> any NotificationsForwarding.AccessoryNotificationsHandler
```

## See Also

- [class NotificationsForwarding](notificationsforwarding.md)
  A class for handling notification forwarding in your accessory’s data provider extension.
- [NotificationsForwarding.AccessoryNotificationsHandler](notificationsforwarding/accessorynotificationshandler.md)
  A protocol that defines methods for handling notification lifecycle events in your extension.
- [NotificationsForwarding.Session](notificationsforwarding/session.md)
  A session object that enables communication between your extension and the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/notificationsforwarding/handlerfactory)*