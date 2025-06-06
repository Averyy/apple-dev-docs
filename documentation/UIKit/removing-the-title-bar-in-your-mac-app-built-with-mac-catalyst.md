# Removing the title bar in your Mac app built with Mac Catalyst

**Framework**: UIKit

Display content that fills the entire height of a window by removing the title bar.

#### Overview

By default, Mac apps built with Mac Catalyst display a title bar across the top of their windows. A horizontal line separates the title bar from the content of the window.

Some Mac apps such as Messages and Contacts have no title bar in their main window. Instead, the top of the window shows only the Close, Minimize, and Zoom buttons with no separator between them and the window’s content. In this UI design, the content area fills the entire height of the window.

The following image illustrates these styles in two windows. The first window displays a title bar, while the second has none.

![Screenshot of two windows, one stacked above the other, with a dark background in the content area of each window.](https://docs-assets.developer.apple.com/published/125be45fc6704d3881a3e241a6706782/media-3507886%402x.png)

##### Remove the Title Bar

If you choose to design your window without a title bar, you must remove it from the window. To remove the title bar, set the title bar’s [`titleVisibility`](uititlebar/titlevisibility.md) property to [`UITitlebarTitleVisibility.hidden`](uititlebartitlevisibility/hidden.md) and the [`toolbar`](uititlebar/toolbar.md) property to `nil`. The following code shows how to remove the title bar and its separator from the window during the setup of a new scene.

```swift
func scene(_ scene: UIScene, willConnectTo session: UISceneSession, options connectionOptions: UIScene.ConnectionOptions) {
    
    guard let windowScene = (scene as? UIWindowScene) else { return }
    
    #if targetEnvironment(macCatalyst)
    if let titlebar = windowScene.titlebar {
        titlebar.titleVisibility = .hidden
        titlebar.toolbar = nil
    }
    #endif

}
```

## See Also

- [UIKit Catalog: Creating and customizing views and controls](uikit-catalog-creating-and-customizing-views-and-controls.md)
  Customize your app’s user interface with views and controls.
- [Building and improving your app with Mac Catalyst](building-and-improving-your-app-with-mac-catalyst.md)
  Improve your iPadOS app with Mac Catalyst by supporting native controls, multiple windows, sharing, printing, menus and keyboard shortcuts.
- [Displaying a checkbox in your Mac app built with Mac Catalyst](displaying-a-checkbox-in-your-mac-app-built-with-mac-catalyst.md)
  Present a switch control as a Mac-style checkbox when your app runs in the Mac user interface idiom.
- [Toolbar](toolbar.md)
  Provide a space for controls under a window’s title bar and above your custom content.
- [Touch Bar](../AppKit/touch-bar.md)
  Display interactive content and controls in the Touch Bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/removing-the-title-bar-in-your-mac-app-built-with-mac-catalyst)*