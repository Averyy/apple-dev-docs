# application(_:didFailToContinueUserActivityWithType:error:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the app couldn’t continue the specified activity.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func application(_ application: NSApplication, didFailToContinueUserActivityWithType userActivityType: String, error: any Error)
```

```objc
- (void) application:(NSApplication *) application didFailToContinueUserActivityWithType:(NSString *) userActivityType error:(NSError *) error;
```

## Discussion

Use this method to let the user know that the specified activity could not be continued. If you do not implement this method, AppKit displays an error to the user with an appropriate message about the reason for the failure.

## Parameters

- `application`: The app that attempted to continue the activity.
- `userActivityType`: The activity type that was attempted.
- `error`: An error object indicating the reason for the failure.

## See Also

### Continuing User Activities
- [func application(NSApplication, willContinueUserActivityWithType: String) -> Bool](./application%28_,willcontinueuseractivitywithtype%29.md)
  Returns a Boolean value that indicates if the app can continue the specified activity.
- [func application(NSApplication, continue: NSUserActivity, restorationHandler: ([any NSUserActivityRestoring]) -> Void) -> Bool](./application%28_,continue,restorationhandler%29.md)
  Returns a Boolean value that indicates if the app successfully recreates the specified activity.
- [func application(NSApplication, didUpdate: NSUserActivity)](./application%28_,didupdate%29.md)
  Tells the delegate that there are changes to the specified activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/application(_:didfailtocontinueuseractivitywithtype:error:))*