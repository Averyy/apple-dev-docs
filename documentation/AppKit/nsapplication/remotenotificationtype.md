# NSApplication.RemoteNotificationType

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

These constants determine whether apps launched by remote notifications display a badge.

**Availability**:
- macOS

## Declaration

```swift
struct RemoteNotificationType
```

```c
enum NSRemoteNotificationType : NSUInteger;
```

## Topics

### Interaction Types
- [static var badge: NSApplication.RemoteNotificationType](./remotenotificationtype/badge.md)
  The app should display a badge.
- [static var sound: NSApplication.RemoteNotificationType](./remotenotificationtype/sound.md)
  The app should play a sound.
- [static var alert: NSApplication.RemoteNotificationType](./remotenotificationtype/alert.md)
  The app should display an alert.
### Initializers
- [init(rawValue: UInt)](./remotenotificationtype/init%28rawvalue%29.md)
  Initializes a new remote notifications options structure.
- [NSRemoteNotificationTypeNone](../nsremotenotificationtype/nsremotenotificationtypenone.md)
  The app shouldn’t display a badge.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Managing remote notifications
- [func registerForRemoteNotifications()](./registerforremotenotifications%28%29.md)
  Register for notifications sent by Apple Push Notification service (APNs).
- [func unregisterForRemoteNotifications()](./unregisterforremotenotifications%28%29.md)
  Unregister for notifications received from Apple Push Notification service.
- [var enabledRemoteNotificationTypes: NSApplication.RemoteNotificationType](./enabledremotenotificationtypes.md)
  The types of push notifications that the app accepts.
- [func registerForRemoteNotifications(matching: NSApplication.RemoteNotificationType)](./registerforremotenotifications%28matching%29.md)
  Register to receive notifications of the specified types from a provider through the Apple Push Notification service.
- [var isRegisteredForRemoteNotifications: Bool](./isregisteredforremotenotifications.md)
  A Boolean value indicating whether the app is registered with Apple Push Notification service (APNs).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/remotenotificationtype)*