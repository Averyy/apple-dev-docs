# application(_:didUpdate:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that there are changes to the specified activity.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func application(_ application: NSApplication, didUpdate userActivity: NSUserActivity)
```

```objc
- (void) application:(NSApplication *) application didUpdateUserActivity:(NSUserActivity *) userActivity;
```

## Discussion

This method is called when any user activity managed by AppKit has been updated. Use this as a last chance to add additional data to the user activity object.

## Parameters

- `application`: The shared app object.
- `userActivity`: The user activity object that was updated.

## See Also

### Continuing User Activities
- [func application(NSApplication, willContinueUserActivityWithType: String) -> Bool](./application%28_,willcontinueuseractivitywithtype%29.md)
  Returns a Boolean value that indicates if the app can continue the specified activity.
- [func application(NSApplication, continue: NSUserActivity, restorationHandler: ([any NSUserActivityRestoring]) -> Void) -> Bool](./application%28_,continue,restorationhandler%29.md)
  Returns a Boolean value that indicates if the app successfully recreates the specified activity.
- [func application(NSApplication, didFailToContinueUserActivityWithType: String, error: any Error)](./application%28_,didfailtocontinueuseractivitywithtype,error%29.md)
  Tells the delegate that the app couldn’t continue the specified activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/application(_:didupdate:))*