# popViewController(animated:)

**Framework**: UIKit  
**Kind**: method

Pops the top view controller from the navigation stack and updates the display.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func popViewController(animated: Bool) -> UIViewController?
```

#### Return Value

The view controller that was popped from the stack.

#### Discussion

This method removes the top view controller from the stack and makes the new top of the stack the active view controller. If the view controller at the top of the stack is the root view controller, this method does nothing. In other words, you cannot pop the last item on the stack.

In addition to displaying the view associated with the new view controller at the top of the stack, this method also updates the navigation bar and tool bar accordingly. For information on how the navigation bar is updated, see [`Updating the navigation bar`](uinavigationcontroller#Updating-the-navigation-bar.md).

## Parameters

- `animated`: Set this value to   to animate the transition. Pass   if you are setting up a navigation controller before its view is displayed.

## See Also

- [func pushViewController(UIViewController, animated: Bool)](uinavigationcontroller/pushviewcontroller(_:animated:).md)
  Pushes a view controller onto the receiver’s stack and updates the display.
- [func popToRootViewController(animated: Bool) -> [UIViewController]?](uinavigationcontroller/poptorootviewcontroller(animated:).md)
  Pops all the view controllers on the stack except the root view controller and updates the display.
- [func popToViewController(UIViewController, animated: Bool) -> [UIViewController]?](uinavigationcontroller/poptoviewcontroller(_:animated:).md)
  Pops view controllers until the specified view controller is at the top of the navigation stack.
- [var interactivePopGestureRecognizer: UIGestureRecognizer?](uinavigationcontroller/interactivepopgesturerecognizer.md)
  The gesture recognizer responsible for popping the top view controller off the navigation stack.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationcontroller/popviewcontroller(animated:))*