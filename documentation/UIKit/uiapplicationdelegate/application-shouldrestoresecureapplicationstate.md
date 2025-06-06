# application(_:shouldRestoreSecureApplicationState:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate whether to restore the app’s saved state.

**Availability**:
- iOS 13.2+
- iPadOS 13.2+
- Mac Catalyst 13.2+
- tvOS 13.2+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func application(_ application: UIApplication, shouldRestoreSecureApplicationState coder: NSCoder) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) to restore the app’s saved state; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

Apps must implement both this method and [`application(_:shouldSaveSecureApplicationState:)`](uiapplicationdelegate/application(_:shouldsavesecureapplicationstate:).md) for state preservation to occur.

Use the information from the provided coder to determine whether to proceed with state restoration. For example, you might return [`false`](https://developer.apple.com/documentation/swift/false) if the data in the coder is from an earlier version of your app and you can’t restore it safely. Any objects you decode from the coder must adopt the [`NSSecureCoding`](https://developer.apple.com/documentation/Foundation/NSSecureCoding) protocol.

This method supersedes [`application(_:shouldRestoreApplicationState:)`](uiapplicationdelegate/application(_:shouldrestoreapplicationstate:).md). If your delegate implements both methods, the system only calls this one.

## Parameters

- `application`: The singleton app object.
- `coder`: A keyed archiver containing the app’s previously saved state. The coder’s   property is set to  , and any objects you decode must adopt  .

## See Also

- [func application(UIApplication, shouldSaveSecureApplicationState: NSCoder) -> Bool](uiapplicationdelegate/application(_:shouldsavesecureapplicationstate:).md)
  Asks the delegate whether to securely preserve the app’s state.
- [func application(UIApplication, viewControllerWithRestorationIdentifierPath: [String], coder: NSCoder) -> UIViewController?](uiapplicationdelegate/application(_:viewcontrollerwithrestorationidentifierpath:coder:).md)
  Asks the delegate to provide the specified view controller.
- [func application(UIApplication, willEncodeRestorableStateWith: NSCoder)](uiapplicationdelegate/application(_:willencoderestorablestatewith:).md)
  Tells your delegate to save any high-level state information at the beginning of the state preservation process.
- [func application(UIApplication, didDecodeRestorableStateWith: NSCoder)](uiapplicationdelegate/application(_:diddecoderestorablestatewith:).md)
  Tells your delegate to restore any high-level state information as part of the state restoration process.
- [class let stateRestorationBundleVersionKey: String](uiapplication/staterestorationbundleversionkey.md)
  The version of your app responsible for creating the restoration archive.
- [class let stateRestorationSystemVersionKey: String](uiapplication/staterestorationsystemversionkey.md)
  The version of the system on which your app created the restoration archive.
- [class let stateRestorationTimestampKey: String](uiapplication/staterestorationtimestampkey.md)
  The time your app created the restoration archive.
- [class let stateRestorationUserInterfaceIdiomKey: String](uiapplication/staterestorationuserinterfaceidiomkey.md)
  The user interface idiom that was in effect when your app created the restoration archive.
- [class let stateRestorationViewControllerStoryboardKey: String](uiapplication/staterestorationviewcontrollerstoryboardkey.md)
  A reference to the storyboard that contains the view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:shouldrestoresecureapplicationstate:))*