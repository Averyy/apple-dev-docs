# application(_:didFailToContinueUserActivityWithType:error:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that the activity couldn’t be continued.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func application(_ application: UIApplication, didFailToContinueUserActivityWithType userActivityType: String, error: any Error)
```

#### Discussion

Use this method to let the user know that the specified activity could not be continued. If you do not implement this method, UIKit displays an error to the user with an appropriate message about the reason for the failure.

This method is not called if either [`application(_:willFinishLaunchingWithOptions:)`](uiapplicationdelegate/application(_:willfinishlaunchingwithoptions:).md) or [`application(_:didFinishLaunchingWithOptions:)`](uiapplicationdelegate/application(_:didfinishlaunchingwithoptions:).md) returns [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `application`: Your shared app object.
- `userActivityType`: The activity type that was attempted.
- `error`: An error object indicating the reason for the failure.

## See Also

- [func application(UIApplication, willContinueUserActivityWithType: String) -> Bool](uiapplicationdelegate/application(_:willcontinueuseractivitywithtype:).md)
  Tells the delegate if your app takes responsibility for notifying users when a continuation activity takes longer than expected.
- [func application(UIApplication, continue: NSUserActivity, restorationHandler: ([any UIUserActivityRestoring]?) -> Void) -> Bool](uiapplicationdelegate/application(_:continue:restorationhandler:).md)
  Tells the delegate that the data for continuing an activity is available.
- [func application(UIApplication, didUpdate: NSUserActivity)](uiapplicationdelegate/application(_:didupdate:).md)
  Tells the delegate that the activity was updated.
- [func application(UIApplication, performActionFor: UIApplicationShortcutItem, completionHandler: (Bool) -> Void)](uiapplicationdelegate/application(_:performactionfor:completionhandler:).md)
  Tells the delegate that the user selected a Home screen quick action for your app, except when you’ve intercepted the interaction in a launch method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:didfailtocontinueuseractivitywithtype:error:))*