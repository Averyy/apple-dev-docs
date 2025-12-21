# NSApplicationDidFinishLaunching User Info Keys

**Framework**: AppKit

The keys you use to access values in the launch options dictionary that the system passes to your app at initialization.

## Topics

### Keys
- [class let launchIsDefaultUserInfoKey: String](nsapplication/launchisdefaultuserinfokey.md)
  A Boolean value that indicates if the app launch is a default launch.
- [class let launchUserNotificationUserInfoKey: String](nsapplication/launchusernotificationuserinfokey.md)
  A key that indicates your app was launched because a user activated a notification in the Notification Center.

## See Also

- [func applicationWillFinishLaunching(Notification)](nsapplicationdelegate/applicationwillfinishlaunching(_:).md)
  Tells the delegate that the app’s initialization is about to complete.
- [func applicationDidFinishLaunching(Notification)](nsapplicationdelegate/applicationdidfinishlaunching(_:).md)
  Tells the delegate that the app’s initialization is complete but it hasn’t received its first event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdidfinishlaunching-user-info-keys)*