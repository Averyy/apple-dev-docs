# launchUserNotificationUserInfoKey

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

A key that indicates your app was launched because a user activated a notification in the Notification Center.

**Availability**:
- macOS 10.8+

## Declaration

```swift
class let launchUserNotificationUserInfoKey: String
```

```c
extern NSString * const NSApplicationLaunchUserNotificationKey;
```

#### Discussion

The [`launchUserNotificationUserInfoKey`](./launchusernotificationuserinfokey.md) key is an [`NSUserNotification`](../../Foundation/nsusernotification.md) object that is present in the [`userInfo`](../../Foundation/nsnotification/userinfo.md) dictionary of the [`didFinishLaunchingNotification`](./didfinishlaunchingnotification.md) notification if your app was launched because a user activated a notification in the Notification Center. To access the notification payload in the [`userInfo`](../../Foundation/nsnotification/userinfo.md) dictionary, you can use code like this:

```objc
NSUserNotification *userNotification = [[myNotification userInfo]
    objectForKey:NSApplicationLaunchUserNotificationKey];
    if (userNotification) {
        // The app was launched by a user selection from Notification Center.
    }
```

## See Also

### Keys
- [class let launchIsDefaultUserInfoKey: String](./launchisdefaultuserinfokey.md)
  A Boolean value that indicates if the app launch is a default launch.
- [NSApplicationLaunchRemoteNotificationKey](../nsapplicationlaunchremotenotificationkey.md)
  Use this key to access the JSON push-notification payload from the user info dictionary of the `didFinishLaunchingNotification` notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/launchusernotificationuserinfokey)*