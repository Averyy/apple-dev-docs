# navigationController(_:willShow:animated:)

**Framework**: UIKit  
**Kind**: method

Notifies the delegate before the navigation controller displays a view controller’s view and navigation item properties.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func navigationController(_ navigationController: UINavigationController, willShow viewController: UIViewController, animated: Bool)
```

## Mentions

- [Enhancing your app with fluid transitions](enhancing-your-app-with-fluid-transitions.md)

## Parameters

- `navigationController`: The navigation controller that is showing the view and properties of a view controller.
- `viewController`: The view controller whose view and navigation item properties are being shown.
- `animated`:   to animate the transition; otherwise,  .

## See Also

- [func navigationController(UINavigationController, didShow: UIViewController, animated: Bool)](uinavigationcontrollerdelegate/navigationcontroller(_:didshow:animated:).md)
  Notifies the delegate after the navigation controller displays a view controller’s view and navigation item properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationcontrollerdelegate/navigationcontroller(_:willshow:animated:))*