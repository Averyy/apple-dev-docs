# application(_:willContinueUserActivityWithType:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate if your app takes responsibility for notifying users when a continuation activity takes longer than expected.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func application(_ application: UIApplication, willContinueUserActivityWithType userActivityType: String) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if you want to notify the user that a continuation is in progress or [`false`](https://developer.apple.com/documentation/swift/false) if you want iOS to notify the user.

#### Discussion

Use this method to provide immediate feedback to the user that an activity is about to continue on this device. The app calls this method as soon as the user confirms that an activity should be continued but possibly before the data associated with that activity is available.

Your implementation of this method should prepare to initiate the activity. If you notify the user as part of your preparations, return [`true`](https://developer.apple.com/documentation/swift/true) from this method so that iOS does not also notify the user. If you do not implement this method or your implementation returns [`false`](https://developer.apple.com/documentation/swift/false), iOS notifes the user.

This method is not called if either [`application(_:willFinishLaunchingWithOptions:)`](uiapplicationdelegate/application(_:willfinishlaunchingwithoptions:).md) or [`application(_:didFinishLaunchingWithOptions:)`](uiapplicationdelegate/application(_:didfinishlaunchingwithoptions:).md) returns [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `application`: Your shared app object.
- `userActivityType`: The requested activity type.

## See Also

- [func application(UIApplication, continue: NSUserActivity, restorationHandler: ([any UIUserActivityRestoring]?) -> Void) -> Bool](uiapplicationdelegate/application(_:continue:restorationhandler:).md)
  Tells the delegate that the data for continuing an activity is available.
- [func application(UIApplication, didUpdate: NSUserActivity)](uiapplicationdelegate/application(_:didupdate:).md)
  Tells the delegate that the activity was updated.
- [func application(UIApplication, didFailToContinueUserActivityWithType: String, error: any Error)](uiapplicationdelegate/application(_:didfailtocontinueuseractivitywithtype:error:).md)
  Tells the delegate that the activity couldn’t be continued.
- [func application(UIApplication, performActionFor: UIApplicationShortcutItem, completionHandler: (Bool) -> Void)](uiapplicationdelegate/application(_:performactionfor:completionhandler:).md)
  Tells the delegate that the user selected a Home screen quick action for your app, except when you’ve intercepted the interaction in a launch method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:willcontinueuseractivitywithtype:))*