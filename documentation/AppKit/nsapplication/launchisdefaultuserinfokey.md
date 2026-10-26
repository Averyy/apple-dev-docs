# launchIsDefaultUserInfoKey

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

A Boolean value that indicates if the app launch is a default launch.

**Availability**:
- macOS 10.7+

## Declaration

```swift
class let launchIsDefaultUserInfoKey: String
```

```c
extern NSString * const NSApplicationLaunchIsDefaultLaunchKey;
```

#### Discussion

The value for this key is an [`NSNumber`](../../Foundation/nsnumber.md) containing a Boolean value. The value is [`false`](../../Swift/false.md) if the app was launched to open or print a file, to perform a Service action, if the app had saved state that will be restored, or if the app launch was in some other sense not a default launch. Otherwise its value will be [`true`](../../Swift/true.md).

## See Also

### Keys
- [class let launchUserNotificationUserInfoKey: String](./launchusernotificationuserinfokey.md)
  A key that indicates your app was launched because a user activated a notification in the Notification Center.
- [NSApplicationLaunchRemoteNotificationKey](../nsapplicationlaunchremotenotificationkey.md)
  Use this key to access the JSON push-notification payload from the user info dictionary of the `didFinishLaunchingNotification` notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/launchisdefaultuserinfokey)*