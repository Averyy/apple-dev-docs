# Optimizing your iPad app for Mac

**Framework**: UIKit

Make your iPad app more like a Mac app by taking advantage of system features in macOS.

#### Overview

The Mac version of your iPad app supports many system features found in macOS without requiring any effort from you, including:

- A default menu bar for your app
- Support for trackpad, mouse, and keyboard input
- Support for window resizing and full-screen display
- Mac-style scroll bars
- Copy-and-paste support
- Drag-and-drop support
- Support for system Touch Bar controls

You can, however, extend your app to take advantage of even more system features.

> ❗ **Important**:  Mac apps built with Mac Catalyst can only use [`AppKit`](https://developer.apple.com/documentation/AppKit) APIs marked as available in Mac Catalyst, such as [`NSToolbar`](https://developer.apple.com/documentation/AppKit/NSToolbar) and [`NSTouchBar`](https://developer.apple.com/documentation/AppKit/NSTouchBar). Mac Catalyst doesn’t support accessing unavailable AppKit APIs.

 Mac apps built with Mac Catalyst can only use [`AppKit`](https://developer.apple.com/documentation/AppKit) APIs marked as available in Mac Catalyst, such as [`NSToolbar`](https://developer.apple.com/documentation/AppKit/NSToolbar) and [`NSTouchBar`](https://developer.apple.com/documentation/AppKit/NSTouchBar). Mac Catalyst doesn’t support accessing unavailable AppKit APIs.

##### Add Menu Bar Items

The Mac version of your app comes with a standard menu bar. Customize it by adding and removing menu items using [`UIMenuBuilder`](uimenubuilder.md). To learn more, see [`Adding menus and shortcuts to the menu bar and user interface`](adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface.md).

##### Show a Preferences Window

Mac apps typically let users manage app-specific settings by displaying a Preferences window. Users see this window by selecting the app menu followed by the Preferences menu item in the menu bar. If your app has a Settings bundle, the system automatically provides your app with a preferences window. To learn more, see [`Displaying a Preferences window`](displaying-a-preferences-window.md).

##### Apply a Translucent Background to Your Primary View Controller

iPad apps using a split view controller get a Mac-style vertical split view when running in macOS. But to make your iPad app look more at home on Mac, apply a translucent effect that blurs the desktop into the primary view controller’s background. To do this, set your split view controller’s [`primaryBackgroundStyle`](uisplitviewcontroller/primarybackgroundstyle.md) to [`UISplitViewController.BackgroundStyle.sidebar`](uisplitviewcontroller/backgroundstyle/sidebar.md), as shown in the following code.

```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {

    let splitViewController = window!.rootViewController as! UISplitViewController
    let navigationController = splitViewController.viewControllers[splitViewController.viewControllers.count-1] as! UINavigationController
    navigationController.topViewController!.navigationItem.leftBarButtonItem = splitViewController.displayModeButtonItem
    
    // Add a translucent background to the primary view controller.
    splitViewController.primaryBackgroundStyle = .sidebar
    
    splitViewController.delegate = self
    
    return true
}
```

##### Detect the Pointer in a View

Mac users rely on a pointer to interact with apps, whether selecting a text field or moving a window. As the user moves the pointer over UI elements, some elements should change their appearance. For example, a web browser highlights a link as the pointer moves over it.

To detect when the user moves the pointer over a view in your app, add a [`UIHoverGestureRecognizer`](uihovergesturerecognizer.md) to that view. This tells your app when the pointer enters or leaves the view, or moves while over it.

```swift
class ViewController: UIViewController {

    @IBOutlet var button: UIButton!

    override func viewDidLoad() {
        super.viewDidLoad()

        let hover = UIHoverGestureRecognizer(target: self, action: #selector(hovering(_:)))
        button.addGestureRecognizer(hover)
    }

    @objc
    func hovering(_ recognizer: UIHoverGestureRecognizer) {
        switch recognizer.state {
        case .began, .changed:
            button.titleLabel?.textColor = #colorLiteral(red: 1, green: 0, blue: 0, alpha: 1)
        case .ended:
            button.titleLabel?.textColor = UIColor.link
        default:
            break
        }
    }
}
```

## See Also

- [Bring an iPad App to the Mac with Mac Catalyst](https://developer.apple.com/tutorials/Mac-Catalyst)
  Build a native Mac app from the same codebase as your iPad app.
- [Choosing a user interface idiom for your Mac app](choosing-a-user-interface-idiom-for-your-mac-app.md)
  Select the iPad or the Mac user interface idiom in your Mac app built with Mac Catalyst.
- [LSMinimumSystemVersion](../BundleResources/Information-Property-List/LSMinimumSystemVersion.md)
  The minimum version of the operating system required for the app to run in macOS.
- [UIApplicationSupportsTabbedSceneCollection](../BundleResources/Information-Property-List/UIApplicationSceneManifest/UIApplicationSupportsTabbedSceneCollection.md)
  A Boolean value indicating whether an app built with Mac Catalyst supports automatic tabbing mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/optimizing-your-ipad-app-for-mac)*