# Appearance customization

**Framework**: UIKit

Apply Liquid Glass to views, support Dark Mode in your app, customize the appearance of bars, and use appearance proxies to modify your UI.

## Topics

### Liquid Glass effects
- [class UIGlassEffect](uiglasseffect.md)
  A visual effect that renders a glass material.
- [class UIGlassContainerEffect](uiglasscontainereffect.md)
  A `UIGlassContainerEffect` renders multiple glass elements into a combined effect.
### Interacting with adjacent views
- [class UIBackgroundExtensionView](uibackgroundextensionview.md)
  A view that extends content to fill its own bounds.
- [class UIScrollEdgeElementContainerInteraction](uiscrolledgeelementcontainerinteraction.md)
  Add this interaction to a container view of views that overlay the edge of a scroll view. Any descendants of this view that should affect the shape of the edge effect, such as labels, images, glass views, and controls, will automatically do so.
### Dark Mode
- [Supporting Dark Mode in your interface](supporting-dark-mode-in-your-interface.md)
  Update colors, images, and behaviors so that your app adapts automatically when Dark Mode is active.
- [Adopting iOS Dark Mode](adopting-ios-dark-mode.md)
  Adopt Dark Mode in your iOS app by using dynamic colors and visual effects.
### Appearance and content
- [Configurations](configurations.md)
  Specify the appearance and content of your views and cells using configurations.
- [Automatic trait tracking](automatic-trait-tracking.md)
  Reduce the need to manually register for trait changes when you use traits within a method or closure that supports automatic trait tracking.
### Navigation bar appearance
- [class UINavigationBarAppearance](uinavigationbarappearance.md)
  An object for customizing the appearance of a navigation bar.
### Toolbar appearance
- [class UIToolbarAppearance](uitoolbarappearance.md)
  An object for customizing the appearance of a toolbar.
### Tab bar appearance
- [class UITabBarAppearance](uitabbarappearance.md)
  An object for customizing the appearance of a tab bar.
- [class UITabBarItemAppearance](uitabbaritemappearance.md)
  An object for customizing the appearance of tab bar items.
- [class UITabBarItemStateAppearance](uitabbaritemstateappearance.md)
  A data object containing the specific customizations for tab bar items in a particular state.
### Shared appearance
- [class UIBarAppearance](uibarappearance.md)
  An object for customizing the basic appearance of system bars.
- [class UIBarButtonItemAppearance](uibarbuttonitemappearance.md)
  An object for customizing the appearance of bar button items.
- [class UIBarButtonItemStateAppearance](uibarbuttonitemstateappearance.md)
  A data object containing the specific customizations for a bar button item in a particular state.
### Appearance proxies
- [protocol UIAppearance](uiappearance.md)
  A collection of methods that gives you access to the appearance proxy for a class.
- [protocol UIAppearanceContainer](uiappearancecontainer.md)
  A protocol that a class must adopt to allow appearance customization using the [`UIAppearance`](uiappearance.md) API.

## See Also

- [Views and controls](views-and-controls.md)
  Present your content onscreen and define the interactions allowed with that content.
- [View controllers](view-controllers.md)
  Manage your interface using view controllers and facilitate navigation around your app’s content.
- [View layout](view-layout.md)
  Use stack views to lay out the views of your interface automatically. Use Auto Layout when you require precise placement of your views.
- [Animation and haptics](animation-and-haptics.md)
  Provide feedback to users using view-based animations and haptics.
- [Windows and screens](windows-and-screens.md)
  Provide a container for your view hierarchies and other content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/appearance-customization)*