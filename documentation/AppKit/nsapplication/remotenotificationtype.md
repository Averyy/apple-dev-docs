# NSApplication.RemoteNotificationType

**Framework**: AppKit  
**Kind**: struct

These constants determine whether apps launched by remote notifications display a badge.

**Availability**:
- macOS ?+

## Declaration

```swift
struct RemoteNotificationType
```

## Topics

### Interaction Types
- [static var badge: NSApplication.RemoteNotificationType](nsapplication/remotenotificationtype/badge.md)
  The app should display a badge.
- [static var sound: NSApplication.RemoteNotificationType](nsapplication/remotenotificationtype/sound.md)
  The app should play a sound.
- [static var alert: NSApplication.RemoteNotificationType](nsapplication/remotenotificationtype/alert.md)
  The app should display an alert.
### Initializers
- [init(rawValue: UInt)](nsapplication/remotenotificationtype/init(rawvalue:).md)
  Initializes a new remote notifications options structure.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [func registerForRemoteNotifications()](nsapplication/registerforremotenotifications.md)
  Register for notifications sent by Apple Push Notification service (APNs).
- [func unregisterForRemoteNotifications()](nsapplication/unregisterforremotenotifications.md)
  Unregister for notifications received from Apple Push Notification service.
- [var enabledRemoteNotificationTypes: NSApplication.RemoteNotificationType](nsapplication/enabledremotenotificationtypes.md)
  The types of push notifications that the app accepts.
- [func registerForRemoteNotifications(matching: NSApplication.RemoteNotificationType)](nsapplication/registerforremotenotifications(matching:).md)
  Register to receive notifications of the specified types from a provider through the Apple Push Notification service.
- [var isRegisteredForRemoteNotifications: Bool](nsapplication/isregisteredforremotenotifications.md)
  A Boolean value indicating whether the app is registered with Apple Push Notification service (APNs).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/remotenotificationtype)*