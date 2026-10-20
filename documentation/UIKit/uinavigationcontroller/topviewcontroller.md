# topViewController

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The view controller at the top of the navigation stack.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var topViewController: UIViewController? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) UIViewController * topViewController;
```

## See Also

### Accessing items on the navigation stack
- [var visibleViewController: UIViewController?](./visibleviewcontroller.md)
  The view controller associated with the currently visible view in the navigation interface.
- [var viewControllers: [UIViewController]](./viewcontrollers.md)
  The view controllers currently on the navigation stack.
- [func setViewControllers([UIViewController], animated: Bool)](./setviewcontrollers%28_,animated%29.md)
  Replaces the view controllers currently managed by the navigation controller with the specified items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationcontroller/topviewcontroller)*