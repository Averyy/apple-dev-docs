# application(_:shouldRestoreSecureApplicationState:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate whether to restore the app’s saved state.

**Availability**:
- iOS 13.2+
- iPadOS 13.2+
- Mac Catalyst 13.2+
- tvOS 13.2+
- visionOS 1.0+

## Declaration

```swift
optional func application(_ application: UIApplication, shouldRestoreSecureApplicationState coder: NSCoder) -> Bool
```

```objc
- (BOOL) application:(UIApplication *) application shouldRestoreSecureApplicationState:(NSCoder *) coder;
```

#### Return Value

[`true`](../../Swift/true.md) to restore the app’s saved state; otherwise, [`false`](../../Swift/false.md).

#### Discussion

Apps must implement both this method and [`application(_:shouldSaveSecureApplicationState:)`](./application%28_,shouldsavesecureapplicationstate%29.md) for state preservation to occur.

Use the information from the provided coder to determine whether to proceed with state restoration. For example, you might return [`false`](../../Swift/false.md) if the data in the coder is from an earlier version of your app and you can’t restore it safely. Any objects you decode from the coder must adopt the [`NSSecureCoding`](../../Foundation/nssecurecoding.md) protocol.

This method supersedes [`application(_:shouldRestoreApplicationState:)`](./application%28_,shouldrestoreapplicationstate%29.md). If your delegate implements both methods, the system only calls this one.

## Parameters

- `application`: The singleton app object.
- `coder`: A keyed archiver containing the app’s previously saved state. The coder’s [`requiresSecureCoding`](../../Foundation/nscoder/requiressecurecoding.md) property is set to [`true`](../../Swift/true.md), and any objects you decode must adopt [`NSSecureCoding`](../../Foundation/nssecurecoding.md).

## See Also

### Managing app state restoration
- [func application(UIApplication, shouldSaveSecureApplicationState: NSCoder) -> Bool](./application%28_,shouldsavesecureapplicationstate%29.md)
  Asks the delegate whether to securely preserve the app’s state.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:shouldrestoresecureapplicationstate:))*