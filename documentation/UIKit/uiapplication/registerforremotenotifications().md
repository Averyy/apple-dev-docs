# registerForRemoteNotifications()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Registers to receive remote notifications through Apple Push Notification service.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func registerForRemoteNotifications()
```

```objc
- (void) registerForRemoteNotifications;
```

#### Discussion

Call this method to initiate the registration process with Apple Push Notification service. If registration succeeds, the app calls your app delegate object’s  [`application(_:didRegisterForRemoteNotificationsWithDeviceToken:)`](../uiapplicationdelegate/application%28_,didregisterforremotenotificationswithdevicetoken%29.md) method and passes it a device token. You should pass this token along to the server you use to generate remote notifications for the device. If registration fails, the app calls its app delegate’s [`application(_:didFailToRegisterForRemoteNotificationsWithError:)`](../uiapplicationdelegate/application%28_,didfailtoregisterforremotenotificationswitherror%29.md) method instead.

If you want your app’s remote notifications to display alerts, play sounds, or perform other user-facing actions, you must request authorization to do so using the [`requestAuthorization(options:completionHandler:)`](../../UserNotifications/unusernotificationcenter/requestauthorization%28options,completionhandler%29.md) method of [`UNUserNotificationCenter`](../../UserNotifications/unusernotificationcenter.md). If you do not request and receive authorization for your app’s interactions, the system delivers all remote notifications to your app silently.

## See Also

### Registering for remote notifications
- [func unregisterForRemoteNotifications()](./unregisterforremotenotifications%28%29.md)
  Unregisters for all remote notifications received through Apple Push Notification service.
- [var isRegisteredForRemoteNotifications: Bool](./isregisteredforremotenotifications.md)
  A Boolean value that indicates whether the app is currently registered for remote notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/registerforremotenotifications())*