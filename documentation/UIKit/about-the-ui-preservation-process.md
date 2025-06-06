# About the UI preservation process

**Framework**: UIKit

Learn how to customize the UIKit state preservation process.

#### Overview

The following diagram shows the sequence of calls that happens during the interface preservation process. After asking your app delegate if you want your app state to be preserved, UIKit encodes the objects currently in your app’s view controller hierarchy. Only view controllers with a valid [`restorationIdentifier`](uiviewcontroller/restorationidentifier.md) are preserved.

![Flow diagram of the interface preservation process.](https://docs-assets.developer.apple.com/published/efccc1e96d24bdb1968ccf71485a4d33/media-2928966%402x.png)

The preservation process walks your view controller hierarchy and recursively encodes the objects that it finds. The process starts with the root view controllers of your app’s windows, which write their data to the provided archive. If the root view controller’s data includes references to other view controllers, UIKit asks each new view controller to encode its data in a separate portion of the archive. Those child view controllers may then encode their own children, and so on.

UIKit view controllers automatically encode their child view controllers, as appropriate. If you define a custom container view controller, your view controller’s [`encodeRestorableState(with:)`](uistaterestoring/encoderestorablestate(with:).md) method must similarly write any child view controllers to the provided archive.

##### Exclude View Controllers From Preservation

There are two ways to exclude a view controller (and its views) from the state restoration process:

- Set its [`restorationIdentifier`](uiviewcontroller/restorationidentifier.md) property to `nil`.
- Provide a restoration class and return `nil` from the [`viewController(withRestorationIdentifierPath:coder:)`](uiviewcontrollerrestoration/viewcontroller(withrestorationidentifierpath:coder:).md) method.

Excluding a view controller prevents that view controller from being saved in the archive. It also excludes all of the view controller’s children from being preserved.

##### Encode Any Object in Your App

State restoration isn’t limited to your app’s views and view controllers. Any object that adopts the [`UIStateRestoring`](uistaterestoring.md) protocol can also be included in the restoration archive. For example, you might adopt this protocol in an object that stores global configuration data for your app. To add an object like this to the archive:

1. Register the object while your app is running by calling the [`registerObject(forStateRestoration:restorationIdentifier:)`](uiapplication/registerobject(forstaterestoration:restorationidentifier:).md) method of [`UIApplication`](uiapplication.md). For example, you might register a configuration object immediately after creating it.
2. In one of your [`encodeRestorableState(with:)`](uistaterestoring/encoderestorablestate(with:).md) methods, encode the object into the restoration archive. You can also encode it in your app delegate’s [`application(_:willEncodeRestorableStateWith:)`](uiapplicationdelegate/application(_:willencoderestorablestatewith:).md) method.

You can encode any data you want for your custom objects, as long as it’s sufficient to return that object to its previous state during the next launch cycle. Encode data that isn’t crucial to your app’s behavior, and never encode data that should be persisted in other ways. For example, don’t encode your app’s settings or user data that must persist between launch cycles.

## See Also

- [About the UI restoration process](about-the-ui-restoration-process.md)
  Learn how to customize the UIKit state restoration process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/about-the-ui-preservation-process)*