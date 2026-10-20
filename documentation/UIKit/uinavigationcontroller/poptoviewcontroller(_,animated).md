# popToViewController(_:animated:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Pops view controllers until the specified view controller is at the top of the navigation stack.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func popToViewController(_ viewController: UIViewController, animated: Bool) -> [UIViewController]?
```

```objc
- (NSArray<__kindof UIViewController *> *) popToViewController:(UIViewController *) viewController animated:(BOOL) animated;
```

#### Return Value

An array containing the view controllers that were popped from the stack.

#### Discussion

For information on how the navigation bar is updated, see doc:UINavigationController#Updating-the-navigation-bar.

## Parameters

- `viewController`: The view controller that you want to be at the top of the stack. This view controller must currently be on the navigation stack.
- `animated`: Set this value to [`true`](../../Swift/true.md) to animate the transition. Pass [`false`](../../Swift/false.md) if you are setting up a navigation controller before its view is displayed.

## See Also

### Pushing and popping stack items
- [func pushViewController(UIViewController, animated: Bool)](./pushviewcontroller%28_,animated%29.md)
  Pushes a view controller onto the receiver’s stack and updates the display.
- [func popViewController(animated: Bool) -> UIViewController?](./popviewcontroller%28animated%29.md)
  Pops the top view controller from the navigation stack and updates the display.
- [func popToRootViewController(animated: Bool) -> [UIViewController]?](./poptorootviewcontroller%28animated%29.md)
  Pops all the view controllers on the stack except the root view controller and updates the display.
- [var interactivePopGestureRecognizer: UIGestureRecognizer?](./interactivepopgesturerecognizer.md)
  The gesture recognizer that handles interactively popping the top view controller off the navigation stack when a person swipes from the leading screen edge.
- [var interactiveContentPopGestureRecognizer: UIGestureRecognizer?](./interactivecontentpopgesturerecognizer.md)
  The gesture recognizer that handles interactively popping the top view controller off the navigation stack when a person pans horizontally in the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationcontroller/poptoviewcontroller(_:animated:))*