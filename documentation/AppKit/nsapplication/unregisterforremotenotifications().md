# unregisterForRemoteNotifications()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Unregister for notifications received from Apple Push Notification service.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func unregisterForRemoteNotifications()
```

```objc
- (void) unregisterForRemoteNotifications;
```

#### Discussion

You should only call this method in rare circumstances, such as when a new version of the app drops support for remote notifications. Apps unregistered through this method can always reregister.

## See Also

### Managing remote notifications
- [func registerForRemoteNotifications()](./registerforremotenotifications%28%29.md)
  Register for notifications sent by Apple Push Notification service (APNs).
- [var enabledRemoteNotificationTypes: NSApplication.RemoteNotificationType](./enabledremotenotificationtypes.md)
  The types of push notifications that the app accepts.
- [func registerForRemoteNotifications(matching: NSApplication.RemoteNotificationType)](./registerforremotenotifications%28matching%29.md)
  Register to receive notifications of the specified types from a provider through the Apple Push Notification service.
- [var isRegisteredForRemoteNotifications: Bool](./isregisteredforremotenotifications.md)
  A Boolean value indicating whether the app is registered with Apple Push Notification service (APNs).
- [NSApplication.RemoteNotificationType](./remotenotificationtype.md)
  These constants determine whether apps launched by remote notifications display a badge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/unregisterforremotenotifications())*