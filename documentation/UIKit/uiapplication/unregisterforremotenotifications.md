# unregisterForRemoteNotifications()

**Framework**: UIKit  
**Kind**: method

Unregisters for all remote notifications received through Apple Push Notification service.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func unregisterForRemoteNotifications()
```

#### Discussion

You should call this method in rare circumstances only, such as when a new version of the app removes support for all types of remote notifications. Users can temporarily prevent apps from receiving remote notifications through the Notifications section of the Settings app. Apps unregistered through this method can always re-register.

## See Also

- [func registerForRemoteNotifications()](uiapplication/registerforremotenotifications.md)
  Registers to receive remote notifications through Apple Push Notification service.
- [var isRegisteredForRemoteNotifications: Bool](uiapplication/isregisteredforremotenotifications.md)
  A Boolean value that indicates whether the app is currently registered for remote notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/unregisterforremotenotifications())*