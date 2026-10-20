# navigationController(_:didShow:animated:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Notifies the delegate after the navigation controller displays a view controller’s view and navigation item properties.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
optional func navigationController(_ navigationController: UINavigationController, didShow viewController: UIViewController, animated: Bool)
```

```objc
- (void) navigationController:(UINavigationController *) navigationController didShowViewController:(UIViewController *) viewController animated:(BOOL) animated;
```

## Mentions

- [Enhancing your app with fluid transitions](../enhancing-your-app-with-fluid-transitions.md)

## Parameters

- `navigationController`: The navigation controller that is showing the view and properties of a view controller.
- `viewController`: The view controller whose view and navigation item properties are being shown.
- `animated`: [`true`](../../Swift/true.md) to animate the transition; otherwise, [`false`](../../Swift/false.md).

## See Also

### Responding to a view controller being shown
- [func navigationController(UINavigationController, willShow: UIViewController, animated: Bool)](./navigationcontroller%28_,willshow,animated%29.md)
  Notifies the delegate before the navigation controller displays a view controller’s view and navigation item properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationcontrollerdelegate/navigationcontroller(_:didshow:animated:))*