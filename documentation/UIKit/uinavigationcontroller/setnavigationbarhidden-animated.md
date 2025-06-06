# setNavigationBarHidden(_:animated:)

**Framework**: UIKit  
**Kind**: method

Sets whether the navigation bar is hidden.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setNavigationBarHidden(_ hidden: Bool, animated: Bool)
```

#### Discussion

For animated transitions, the duration of the animation is specified by the value in the [`hideShowBarDuration`](uinavigationcontroller/hideshowbarduration.md) constant.

## Parameters

- `hidden`: Specify   to hide the navigation bar or   to show it.
- `animated`: Specify   if you want to animate the change in visibility or   if you want the navigation bar to appear immediately.

## See Also

- [var isNavigationBarHidden: Bool](uinavigationcontroller/isnavigationbarhidden.md)
  A Boolean value that indicates whether the navigation bar is hidden.
- [var navigationBar: UINavigationBar](uinavigationcontroller/navigationbar.md)
  The navigation bar managed by the navigation controller.
- [Customizing your app’s navigation bar](customizing-your-app-s-navigation-bar.md)
  Create custom titles, prompts, and buttons in your app’s navigation bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationcontroller/setnavigationbarhidden(_:animated:))*