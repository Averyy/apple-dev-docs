# application(_:didDecodeRestorableStateWith:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells your delegate to restore any high-level state information as part of the state restoration process.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
optional func application(_ application: UIApplication, didDecodeRestorableStateWith coder: NSCoder)
```

```objc
- (void) application:(UIApplication *) application didDecodeRestorableStateWithCoder:(NSCoder *) coder;
```

## Discussion

The state restoration system calls this method as the final step in the state restoration process. By the time this method is called, all other restorable objects will have been restored and put back into their previous state. You can use this method to read any high-level app data you saved in the [`application(_:willEncodeRestorableStateWith:)`](./application%28_,willencoderestorablestatewith%29.md) method and apply it to your app.

## Parameters

- `application`: Your singleton app object.
- `coder`: The keyed archiver containing the app’s previously saved state information.

## See Also

### Managing app state restoration
- [func application(UIApplication, shouldSaveSecureApplicationState: NSCoder) -> Bool](./application%28_,shouldsavesecureapplicationstate%29.md)
  Asks the delegate whether to securely preserve the app’s state.
- [func application(UIApplication, shouldRestoreSecureApplicationState: NSCoder) -> Bool](./application%28_,shouldrestoresecureapplicationstate%29.md)
  Asks the delegate whether to restore the app’s saved state.
- [func application(UIApplication, viewControllerWithRestorationIdentifierPath: [String], coder: NSCoder) -> UIViewController?](./application%28_,viewcontrollerwithrestorationidentifierpath,coder%29.md)
  Asks the delegate to provide the specified view controller.
- [func application(UIApplication, willEncodeRestorableStateWith: NSCoder)](./application%28_,willencoderestorablestatewith%29.md)
  Tells your delegate to save any high-level state information at the beginning of the state preservation process.
- [class let stateRestorationBundleVersionKey: String](../uiapplication/staterestorationbundleversionkey.md)
  The version of your app responsible for creating the restoration archive.
- [class let stateRestorationSystemVersionKey: String](../uiapplication/staterestorationsystemversionkey.md)
  The version of the system on which your app created the restoration archive.
- [class let stateRestorationTimestampKey: String](../uiapplication/staterestorationtimestampkey.md)
  The time your app created the restoration archive.
- [class let stateRestorationUserInterfaceIdiomKey: String](../uiapplication/staterestorationuserinterfaceidiomkey.md)
  The user interface idiom that was in effect when your app created the restoration archive.
- [class let stateRestorationViewControllerStoryboardKey: String](../uiapplication/staterestorationviewcontrollerstoryboardkey.md)
  A reference to the storyboard that contains the view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:diddecoderestorablestatewith:))*