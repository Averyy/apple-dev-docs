# application(_:continue:restorationHandler:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates if the app successfully recreates the specified activity.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func application(_ application: NSApplication, continue userActivity: NSUserActivity, restorationHandler: @escaping ([any NSUserActivityRestoring]) -> Void) -> Bool
```

```objc
- (BOOL) application:(NSApplication *) application continueUserActivity:(NSUserActivity *) userActivity restorationHandler:(void (^)(NSArray<id<NSUserActivityRestoring>> *restorableObjects)) restorationHandler;
```

## Return Value

[`true`](../../Swift/true.md) if this method handled continuing the activity; [`false`](../../Swift/false.md) to have AppKit attempt to continue the activity.

## Discussion

The app calls this method when it receives the data associated with the user activity. Use the data stored in the `NSUserActivity` object to re-create the user’s activity. This method is your opportunity to update your app so that it can perform the associated task.

If this user activity object was created automatically by having `NSUbiquitousDocumentUserActivityType` in a `CFBundleDocumentTypes` entry, AppKit can automatically restore the [`NSUserActivity`](../../Foundation/nsuseractivity.md) in macOS if this method returns [`false`](../../Swift/false.md), or if it is unimplemented. It does this by creating a document of the appropriate type using the URL stored in the [`userInfo`](../../Foundation/nsuseractivity/userinfo.md) dictionary under the `NSUserActivityDocumentURLKey`. The system calls the [`NSDocument`](../nsdocument.md) method [`restoreUserActivityState(_:)`](../nsuseractivityrestoring/restoreuseractivitystate%28_%29.md) on the document.

## Parameters

- `application`: The app continuing the user activity.
- `userActivity`: The activity object containing the data associated with the task the user was performing. Use the data in this object to recreate what the user was doing.
- `restorationHandler`: A block to execute if your app creates or fetches objects to perform the task. Calling this block is optional and is only needed when specific objects are capable of continuing the activity. You can copy this block and call it at a later time. When calling a saved copy of the block, you must call it from the app’s main thread. This block has no return value and takes the following parameter:

  - **`restorableObjects`**: An array of [`NSResponder`](../nsresponder.md) or [`NSDocument`](../nsdocument.md) objects that you created or fetched in order to perform the operation. The system calls the [`restoreUserActivityState(_:)`](../nsuseractivityrestoring/restoreuseractivitystate%28_%29.md) method of each object in the array to perform the operation.

## See Also

### Continuing User Activities
- [func application(NSApplication, willContinueUserActivityWithType: String) -> Bool](./application%28_,willcontinueuseractivitywithtype%29.md)
  Returns a Boolean value that indicates if the app can continue the specified activity.
- [func application(NSApplication, didFailToContinueUserActivityWithType: String, error: any Error)](./application%28_,didfailtocontinueuseractivitywithtype,error%29.md)
  Tells the delegate that the app couldn’t continue the specified activity.
- [func application(NSApplication, didUpdate: NSUserActivity)](./application%28_,didupdate%29.md)
  Tells the delegate that there are changes to the specified activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/application(_:continue:restorationhandler:))*