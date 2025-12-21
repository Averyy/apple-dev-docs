# interactiveContentPopGestureRecognizer

**Framework**: UIKit  
**Kind**: property

The gesture recognizer that handles interactively popping the top view controller off the navigation stack when a person pans horizontally in the view.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
var interactiveContentPopGestureRecognizer: UIGestureRecognizer? { get }
```

#### Overview

The navigation controller installs this gesture recognizer on its view and uses it to interactively pop the topmost view controller off the navigation stack when a person initially pans horizontally in a leading to trailing direction in the view. It recognizes a gesture on the entire content area of the navigation controller in cases that are not covered by [`interactivePopGestureRecognizer`](uinavigationcontroller/interactivepopgesturerecognizer.md) and initiates an interactive pop.

Use this property to retrieve the gesture recognizer and tie it to the behavior of other gesture recognizers in your user interface.

## See Also

- [func pushViewController(UIViewController, animated: Bool)](uinavigationcontroller/pushviewcontroller(_:animated:).md)
  Pushes a view controller onto the receiver’s stack and updates the display.
- [func popViewController(animated: Bool) -> UIViewController?](uinavigationcontroller/popviewcontroller(animated:).md)
  Pops the top view controller from the navigation stack and updates the display.
- [func popToRootViewController(animated: Bool) -> [UIViewController]?](uinavigationcontroller/poptorootviewcontroller(animated:).md)
  Pops all the view controllers on the stack except the root view controller and updates the display.
- [func popToViewController(UIViewController, animated: Bool) -> [UIViewController]?](uinavigationcontroller/poptoviewcontroller(_:animated:).md)
  Pops view controllers until the specified view controller is at the top of the navigation stack.
- [var interactivePopGestureRecognizer: UIGestureRecognizer?](uinavigationcontroller/interactivepopgesturerecognizer.md)
  The gesture recognizer responsible for popping the top view controller off the navigation stack when a person swipes from the leading screen edge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationcontroller/interactivecontentpopgesturerecognizer)*