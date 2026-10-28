# presentingViewController

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The view controller that is the starting point for the presentation.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var presentingViewController: UIViewController { get }
```

```objc
@property (nonatomic, strong, readonly) UIViewController * presentingViewController;
```

## Discussion

The object in this property could be the root view controller of the window, a parent view controller that is marked as defining the current context, or the last view controller that was presented onscreen. This view controller may or may not be the same one whose [`present(_:animated:completion:)`](../uiviewcontroller/present%28_,animated,completion%29.md) method was called to initiate the presentation process. It may also not be the view controller used to initialize your presentation controller.

## See Also

### Getting the presentation objects
- [var presentedViewController: UIViewController](./presentedviewcontroller.md)
  The view controller being presented.
- [var containerView: UIView?](./containerview.md)
  The view in which the presentation occurs.
- [var presentedView: UIView?](./presentedview.md)
  The view to be animated by the animator objects during a transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipresentationcontroller/presentingviewcontroller)*