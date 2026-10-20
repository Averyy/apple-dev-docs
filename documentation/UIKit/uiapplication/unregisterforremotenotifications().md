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
func unregisterForRemoteNotifications()
```

#### Discussion

Call this method when your app no longer needs to receive push notifications, such as when:

- Someone logs out of an account associated with push notifications
- Someone explicitly requests to stop receiving notifications through your app interface
- Your app removes support for all types of remote notifications

The Settings app also provides controls to prevent apps from receiving remote notifications. Apps unregistered through this method can always re-register by calling [`registerForRemoteNotifications()`](uiapplication/registerforremotenotifications().md).

## See Also

- [func registerForRemoteNotifications()](uiapplication/registerforremotenotifications.md)
  Registers to receive remote notifications through Apple Push Notification service.
- [var isRegisteredForRemoteNotifications: Bool](uiapplication/isregisteredforremotenotifications.md)
  A Boolean value that indicates whether the app is currently registered for remote notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/unregisterforremotenotifications())*