# unregisterForRemoteNotifications()

**Framework**: AppKit  
**Kind**: method

Unregister for notifications received from Apple Push Notification service.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func unregisterForRemoteNotifications()
```

#### Discussion

You should only call this method in rare circumstances, such as when a new version of the app drops support for remote notifications. Apps unregistered through this method can always reregister.

## See Also

- [func registerForRemoteNotifications()](nsapplication/registerforremotenotifications.md)
  Register for notifications sent by Apple Push Notification service (APNs).
- [var enabledRemoteNotificationTypes: NSApplication.RemoteNotificationType](nsapplication/enabledremotenotificationtypes.md)
  The types of push notifications that the app accepts.
- [func registerForRemoteNotifications(matching: NSApplication.RemoteNotificationType)](nsapplication/registerforremotenotifications(matching:).md)
  Register to receive notifications of the specified types from a provider through the Apple Push Notification service.
- [var isRegisteredForRemoteNotifications: Bool](nsapplication/isregisteredforremotenotifications.md)
  A Boolean value indicating whether the app is registered with Apple Push Notification service (APNs).
- [NSApplication.RemoteNotificationType](nsapplication/remotenotificationtype.md)
  These constants determine whether apps launched by remote notifications display a badge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/unregisterforremotenotifications())*