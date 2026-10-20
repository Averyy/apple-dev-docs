# isRegisteredForRemoteNotifications

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the app is registered with Apple Push Notification service (APNs).

**Availability**:
- macOS 10.14+

## Declaration

```swift
var isRegisteredForRemoteNotifications: Bool { get }
```

```objc
@property (readonly, getter=isRegisteredForRemoteNotifications) BOOL registeredForRemoteNotifications;
```

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
- [NSApplication.RemoteNotificationType](./remotenotificationtype.md)
  These constants determine whether apps launched by remote notifications display a badge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/isregisteredforremotenotifications)*