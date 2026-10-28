# pushViewController(_:animated:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Pushes a view controller onto the receiver’s stack and updates the display.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func pushViewController(_ viewController: UIViewController, animated: Bool)
```

```objc
- (void) pushViewController:(UIViewController *) viewController animated:(BOOL) animated;
```

## Discussion

The object in the `viewController` parameter becomes the top view controller on the navigation stack. Pushing a view controller causes its view to be embedded in the navigation interface. If the `animated` parameter is [`true`](../../Swift/true.md), the view is animated into position; otherwise, the view is simply displayed in its final location.

In addition to displaying the view associated with the new view controller at the top of the stack, this method also updates the navigation bar and tool bar accordingly. For information on how the navigation bar is updated, see doc:UINavigationController#Updating-the-navigation-bar.

## Parameters

- `viewController`: The view controller to push onto the stack. This object cannot be a tab bar controller. If the view controller is already on the navigation stack, this method throws an exception.
- `animated`: Specify [`true`](../../Swift/true.md) to animate the transition or [`false`](../../Swift/false.md) if you do not want the transition to be animated. You might specify [`false`](../../Swift/false.md) if you are setting up the navigation controller at launch time.

## See Also

### Pushing and popping stack items
- [func popViewController(animated: Bool) -> UIViewController?](./popviewcontroller%28animated%29.md)
  Pops the top view controller from the navigation stack and updates the display.
- [func popToRootViewController(animated: Bool) -> [UIViewController]?](./poptorootviewcontroller%28animated%29.md)
  Pops all the view controllers on the stack except the root view controller and updates the display.
- [func popToViewController(UIViewController, animated: Bool) -> [UIViewController]?](./poptoviewcontroller%28_,animated%29.md)
  Pops view controllers until the specified view controller is at the top of the navigation stack.
- [var interactivePopGestureRecognizer: UIGestureRecognizer?](./interactivepopgesturerecognizer.md)
  The gesture recognizer that handles interactively popping the top view controller off the navigation stack when a person swipes from the leading screen edge.
- [var interactiveContentPopGestureRecognizer: UIGestureRecognizer?](./interactivecontentpopgesturerecognizer.md)
  The gesture recognizer that handles interactively popping the top view controller off the navigation stack when a person pans horizontally in the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationcontroller/pushviewcontroller(_:animated:))*