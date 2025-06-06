# popToRootViewController(animated:)

**Framework**: UIKit  
**Kind**: method

Pops all the view controllers on the stack except the root view controller and updates the display.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func popToRootViewController(animated: Bool) -> [UIViewController]?
```

#### Return Value

An array of view controllers representing the items that were popped from the stack.

#### Discussion

The root view controller becomes the top view controller. For information on how the navigation bar is updated, see [`Updating the navigation bar`](uinavigationcontroller#Updating-the-navigation-bar.md).

## Parameters

- `animated`: Set this value to   to animate the transition. Pass   if you are setting up a navigation controller before its view is displayed.

## See Also

- [func pushViewController(UIViewController, animated: Bool)](uinavigationcontroller/pushviewcontroller(_:animated:).md)
  Pushes a view controller onto the receiver’s stack and updates the display.
- [func popViewController(animated: Bool) -> UIViewController?](uinavigationcontroller/popviewcontroller(animated:).md)
  Pops the top view controller from the navigation stack and updates the display.
- [func popToViewController(UIViewController, animated: Bool) -> [UIViewController]?](uinavigationcontroller/poptoviewcontroller(_:animated:).md)
  Pops view controllers until the specified view controller is at the top of the navigation stack.
- [var interactivePopGestureRecognizer: UIGestureRecognizer?](uinavigationcontroller/interactivepopgesturerecognizer.md)
  The gesture recognizer responsible for popping the top view controller off the navigation stack.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationcontroller/poptorootviewcontroller(animated:))*