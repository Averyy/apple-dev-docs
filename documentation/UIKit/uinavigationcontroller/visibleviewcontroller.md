# visibleViewController

**Framework**: UIKit  
**Kind**: property

The view controller associated with the currently visible view in the navigation interface.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var visibleViewController: UIViewController? { get }
```

#### Discussion

The currently visible view can belong either to the view controller at the top of the navigation stack or to a view controller that was presented modally on top of the navigation controller itself.

## See Also

- [var topViewController: UIViewController?](uinavigationcontroller/topviewcontroller.md)
  The view controller at the top of the navigation stack.
- [var viewControllers: [UIViewController]](uinavigationcontroller/viewcontrollers.md)
  The view controllers currently on the navigation stack.
- [func setViewControllers([UIViewController], animated: Bool)](uinavigationcontroller/setviewcontrollers(_:animated:).md)
  Replaces the view controllers currently managed by the navigation controller with the specified items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationcontroller/visibleviewcontroller)*