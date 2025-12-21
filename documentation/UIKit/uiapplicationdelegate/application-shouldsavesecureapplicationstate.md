# application(_:shouldSaveSecureApplicationState:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate whether to securely preserve the app’s state.

**Availability**:
- iOS 13.2+
- iPadOS 13.2+
- Mac Catalyst 13.2+
- tvOS 13.2+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func application(_ application: UIApplication, shouldSaveSecureApplicationState coder: NSCoder) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) to securely preserve the app’s state; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

Apps must implement both this method and [`application(_:shouldRestoreSecureApplicationState:)`](uiapplicationdelegate/application(_:shouldrestoresecureapplicationstate:).md) for state preservation to occur.

Your implementation of this method should return [`true`](https://developer.apple.com/documentation/Swift/true) each time UIKit attempts to preserve the state of your app. You can temporarily disable state preservation by returning [`false`](https://developer.apple.com/documentation/Swift/false), which you may want to do during testing, for example.

You can add version information or any other contextual data to the provided coder as necessary. During restoration, you can use that information to determine whether to proceed with restoring your app to its previous state. Any objects you add to the coder must adopt the [`NSSecureCoding`](https://developer.apple.com/documentation/Foundation/NSSecureCoding) protocol.

This method supersedes [`application(_:shouldSaveApplicationState:)`](uiapplicationdelegate/application(_:shouldsaveapplicationstate:).md). If your delegate implements both methods, the system only calls this one.

## Parameters

- `application`: The singleton app object.
- `coder`: A keyed archiver where you can store high-level state information. The coder’s   property is set to  , and any objects you encode must adopt  .

## See Also

- [func application(UIApplication, shouldRestoreSecureApplicationState: NSCoder) -> Bool](uiapplicationdelegate/application(_:shouldrestoresecureapplicationstate:).md)
  Asks the delegate whether to restore the app’s saved state.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:shouldsavesecureapplicationstate:))*