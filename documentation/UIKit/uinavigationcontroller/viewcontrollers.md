# viewControllers

**Framework**: UIKit  
**Kind**: property

The view controllers currently on the navigation stack.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var viewControllers: [UIViewController] { get set }
```

#### Discussion

The root view controller is at index `0` in the array, the back view controller is at index `n-2`, and the top controller is at index `n-1`, where `n` is the number of items in the array.

Assigning a new array of view controllers to this property is equivalent to calling the [`setViewControllers(_:animated:)`](uinavigationcontroller/setviewcontrollers(_:animated:).md) method with the `animated` parameter set to [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var topViewController: UIViewController?](uinavigationcontroller/topviewcontroller.md)
  The view controller at the top of the navigation stack.
- [var visibleViewController: UIViewController?](uinavigationcontroller/visibleviewcontroller.md)
  The view controller associated with the currently visible view in the navigation interface.
- [func setViewControllers([UIViewController], animated: Bool)](uinavigationcontroller/setviewcontrollers(_:animated:).md)
  Replaces the view controllers currently managed by the navigation controller with the specified items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationcontroller/viewcontrollers)*