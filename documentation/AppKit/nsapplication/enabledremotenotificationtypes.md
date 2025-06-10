# enabledRemoteNotificationTypes

**Framework**: AppKit  
**Kind**: property

The types of push notifications that the app accepts.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
var enabledRemoteNotificationTypes: NSApplication.RemoteNotificationType { get }
```

#### Return Value

A bit mask whose values indicate the types of notifications the user has requested for the app. See [`NSApplication.RemoteNotificationType`](nsapplication/remotenotificationtype.md) for valid bit-mask values.

#### Discussion

This property contains a bitmask whose values indicate the types of push notifications that the app requested. You don’t set this property directly. Call the [`registerForRemoteNotifications(matching:)`](nsapplication/registerforremotenotifications(matching:).md) method to register your app with Apple Push Notification Service and request the notification types your app supports. macOS delivers only notifications of types that the app supports. For a list of possible values, see [`NSApplication.RemoteNotificationType`](nsapplication/remotenotificationtype.md).

> **Note**:  Currently the only notification type supported for non-running apps is the badging of app icons.

## See Also

- [func registerForRemoteNotifications()](nsapplication/registerforremotenotifications.md)
  Register for notifications sent by Apple Push Notification service (APNs).
- [func unregisterForRemoteNotifications()](nsapplication/unregisterforremotenotifications.md)
  Unregister for notifications received from Apple Push Notification service.
- [func registerForRemoteNotifications(matching: NSApplication.RemoteNotificationType)](nsapplication/registerforremotenotifications(matching:).md)
  Register to receive notifications of the specified types from a provider through the Apple Push Notification service.
- [var isRegisteredForRemoteNotifications: Bool](nsapplication/isregisteredforremotenotifications.md)
  A Boolean value indicating whether the app is registered with Apple Push Notification service (APNs).
- [NSApplication.RemoteNotificationType](nsapplication/remotenotificationtype.md)
  These constants determine whether apps launched by remote notifications display a badge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/enabledremotenotificationtypes)*