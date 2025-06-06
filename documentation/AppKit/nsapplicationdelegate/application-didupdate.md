# application(_:didUpdate:)

**Framework**: AppKit  
**Kind**: method

Tells the delegate that there are changes to the specified activity.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func application(_ application: NSApplication, didUpdate userActivity: NSUserActivity)
```

#### Discussion

This method is called when any user activity managed by AppKit has been updated. Use this as a last chance to add additional data to the user activity object.

## Parameters

- `application`: The shared app object.
- `userActivity`: The user activity object that was updated.

## See Also

- [func application(NSApplication, willContinueUserActivityWithType: String) -> Bool](nsapplicationdelegate/application(_:willcontinueuseractivitywithtype:).md)
  Returns a Boolean value that indicates if the app can continue the specified activity.
- [func application(NSApplication, continue: NSUserActivity, restorationHandler: ([any NSUserActivityRestoring]) -> Void) -> Bool](nsapplicationdelegate/application(_:continue:restorationhandler:).md)
  Returns a Boolean value that indicates if the app successfully recreates the specified activity.
- [func application(NSApplication, didFailToContinueUserActivityWithType: String, error: any Error)](nsapplicationdelegate/application(_:didfailtocontinueuseractivitywithtype:error:).md)
  Tells the delegate that the app couldn’t continue the specified activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/application(_:didupdate:))*