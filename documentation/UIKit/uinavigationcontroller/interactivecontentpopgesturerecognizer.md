# interactiveContentPopGestureRecognizer

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The gesture recognizer that handles interactively popping the top view controller off the navigation stack when a person pans horizontally in the view.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- visionOS 26.0+

## Declaration

```swift
var interactiveContentPopGestureRecognizer: UIGestureRecognizer? { get }
```

```objc
@property (nonatomic, readonly, nullable) UIGestureRecognizer * interactiveContentPopGestureRecognizer;
```

#### Discussion

The navigation controller installs this gesture recognizer on its view and uses it to interactively pop the topmost view controller off the navigation stack when a person initially pans horizontally in a leading to trailing direction in the view. It recognizes a gesture on the entire content area of the navigation controller in cases that are not covered by [`interactivePopGestureRecognizer`](./interactivepopgesturerecognizer.md) and initiates an interactive pop.

Use this property to retrieve the gesture recognizer and tie it to the behavior of other gesture recognizers in your user interface.

## See Also

### Pushing and popping stack items
- [func pushViewController(UIViewController, animated: Bool)](./pushviewcontroller%28_,animated%29.md)
  Pushes a view controller onto the receiver’s stack and updates the display.
- [func popViewController(animated: Bool) -> UIViewController?](./popviewcontroller%28animated%29.md)
  Pops the top view controller from the navigation stack and updates the display.
- [func popToRootViewController(animated: Bool) -> [UIViewController]?](./poptorootviewcontroller%28animated%29.md)
  Pops all the view controllers on the stack except the root view controller and updates the display.
- [func popToViewController(UIViewController, animated: Bool) -> [UIViewController]?](./poptoviewcontroller%28_,animated%29.md)
  Pops view controllers until the specified view controller is at the top of the navigation stack.
- [var interactivePopGestureRecognizer: UIGestureRecognizer?](./interactivepopgesturerecognizer.md)
  The gesture recognizer that handles interactively popping the top view controller off the navigation stack when a person swipes from the leading screen edge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationcontroller/interactivecontentpopgesturerecognizer)*