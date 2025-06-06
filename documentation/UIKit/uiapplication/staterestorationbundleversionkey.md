# stateRestorationBundleVersionKey

**Framework**: UIKit  
**Kind**: property

The version of your app responsible for creating the restoration archive.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
class let stateRestorationBundleVersionKey: String
```

#### Discussion

The value of this key is an [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) object that identifies the version of your app (as obtained from the `CFBundleVersion` key of your app’s `Info.plist` file) that was present when the state information was saved. You can use the value of this key to help make choices about how to proceed during state restoration. For example, if the key indicates that the state is associated with an older version of your app, you might want to avoid restoring the previous state altogether or modify the restoration process more significantly.

## See Also

- [func application(UIApplication, shouldSaveSecureApplicationState: NSCoder) -> Bool](uiapplicationdelegate/application(_:shouldsavesecureapplicationstate:).md)
  Asks the delegate whether to securely preserve the app’s state.
- [func application(UIApplication, shouldRestoreSecureApplicationState: NSCoder) -> Bool](uiapplicationdelegate/application(_:shouldrestoresecureapplicationstate:).md)
  Asks the delegate whether to restore the app’s saved state.
- [func application(UIApplication, viewControllerWithRestorationIdentifierPath: [String], coder: NSCoder) -> UIViewController?](uiapplicationdelegate/application(_:viewcontrollerwithrestorationidentifierpath:coder:).md)
  Asks the delegate to provide the specified view controller.
- [func application(UIApplication, willEncodeRestorableStateWith: NSCoder)](uiapplicationdelegate/application(_:willencoderestorablestatewith:).md)
  Tells your delegate to save any high-level state information at the beginning of the state preservation process.
- [func application(UIApplication, didDecodeRestorableStateWith: NSCoder)](uiapplicationdelegate/application(_:diddecoderestorablestatewith:).md)
  Tells your delegate to restore any high-level state information as part of the state restoration process.
- [class let stateRestorationSystemVersionKey: String](uiapplication/staterestorationsystemversionkey.md)
  The version of the system on which your app created the restoration archive.
- [class let stateRestorationTimestampKey: String](uiapplication/staterestorationtimestampkey.md)
  The time your app created the restoration archive.
- [class let stateRestorationUserInterfaceIdiomKey: String](uiapplication/staterestorationuserinterfaceidiomkey.md)
  The user interface idiom that was in effect when your app created the restoration archive.
- [class let stateRestorationViewControllerStoryboardKey: String](uiapplication/staterestorationviewcontrollerstoryboardkey.md)
  A reference to the storyboard that contains the view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/staterestorationbundleversionkey)*