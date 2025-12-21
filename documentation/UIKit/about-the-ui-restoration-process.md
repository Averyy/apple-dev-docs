# About the UI restoration process

**Framework**: UIKit

Learn how to customize the UIKit state restoration process.

#### Overview

The following diagram shows the sequence of calls that happens from the time your app launches until the time it’s restored. Restoration occurs during the middle of your app’s initialization, and it proceeds only when a state restoration archive is available and your app delegate’s [`application(_:shouldRestoreApplicationState:)`](uiapplicationdelegate/application(_:shouldrestoreapplicationstate:).md) method returns [`true`](https://developer.apple.com/documentation/Swift/true).

![Flow diagram of the interface restoration process.](https://docs-assets.developer.apple.com/published/8ae9ad9ee6c3db2adb3b3d2ed01aa1a6/media-2934436%402x.png)

The first step in the restoration process is to create the view controller objects (either explicitly or implicitly) for your interface. The second step is to decode and restore the state of those objects. Both steps are needed to recreate your view controller hierarchy. For example, after the creation of a navigation controller and its child view controllers, there’s no immediate connection between those objects. It’s actually the navigation controller’s [`decodeRestorableState(with:)`](uistaterestoring/decoderestorablestate(with:).md) method that reestablishes the relationships to its child view controllers.

After state restoration finishes, UIKit calls the app delegate’s [`application(_:didFinishLaunchingWithOptions:)`](uiapplicationdelegate/application(_:didfinishlaunchingwithoptions:).md) method. Use that method to make any last minute changes or additions to your interface. For example, you might add a login screen to the view controller hierarchy.

##### Recreate Your View Controllers

During restoration, UIKit tries to create or locate view controller objects from your preserved interface. UIKit first asks you to provide the view controller object. If you don’t provide the view controller, UIKit looks for it implicitly. Here’s the sequence of steps that UIKit follows to recreate view controllers:

1.  A restoration class knows how to create a specific view controller. You designate a restoration class by assigning that class to the [`restorationClass`](uiviewcontroller/restorationclass.md) property of your view controller. During restoration, UIKit calls the [`viewController(withRestorationIdentifierPath:coder:)`](uiviewcontrollerrestoration/viewcontroller(withrestorationidentifierpath:coder:).md) method of the restoration class to request a new instance of the view controller, which your method then returns. If you return `nil`, UIKit stops trying to create the view controller and leaves it out of the restoration process.
2.  If the view controller had no restoration class, UIKit calls the [`application(_:viewControllerWithRestorationIdentifierPath:coder:)`](uiapplicationdelegate/application(_:viewcontrollerwithrestorationidentifierpath:coder:).md) method of the app delegate. If you return `nil` from that method, UIKit continues searching.
3.  UIKit looks for an already created view controller with the exact same restoration path.
4.  If it still doesn’t have the view controller, UIKit automatically instantiates it from your app’s storyboards.

Before state restoration even begins, UIKit loads your app’s default view controllers from your storyboards. Because UIKit loads these view controllers for free, it’s better not to create them using a restoration class or your app delegate. For all other view controllers, assign a restoration class only if the view controller isn’t defined in your storyboards. You might also assign a restoration class to prevent the creation of your view controller in specific circumstances. For example, you might want to avoid displaying the view controller if the associated restoration archive refers to stale or missing data.

When recreating view controllers in code, always reassign a value to the view controller’s [`restorationIdentifier`](uiviewcontroller/restorationidentifier.md) property in addition to any other initialization. Also assign a value to the [`restorationClass`](uiviewcontroller/restorationclass.md) property as appropriate. Assigning these values at creation time ensures that the view controller will be preserved during the next cycle.

```swift
func viewController(withRestorationIdentifierPath 
                    identifierComponents: [Any], 
                    coder: NSCoder) -> UIViewController? {
   let vc = MyViewController()
        
   vc.restorationIdentifier = identifierComponents.last as? String
   vc.restorationClass = MyViewController.self
        
   return vc
}
```

> **Note**:  Your restoration class should always return the class expected by UIKit. The restoration archive includes the class of each preserved view controller. If your restoration class returns an instance of a different class, UIKit doesn’t call that view controller’s [`decodeRestorableState(with:)`](uiviewcontroller/decoderestorablestate(with:).md) method.

## See Also

- [About the UI preservation process](about-the-ui-preservation-process.md)
  Learn how to customize the UIKit state preservation process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/about-the-ui-restoration-process)*