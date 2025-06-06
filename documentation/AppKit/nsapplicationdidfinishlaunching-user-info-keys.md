# NSApplicationDidFinishLaunching User Info Keys

**Framework**: AppKit

The keys you use to access values in the launch options dictionary that the system passes to your app at initialization.

## Topics

### Keys
- [class let launchIsDefaultUserInfoKey: String](nsapplication/launchisdefaultuserinfokey.md)
  The value for this key is an `NSNumber` containing a Boolean value. The value is [`false`](https://developer.apple.com/documentation/swift/false) if the app was launched to open or print a file, to perform a Service action, if the app had saved state that will be restored, or if the app launch was in some other sense not a default launch. Otherwise its value will be [`true`](https://developer.apple.com/documentation/swift/true).
- [class let launchUserNotificationUserInfoKey: String](nsapplication/launchusernotificationuserinfokey.md)
  A key that indicates your app was launched because a user activated a notification in the Notification Center.

## See Also

- [func applicationWillFinishLaunching(Notification)](nsapplicationdelegate/applicationwillfinishlaunching(_:).md)
  Tells the delegate that the app’s initialization is about to complete.
- [func applicationDidFinishLaunching(Notification)](nsapplicationdelegate/applicationdidfinishlaunching(_:).md)
  Tells the delegate that the app’s initialization is complete but it hasn’t received its first event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdidfinishlaunching-user-info-keys)*