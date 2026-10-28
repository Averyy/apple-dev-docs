# application(_:userDidAcceptCloudKitShareWith:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the app now has access to shared information in CloudKit.

**Availability**:
- iOS 10.0+ - Deprecated in 26.0
- iPadOS 10.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- tvOS 10.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0

> **Deprecated**: Use UIScene lifecycle and windowScene(_:userDidAcceptCloudKitShareWith:) from UIWindowSceneDelegate instead.

## Declaration

```swift
optional func application(_ application: UIApplication, userDidAcceptCloudKitShareWith cloudKitShareMetadata: CKShareMetadata)
```

```objc
- (void) application:(UIApplication *) application userDidAcceptCloudKitShareWithMetadata:(CKShareMetadata *) cloudKitShareMetadata;
```

## Discussion

If your app doesn’t support scenes, use this method to respond to a CloudKit Sharing invitation. In your implementation, accept the share by scheduling a [`CKAcceptSharesOperation`](../../CloudKit/ckacceptsharesoperation.md) object that contains the metadata object in the `cloudKitShareMetadata` parameter. After the share has been accepted, you can begin fetching records and incorporating the resulting data into your app. For a scene-based app, accept the invitation in your window scene delegate’s [`windowScene(_:userDidAcceptCloudKitShareWith:)`](../uiwindowscenedelegate/windowscene%28_,userdidacceptcloudkitsharewith%29.md) method.

The system launches the app, as needed, before calling this method.

## Parameters

- `application`: The shared app object.
- `cloudKitShareMetadata`: Information about the CloudKit data that is now available to the app. Use this object to retrieve information about the [`CKShare`](../../CloudKit/ckshare.md) object and the associated records that are now available.

## See Also

### Deprecated methods
- [func applicationDidBecomeActive(UIApplication)](./applicationdidbecomeactive%28_%29.md)
  Tells the delegate that the app has become active.
- [func applicationWillResignActive(UIApplication)](./applicationwillresignactive%28_%29.md)
  Tells the delegate that the app is about to become inactive.
- [func applicationWillEnterForeground(UIApplication)](./applicationwillenterforeground%28_%29.md)
  Tells the delegate that the app is about to enter the foreground.
- [func application(UIApplication, willContinueUserActivityWithType: String) -> Bool](./application%28_,willcontinueuseractivitywithtype%29.md)
  Tells the delegate if your app takes responsibility for notifying users when a continuation activity takes longer than expected.
- [func application(UIApplication, continue: NSUserActivity, restorationHandler: ([any UIUserActivityRestoring]?) -> Void) -> Bool](./application%28_,continue,restorationhandler%29.md)
  Tells the delegate that the data for continuing an activity is available.
- [func application(UIApplication, didUpdate: NSUserActivity)](./application%28_,didupdate%29.md)
  Tells the delegate that the activity was updated.
- [func application(UIApplication, didFailToContinueUserActivityWithType: String, error: any Error)](./application%28_,didfailtocontinueuseractivitywithtype,error%29.md)
  Tells the delegate that the activity couldn’t be continued.
- [func application(UIApplication, performActionFor: UIApplicationShortcutItem, completionHandler: (Bool) -> Void)](./application%28_,performactionfor,completionhandler%29.md)
  Tells the delegate that the user selected a Home screen quick action for your app, except when you’ve intercepted the interaction in a launch method.
- [func application(UIApplication, open: URL, options: [UIApplication.OpenURLOptionsKey : Any]) -> Bool](./application%28_,open,options%29.md)
  Asks the delegate to open a resource specified by a URL, and provides a dictionary of launch options.
- [func application(UIApplication, supportedInterfaceOrientationsFor: UIWindow?) -> UIInterfaceOrientationMask](./application%28_,supportedinterfaceorientationsfor%29.md)
  Asks the delegate for the interface orientations to use for the view controllers in the specified window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:userdidacceptcloudkitsharewith:))*