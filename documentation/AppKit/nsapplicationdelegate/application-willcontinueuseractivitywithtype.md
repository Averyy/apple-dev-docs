# application(_:willContinueUserActivityWithType:)

**Framework**: AppKit  
**Kind**: method

Returns a Boolean value that indicates if the app can continue the specified activity.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func application(_ application: NSApplication, willContinueUserActivityWithType userActivityType: String) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if you notify the user that your app is about to continue the activity or [`false`](https://developer.apple.com/documentation/swift/false) if you want AppKit to notify the user.

#### Discussion

Use this method to provide immediate feedback to the user that an activity is about to continue on this device. The app calls this method as soon as the user confirms that an activity should be continued but possibly before the data associated with that activity is available.

This method is called on the main thread as soon as the user indicates they want to continue an activity in your app. The `NSUserActivity` object may not be available instantly, so use this as an opportunity to show the user that an activity will be continued shortly and return [`true`](https://developer.apple.com/documentation/swift/true). If you leave this method unimplemented or return [`false`](https://developer.apple.com/documentation/swift/false), AppKit displays a default indication.

For each invocation of this method, the app delegate is guaranteed to get exactly one invocation of [`application(_:continue:restorationHandler:)`](nsapplicationdelegate/application(_:continue:restorationhandler:).md) on success, or [`application(_:didFailToContinueUserActivityWithType:error:)`](nsapplicationdelegate/application(_:didfailtocontinueuseractivitywithtype:error:).md) if an error was encountered.

## Parameters

- `application`: The app continuing the user activity.
- `userActivityType`: The type of activity to be continued.

## See Also

- [func application(NSApplication, continue: NSUserActivity, restorationHandler: ([any NSUserActivityRestoring]) -> Void) -> Bool](nsapplicationdelegate/application(_:continue:restorationhandler:).md)
  Returns a Boolean value that indicates if the app successfully recreates the specified activity.
- [func application(NSApplication, didFailToContinueUserActivityWithType: String, error: any Error)](nsapplicationdelegate/application(_:didfailtocontinueuseractivitywithtype:error:).md)
  Tells the delegate that the app couldn’t continue the specified activity.
- [func application(NSApplication, didUpdate: NSUserActivity)](nsapplicationdelegate/application(_:didupdate:).md)
  Tells the delegate that there are changes to the specified activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/application(_:willcontinueuseractivitywithtype:))*