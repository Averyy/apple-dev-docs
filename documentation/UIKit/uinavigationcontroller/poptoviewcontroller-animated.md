# popToViewController(_:animated:)

**Framework**: UIKit  
**Kind**: method

Pops view controllers until the specified view controller is at the top of the navigation stack.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func popToViewController(_ viewController: UIViewController, animated: Bool) -> [UIViewController]?
```

#### Return Value

An array containing the view controllers that were popped from the stack.

#### Discussion

For information on how the navigation bar is updated, see [`Updating the navigation bar`](uinavigationcontroller#Updating-the-navigation-bar.md).

## Parameters

- `viewController`: The view controller that you want to be at the top of the stack. This view controller must currently be on the navigation stack.
- `animated`: Set this value to   to animate the transition. Pass   if you are setting up a navigation controller before its view is displayed.

## See Also

- [func pushViewController(UIViewController, animated: Bool)](uinavigationcontroller/pushviewcontroller(_:animated:).md)
  Pushes a view controller onto the receiver’s stack and updates the display.
- [func popViewController(animated: Bool) -> UIViewController?](uinavigationcontroller/popviewcontroller(animated:).md)
  Pops the top view controller from the navigation stack and updates the display.
- [func popToRootViewController(animated: Bool) -> [UIViewController]?](uinavigationcontroller/poptorootviewcontroller(animated:).md)
  Pops all the view controllers on the stack except the root view controller and updates the display.
- [var interactivePopGestureRecognizer: UIGestureRecognizer?](uinavigationcontroller/interactivepopgesturerecognizer.md)
  The gesture recognizer responsible for popping the top view controller off the navigation stack when a person swipes from the leading screen edge.
- [var interactiveContentPopGestureRecognizer: UIGestureRecognizer?](uinavigationcontroller/interactivecontentpopgesturerecognizer.md)
  The gesture recognizer that handles interactively popping the top view controller off the navigation stack when a person pans horizontally in the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationcontroller/poptoviewcontroller(_:animated:))*