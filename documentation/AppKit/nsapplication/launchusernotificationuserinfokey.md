# launchUserNotificationUserInfoKey

**Framework**: AppKit  
**Kind**: property

A key that indicates your app was launched because a user activated a notification in the Notification Center.

**Availability**:
- macOS 10.8+

## Declaration

```swift
class let launchUserNotificationUserInfoKey: String
```

#### Discussion

The [`launchUserNotificationUserInfoKey`](nsapplication/launchusernotificationuserinfokey.md) key is an [`NSUserNotification`](https://developer.apple.com/documentation/Foundation/NSUserNotification) object that is present in the [`userInfo`](https://developer.apple.com/documentation/Foundation/NSNotification/userInfo) dictionary of the [`didFinishLaunchingNotification`](nsapplication/didfinishlaunchingnotification.md) notification if your app was launched because a user activated a notification in the Notification Center. To access the notification payload in the [`userInfo`](https://developer.apple.com/documentation/Foundation/NSNotification/userInfo) dictionary, you can use code like this:

```objc
NSUserNotification *userNotification = [[myNotification userInfo]
    objectForKey:NSApplicationLaunchUserNotificationKey];
    if (userNotification) {
        // The app was launched by a user selection from Notification Center.
    }
```

## See Also

- [class let launchIsDefaultUserInfoKey: String](nsapplication/launchisdefaultuserinfokey.md)
  A Boolean value that indicates if the app launch is a default launch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/launchusernotificationuserinfokey)*