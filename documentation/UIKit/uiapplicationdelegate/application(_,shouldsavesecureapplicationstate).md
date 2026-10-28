# application(_:shouldSaveSecureApplicationState:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate whether to securely preserve the app’s state.

**Availability**:
- iOS 13.2+
- iPadOS 13.2+
- Mac Catalyst 13.2+
- tvOS 13.2+
- visionOS 1.0+

## Declaration

```swift
optional func application(_ application: UIApplication, shouldSaveSecureApplicationState coder: NSCoder) -> Bool
```

```objc
- (BOOL) application:(UIApplication *) application shouldSaveSecureApplicationState:(NSCoder *) coder;
```

## Return Value

[`true`](../../Swift/true.md) to securely preserve the app’s state; otherwise, [`false`](../../Swift/false.md).

## Discussion

Apps must implement both this method and [`application(_:shouldRestoreSecureApplicationState:)`](./application%28_,shouldrestoresecureapplicationstate%29.md) for state preservation to occur.

Your implementation of this method should return [`true`](../../Swift/true.md) each time UIKit attempts to preserve the state of your app. You can temporarily disable state preservation by returning [`false`](../../Swift/false.md), which you may want to do during testing, for example.

You can add version information or any other contextual data to the provided coder as necessary. During restoration, you can use that information to determine whether to proceed with restoring your app to its previous state. Any objects you add to the coder must adopt the [`NSSecureCoding`](../../Foundation/nssecurecoding.md) protocol.

This method supersedes [`application(_:shouldSaveApplicationState:)`](./application%28_,shouldsaveapplicationstate%29.md). If your delegate implements both methods, the system only calls this one.

## Parameters

- `application`: The singleton app object.
- `coder`: A keyed archiver where you can store high-level state information. The coder’s [`requiresSecureCoding`](../../Foundation/nscoder/requiressecurecoding.md) property is set to [`true`](../../Swift/true.md), and any objects you encode must adopt [`NSSecureCoding`](../../Foundation/nssecurecoding.md).

## See Also

### Managing app state restoration
- [func application(UIApplication, shouldRestoreSecureApplicationState: NSCoder) -> Bool](./application%28_,shouldrestoresecureapplicationstate%29.md)
  Asks the delegate whether to restore the app’s saved state.
- [func application(UIApplication, viewControllerWithRestorationIdentifierPath: [String], coder: NSCoder) -> UIViewController?](./application%28_,viewcontrollerwithrestorationidentifierpath,coder%29.md)
  Asks the delegate to provide the specified view controller.
- [func application(UIApplication, willEncodeRestorableStateWith: NSCoder)](./application%28_,willencoderestorablestatewith%29.md)
  Tells your delegate to save any high-level state information at the beginning of the state preservation process.
- [func application(UIApplication, didDecodeRestorableStateWith: NSCoder)](./application%28_,diddecoderestorablestatewith%29.md)
  Tells your delegate to restore any high-level state information as part of the state restoration process.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:shouldsavesecureapplicationstate:))*