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

The [`launchUserNotificationUserInfoKey`](nsapplication/launchusernotificationuserinfokey.md) key is an [`NSUserNotification`](https://developer.apple.com/documentation/Foundation/NSUserNotification) object that is present in the [`userInfo`](https://developer.apple.com/documentation/foundation/nsnotification/1409222-userinfo) dictionary of the [`didFinishLaunchingNotification`](nsapplication/didfinishlaunchingnotification.md) notification if your app was launched because a user activated a notification in the Notification Center. To access the notification payload in the [`userInfo`](https://developer.apple.com/documentation/foundation/nsnotification/1409222-userinfo) dictionary, you can use code like this:

```objc
NSUserNotification *userNotification = [[myNotification userInfo]
    objectForKey:NSApplicationLaunchUserNotificationKey];
    if (userNotification) {
        // The app was launched by a user selection from Notification Center.
    }
```

## See Also

- [class let launchIsDefaultUserInfoKey: String](nsapplication/launchisdefaultuserinfokey.md)
  The value for this key is an `NSNumber` containing a Boolean value. The value is [`false`](https://developer.apple.com/documentation/swift/false) if the app was launched to open or print a file, to perform a Service action, if the app had saved state that will be restored, or if the app launch was in some other sense not a default launch. Otherwise its value will be [`true`](https://developer.apple.com/documentation/swift/true).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/launchusernotificationuserinfokey)*