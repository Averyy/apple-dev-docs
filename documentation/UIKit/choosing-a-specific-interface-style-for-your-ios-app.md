# Choosing a specific interface style for your iOS app

**Framework**: UIKit

Adopt a specific interface style for your views, view controllers, or app when it is inappropriate to support both light and dark variants.

#### Overview

Supporting both light and dark appearances is a good practice, but you might have good reasons to opt out of appearance changes wholly or partially in your app. Views containing user-created content should always reflect the user’s choices. Similarly, you might choose a specific appearance for print-related views so that they reflect what the user sees on the printed page.

The system assumes that apps linked against the iOS 13 or later SDK support both light and dark appearances. In iOS, you specify the specific appearance you want by assigning a specific interface style to your window, view, or view controller. You can also disable support for Dark Mode entirely using an `Info.plist` key.

For general information about how to support Dark Mode, see [`Supporting Dark Mode in your interface`](supporting-dark-mode-in-your-interface.md).

##### Override the Interface Style for a Window View or View Controller

When your interface must always appear in a light or dark style, regardless of the system setting, set the [`overrideUserInterfaceStyle`](uiview/overrideuserinterfacestyle.md) property of the appropriate window, view, or view controller to that style. Overriding the interface style affects other objects in your interface as follows:

- View controllers—The view controller’s views and child view controllers adopt the style.
- Views—The view and all of its subviews adopt the style.
- Windows—Everything in the window adopts the style, including the root view controller and all presentation controllers that display content in that window.

The following code example enables a light appearance for a view controller and all of its views.

```swift
    override func viewDidLoad() {
        super.viewDidLoad()

        // Always adopt a light interface style.    
        overrideUserInterfaceStyle = .light
    }
```

##### Override the Interface Style for Child View Controllers

Parent view controllers control the appearance of their contained child view controllers. To override the interface style for a child view controller, use the [`setOverrideTraitCollection(_:forChild:)`](uiviewcontroller/setoverridetraitcollection(_:forchild:).md) method to assign new traits to that view controller. For custom presentations, you can similarly override the interface style of the presented view controller by assigning new traits to the [`overrideTraitCollection`](uipresentationcontroller/overridetraitcollection.md) property of your [`UIPresentationController`](uipresentationcontroller.md) object.

##### Opt Out of Dark Mode Entirely

The system automatically opts in any app linked against the iOS 13.0 or later SDK to both light and dark appearances. If you need extra time to work on your app’s Dark Mode support, you can temporarily opt out by including the [`UIUserInterfaceStyle`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UIUserInterfaceStyle) key (with a value of `Light`) in your app’s `Info.plist` file. Setting this key to `Light` causes the system to ignore the user’s preference and always apply a light appearance to your app.

> ❗ **Important**:  Supporting Dark Mode is strongly encouraged. Use the [`UIUserInterfaceStyle`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UIUserInterfaceStyle) key to opt out only temporarily while you work on improvements to your app’s Dark Mode support.

 Supporting Dark Mode is strongly encouraged. Use the [`UIUserInterfaceStyle`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UIUserInterfaceStyle) key to opt out only temporarily while you work on improvements to your app’s Dark Mode support.

## See Also

- [Choosing a Specific Appearance for Your macOS App](../AppKit/choosing-a-specific-appearance-for-your-macos-app.md)
  Adopt a specific appearance for your windows, views, or app when it is inappropriate to support both light and dark variants.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/choosing-a-specific-interface-style-for-your-ios-app)*