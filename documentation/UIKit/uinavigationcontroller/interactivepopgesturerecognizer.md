# interactivePopGestureRecognizer

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The gesture recognizer that handles interactively popping the top view controller off the navigation stack when a person swipes from the leading screen edge.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var interactivePopGestureRecognizer: UIGestureRecognizer? { get }
```

```objc
@property (nonatomic, readonly, nullable) UIGestureRecognizer * interactivePopGestureRecognizer;
```

## Discussion

The navigation controller installs this gesture recognizer on its view and uses it to pop the topmost view controller off the navigation stack when a person swipes horizontally from the leading edge of the screen.

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
- [var interactiveContentPopGestureRecognizer: UIGestureRecognizer?](./interactivecontentpopgesturerecognizer.md)
  The gesture recognizer that handles interactively popping the top view controller off the navigation stack when a person pans horizontally in the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationcontroller/interactivepopgesturerecognizer)*