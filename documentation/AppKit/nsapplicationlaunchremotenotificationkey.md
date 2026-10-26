# NSApplicationLaunchRemoteNotificationKey

**Framework**: AppKit  
**Kind**: var  
**Role**: Global Variable

Use this key to access the JSON push-notification payload from the user info dictionary of the `didFinishLaunchingNotification` notification.

**Availability**:
- macOS 10.7+ - Deprecated in 10.8

## Declaration

```c
extern NSString * const NSApplicationLaunchRemoteNotificationKey;
```

#### Discussion

> **Deprecated**: Use [`launchUserNotificationUserInfoKey`](./nsapplication/launchusernotificationuserinfokey.md) instead.

The [`didFinishLaunchingNotification`](./nsapplication/didfinishlaunchingnotification.md) notification is passed into the delegate method [`applicationDidFinishLaunching(_:)`](./nsapplicationdelegate/applicationdidfinishlaunching%28_%29.md) declared by the [`NSApplicationDelegate`](./nsapplicationdelegate.md) protocol to handle this notification.

## See Also

### Keys
- [class let launchIsDefaultUserInfoKey: String](./nsapplication/launchisdefaultuserinfokey.md)
  A Boolean value that indicates if the app launch is a default launch.
- [class let launchUserNotificationUserInfoKey: String](./nsapplication/launchusernotificationuserinfokey.md)
  A key that indicates your app was launched because a user activated a notification in the Notification Center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationlaunchremotenotificationkey)*