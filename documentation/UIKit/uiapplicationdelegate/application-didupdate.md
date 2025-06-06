# application(_:didUpdate:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that the activity was updated.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func application(_ application: UIApplication, didUpdate userActivity: NSUserActivity)
```

#### Discussion

This method is called on the main thread when a user activity managed by UIKit has been updated. You can implement this method as a final opportunity to add data to the user activity object.

## Parameters

- `application`: Your shared app object.
- `userActivity`: The activity object containing the data associated with the task the user was performing.

## See Also

- [func application(UIApplication, willContinueUserActivityWithType: String) -> Bool](uiapplicationdelegate/application(_:willcontinueuseractivitywithtype:).md)
  Tells the delegate if your app takes responsibility for notifying users when a continuation activity takes longer than expected.
- [func application(UIApplication, continue: NSUserActivity, restorationHandler: ([any UIUserActivityRestoring]?) -> Void) -> Bool](uiapplicationdelegate/application(_:continue:restorationhandler:).md)
  Tells the delegate that the data for continuing an activity is available.
- [func application(UIApplication, didFailToContinueUserActivityWithType: String, error: any Error)](uiapplicationdelegate/application(_:didfailtocontinueuseractivitywithtype:error:).md)
  Tells the delegate that the activity couldn’t be continued.
- [func application(UIApplication, performActionFor: UIApplicationShortcutItem, completionHandler: (Bool) -> Void)](uiapplicationdelegate/application(_:performactionfor:completionhandler:).md)
  Tells the delegate that the user selected a Home screen quick action for your app, except when you’ve intercepted the interaction in a launch method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:didupdate:))*