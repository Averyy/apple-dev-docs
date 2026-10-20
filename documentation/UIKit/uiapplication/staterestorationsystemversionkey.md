# stateRestorationSystemVersionKey

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

The version of the system on which your app created the restoration archive.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
class let stateRestorationSystemVersionKey: String
```

```c
extern NSString * const UIApplicationStateRestorationSystemVersionKey;
```

#### Discussion

The value of this key is an [`NSString`](../../Foundation/nsstring.md) object containing the iOS system version that was installed when the archive was saved. The format of this string matches the format of the value in the [`systemVersion`](../uidevice/systemversion.md) property of the [`UIDevice`](../uidevice.md) class.

## See Also

### Managing app state restoration
- [func application(UIApplication, shouldSaveSecureApplicationState: NSCoder) -> Bool](../uiapplicationdelegate/application%28_,shouldsavesecureapplicationstate%29.md)
  Asks the delegate whether to securely preserve the app’s state.
- [func application(UIApplication, shouldRestoreSecureApplicationState: NSCoder) -> Bool](../uiapplicationdelegate/application%28_,shouldrestoresecureapplicationstate%29.md)
  Asks the delegate whether to restore the app’s saved state.
- [func application(UIApplication, viewControllerWithRestorationIdentifierPath: [String], coder: NSCoder) -> UIViewController?](../uiapplicationdelegate/application%28_,viewcontrollerwithrestorationidentifierpath,coder%29.md)
  Asks the delegate to provide the specified view controller.
- [func application(UIApplication, willEncodeRestorableStateWith: NSCoder)](../uiapplicationdelegate/application%28_,willencoderestorablestatewith%29.md)
  Tells your delegate to save any high-level state information at the beginning of the state preservation process.
- [func application(UIApplication, didDecodeRestorableStateWith: NSCoder)](../uiapplicationdelegate/application%28_,diddecoderestorablestatewith%29.md)
  Tells your delegate to restore any high-level state information as part of the state restoration process.
- [class let stateRestorationBundleVersionKey: String](./staterestorationbundleversionkey.md)
  The version of your app responsible for creating the restoration archive.
- [class let stateRestorationTimestampKey: String](./staterestorationtimestampkey.md)
  The time your app created the restoration archive.
- [class let stateRestorationUserInterfaceIdiomKey: String](./staterestorationuserinterfaceidiomkey.md)
  The user interface idiom that was in effect when your app created the restoration archive.
- [class let stateRestorationViewControllerStoryboardKey: String](./staterestorationviewcontrollerstoryboardkey.md)
  A reference to the storyboard that contains the view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/staterestorationsystemversionkey)*