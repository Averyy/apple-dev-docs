# application(_:continue:restorationHandler:)

**Framework**: AppKit  
**Kind**: method

Returns a Boolean value that indicates if the app successfully recreates the specified activity.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func application(_ application: NSApplication, continue userActivity: NSUserActivity, restorationHandler: @escaping ([any NSUserActivityRestoring]) -> Void) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if this method handled continuing the activity; [`false`](https://developer.apple.com/documentation/swift/false) to have AppKit attempt to continue the activity.

#### Discussion

The app calls this method when it receives the data associated with the user activity. Use the data stored in the `NSUserActivity` object to re-create the user’s activity. This method is your opportunity to update your app so that it can perform the associated task.

If this user activity object was created automatically by having `NSUbiquitousDocumentUserActivityType` in a `CFBundleDocumentTypes` entry, AppKit can automatically restore the [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) in macOS if this method returns [`false`](https://developer.apple.com/documentation/swift/false), or if it is unimplemented. It does this by creating a document of the appropriate type using the URL stored in the [`userInfo`](https://developer.apple.com/documentation/foundation/nsuseractivity/1411706-userinfo) dictionary under the `NSUserActivityDocumentURLKey`. The system calls the [`NSDocument`](nsdocument.md) method [`restoreUserActivityState(_:)`](nsuseractivityrestoring/restoreuseractivitystate(_:).md) on the document.

## Parameters

- `application`: The app continuing the user activity.
- `userActivity`: The activity object containing the data associated with the task the user was performing. Use the data in this object to recreate what the user was doing.
- `restorationHandler`: A block to execute if your app creates or fetches objects to perform the task. Calling this block is optional and is only needed when specific objects are capable of continuing the activity. You can copy this block and call it at a later time. When calling a saved copy of the block, you must call it from the app’s main thread. This block has no return value and takes the following parameter:

## See Also

- [func application(NSApplication, willContinueUserActivityWithType: String) -> Bool](nsapplicationdelegate/application(_:willcontinueuseractivitywithtype:).md)
  Returns a Boolean value that indicates if the app can continue the specified activity.
- [func application(NSApplication, didFailToContinueUserActivityWithType: String, error: any Error)](nsapplicationdelegate/application(_:didfailtocontinueuseractivitywithtype:error:).md)
  Tells the delegate that the app couldn’t continue the specified activity.
- [func application(NSApplication, didUpdate: NSUserActivity)](nsapplicationdelegate/application(_:didupdate:).md)
  Tells the delegate that there are changes to the specified activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/application(_:continue:restorationhandler:))*