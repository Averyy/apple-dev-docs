# application(_:performActionFor:completionHandler:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that the user selected a Home screen quick action for your app, except when you’ve intercepted the interaction in a launch method.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func application(_ application: UIApplication, performActionFor shortcutItem: UIApplicationShortcutItem) async -> Bool
```

#### Discussion

> ❗ **Important**:  This method is not called for scene-based apps. If you have a scene-based app, implement [`windowScene(_:performActionFor:completionHandler:)`](uiwindowscenedelegate/windowscene(_:performactionfor:completionhandler:).md) in your scene delegate instead.

Implement this method to respond to the user’s selection of a Home screen quick action for your app. When finished, call the completion handler, with an appropriate Boolean value.

It’s your responsibility to ensure the system calls this method conditionally, depending on whether or not one of your app launch methods ([`application(_:willFinishLaunchingWithOptions:)`](uiapplicationdelegate/application(_:willfinishlaunchingwithoptions:).md) or [`application(_:didFinishLaunchingWithOptions:)`](uiapplicationdelegate/application(_:didfinishlaunchingwithoptions:).md)) has already handled a quick action invocation. The system calls a launch method (before calling this method) when a user selects a quick action for your app and your app  instead of .

The requested quick action might employ code paths different than those used otherwise when your app launches. For example, your app normally launches to display view A, but your app was launched in response to a quick action that needs view B. To handle such cases, upon launch, check whether your app is being launched via a quick action. Perform this check in your [`application(_:willFinishLaunchingWithOptions:)`](uiapplicationdelegate/application(_:willfinishlaunchingwithoptions:).md) or [`application(_:didFinishLaunchingWithOptions:)`](uiapplicationdelegate/application(_:didfinishlaunchingwithoptions:).md) method by checking for the [`shortcutItem`](uiapplication/launchoptionskey/shortcutitem.md) launch option key. The [`UIApplicationShortcutItem`](uiapplicationshortcutitem.md) object is available as the value of the launch option key.

If you find that your app was indeed launched using a quick action, perform the requested quick action within the launch method and return a value of [`false`](https://developer.apple.com/documentation/swift/false) from that method. When you return a value of [`false`](https://developer.apple.com/documentation/swift/false), the system doesn’t call the [`application(_:performActionFor:completionHandler:)`](uiapplicationdelegate/application(_:performactionfor:completionhandler:).md) method.

## Parameters

- `application`: Your shared app object.
- `shortcutItem`: The quick action for which you’re providing an implementation in this method.
- `completionHandler`: The block you call after your quick action implementation completes, returning   or   depending on the success or failure of your implementation code.

## See Also

- [func application(UIApplication, willContinueUserActivityWithType: String) -> Bool](uiapplicationdelegate/application(_:willcontinueuseractivitywithtype:).md)
  Tells the delegate if your app takes responsibility for notifying users when a continuation activity takes longer than expected.
- [func application(UIApplication, continue: NSUserActivity, restorationHandler: ([any UIUserActivityRestoring]?) -> Void) -> Bool](uiapplicationdelegate/application(_:continue:restorationhandler:).md)
  Tells the delegate that the data for continuing an activity is available.
- [func application(UIApplication, didUpdate: NSUserActivity)](uiapplicationdelegate/application(_:didupdate:).md)
  Tells the delegate that the activity was updated.
- [func application(UIApplication, didFailToContinueUserActivityWithType: String, error: any Error)](uiapplicationdelegate/application(_:didfailtocontinueuseractivitywithtype:error:).md)
  Tells the delegate that the activity couldn’t be continued.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:performactionfor:completionhandler:))*