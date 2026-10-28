# navigationBar

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The navigation bar managed by the navigation controller.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var navigationBar: UINavigationBar { get }
```

```objc
@property (nonatomic, readonly) UINavigationBar * navigationBar;
```

## Discussion

It is permissible to customize the appearance of the navigation bar using the methods and properties of the [`UINavigationBar`](../uinavigationbar.md) class but you must never change its [`frame`](../uiview/frame.md), [`bounds`](../uiview/bounds.md), or [`alpha`](../uiview/alpha.md) values or modify its view hierarchy directly. To show or hide the navigation bar, you should always do so through the navigation controller by changing its [`isNavigationBarHidden`](./isnavigationbarhidden.md) property or calling the [`setNavigationBarHidden(_:animated:)`](./setnavigationbarhidden%28_,animated%29.md) method.

## See Also

### Configuring navigation bars
- [func setNavigationBarHidden(Bool, animated: Bool)](./setnavigationbarhidden%28_,animated%29.md)
  Sets whether the navigation bar is hidden.
- [Customizing your app’s navigation bar](../customizing-your-app-s-navigation-bar.md)
  Create custom titles, prompts, and buttons in your app’s navigation bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationcontroller/navigationbar)*