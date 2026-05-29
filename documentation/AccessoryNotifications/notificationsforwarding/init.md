# init(_:)

**Framework**: Accessory Notifications  
**Kind**: init

Initializes a notifications-forwarding capability with a handler factory.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+

## Declaration

```swift
init(_ handlerFactory: @escaping @Sendable () -> any NotificationsForwarding.AccessoryNotificationsHandler)
```

## Parameters

- `handlerFactory`: A closure that creates and returns an [`NotificationsForwarding.AccessoryNotificationsHandler`](notificationsforwarding/accessorynotificationshandler.md) instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/notificationsforwarding/init(_:))*