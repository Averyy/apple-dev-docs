# navigationBar

**Framework**: UIKit  
**Kind**: property

The navigation bar managed by the navigation controller.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var navigationBar: UINavigationBar { get }
```

#### Discussion

It is permissible to customize the appearance of the navigation bar using the methods and properties of the [`UINavigationBar`](uinavigationbar.md) class but you must never change its [`frame`](uiview/frame.md), [`bounds`](uiview/bounds.md), or [`alpha`](uiview/alpha.md) values or modify its view hierarchy directly. To show or hide the navigation bar, you should always do so through the navigation controller by changing its [`isNavigationBarHidden`](uinavigationcontroller/isnavigationbarhidden.md) property or calling the [`setNavigationBarHidden(_:animated:)`](uinavigationcontroller/setnavigationbarhidden(_:animated:).md) method.

## See Also

- [func setNavigationBarHidden(Bool, animated: Bool)](uinavigationcontroller/setnavigationbarhidden(_:animated:).md)
  Sets whether the navigation bar is hidden.
- [Customizing your app’s navigation bar](customizing-your-app-s-navigation-bar.md)
  Create custom titles, prompts, and buttons in your app’s navigation bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationcontroller/navigationbar)*