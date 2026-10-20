# isRegisteredForRemoteNotifications

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the app is currently registered for remote notifications.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var isRegisteredForRemoteNotifications: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isRegisteredForRemoteNotifications) BOOL registeredForRemoteNotifications;
```

#### Discussion

This method reflects whether the remote registration process completed successfully—a process that begins when you call the [`registerForRemoteNotifications()`](./registerforremotenotifications%28%29.md) method. This method does not reflect whether remote notifications are actually available due to connectivity issues. The value returned by this method takes into account the user’s preferences for receiving remote notifications.

## See Also

### Registering for remote notifications
- [func registerForRemoteNotifications()](./registerforremotenotifications%28%29.md)
  Registers to receive remote notifications through Apple Push Notification service.
- [func unregisterForRemoteNotifications()](./unregisterforremotenotifications%28%29.md)
  Unregisters for all remote notifications received through Apple Push Notification service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/isregisteredforremotenotifications)*